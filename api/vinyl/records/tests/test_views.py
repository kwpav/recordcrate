# This file is part of recordcrate.

# recordcrate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# recordcrate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with recordcrate.  If not, see <http://www.gnu.org/licenses/>.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from records.models import Profile
from records.models import Label
from records.models import Format
from records.models import Person
from records.models import Role
from records.models import Artist
from records.models import MasterAlbum
from records.models import Release
from records.models import Track
# the client returns the response as an OrderedDict
from collections import OrderedDict


class ProfileViewTests(APITestCase):
    url = reverse('profile-list')

    def test_profiles_url(self):
        """
        Ensure that the profile list url is '/profiles/'.
        """
        # assert
        self.assertEqual(self.url, '/profiles/')

    def test_get_profiles_ok(self):
        """
        Ensure that GET /profiles/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserViewTests(APITestCase):
    url = reverse('user-list')

    def test_users_url(self):
        """
        Ensure that the user list url is '/users/'.
        """
        # assert
        self.assertEqual(self.url, '/users/')

    def test_get_users_ok(self):
        """
        Ensure that GET /users/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LabelViewTests(APITestCase):
    url = reverse('label-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

    def test_labels_url(self):
        """
        Ensure that the label list url is '/labels/'.
        """
        # assert
        self.assertEqual(self.url, '/labels/')

    def test_get_labels_ok(self):
        """
        Ensure that GET /labels/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_label(self):
        # arrange
        data = {'name': 'MGM'}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Label.objects.count(), 1)
        self.assertEqual(Label.objects.get().name, 'MGM')

    def test_create_empty_label(self):
        # arrange
        data = {'name': ''}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Label.objects.count(), 0)

    def test_create_label_without_logging_in(self):
        # arrange
        data = {'name': 'MGM'}
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Label.objects.count(), 0)

    def test_read_label(self):
        # arrange
        Label.objects.create(
            name='MGM',
            owner=User.objects.get()
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/labels/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('name', 'MGM')
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)

    def test_update_label(self):
        # arrange
        Label.objects.create(
            name='MGM',
            owner=User.objects.get()
        )
        data = {
            'url': 'http://testserver/labels/1/',
            'id': 1,
            'owner': self.user.username,
            'name': 'MGM1',
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.put('/labels/1/', data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_delete_label(self):
        # arrange
        Label.objects.create(
            name='MGM',
            owner=User.objects.get()
        )
        # act
        response = self.client.delete(f'{self.url}/1/')
        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class FormatViewTests(APITestCase):
    url = reverse('format-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

    def test_formats_url(self):
        """
        Ensure that the format list url is '/formats/'.
        """
        # assert
        self.assertEqual(self.url, '/formats/')

    def test_get_formats_ok(self):
        """
        Ensure that GET /format/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_format(self):
        # arrange
        data = {'description': '33'}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Format.objects.count(), 1)
        self.assertEqual(Format.objects.get().description, '33')

    def test_create_empty_format(self):
        # arrange
        data = {'description': ''}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Label.objects.count(), 0)

    def test_create_format_without_logging_in(self):
        # arrange
        data = {'name': '33'}
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Format.objects.count(), 0)

    def test_read_format(self):
        # arrange
        Format.objects.create(
            description='33',
            owner=self.user
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/formats/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('description', '33')
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)

    def test_update_format(self):
        # arrange
        Format.objects.create(
            description='33',
            owner=self.user
        )
        data = {
            'url': 'http://testserver/formats/1/',
            'id': 1,
            'owner': self.user.username,
            'description': '45',
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.put('/formats/1/', data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_delete_format(self):
        # arrange
        Format.objects.create(
            description='33',
            owner=self.user
        )
        # act
        response = self.client.delete(f'{self.url}/1/')
        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PersonViewTests(APITestCase):
    url = reverse('person-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

    def test_people_url(self):
        """
        Ensure that the person list url is '/people/'.
        """
        # assert
        self.assertEqual(self.url, '/people/')

    def test_get_people_ok(self):
        """
        Ensure that GET /people/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_person(self):
        """
        Ensure that we can create a person.
        """
        # arrange
        data = {'first_name': 'Levon', 'last_name': 'Helm'}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'Levon')
        self.assertEqual(Person.objects.get().last_name, 'Helm')

    def test_create_empty_person(self):
        # arrange
        data = {'first_name': '', 'last_name': ''}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Person.objects.count(), 0)

    def test_create_person_without_logging_in(self):
        # arrange
        data = {'first_name': 'Levon', 'last_name': 'Helm'}
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Person.objects.count(), 0)

    def test_read_person(self):
        # arrange
        Person.objects.create(
            first_name='Levon',
            last_name='Helm',
            owner=self.user
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/people/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('first_name', 'Levon'),
            ('last_name', 'Helm'),
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)

    def test_update_person(self):
        # arrange
        Person.objects.create(
            first_name='Levon',
            last_name='Helm',
            owner=self.user
        )
        data = {
            'url': 'http://testserver/people/1/',
            'id': 1,
            'owner': self.user.username,
            'first_name': 'Neil',
            'last_name': 'Young'
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.put('/people/1/', data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_delete_person(self):
        # arrange
        Person.objects.create(
            first_name='Levon',
            last_name='Helm',
            owner=self.user
        )
        # act
        response = self.client.delete(f'{self.url}/1/')
        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ArtistViewTests(APITestCase):
    url = reverse('artist-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

    def test_artists_url(self):
        """
        Ensure that the artist list url is '/artists/'.
        """
        # assert
        self.assertEqual(self.url, '/artists/')

    def test_get_artists_ok(self):
        """
        Ensure that GET /artists/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_artist(self):
        # arrange
        data = {'name': 'The Band', 'members': []}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(Artist.objects.get().name, 'The Band')

    def test_create_empty_artist(self):
        # arrange
        data = {'owner': '/users/1/', 'name': '', 'members': []}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Label.objects.count(), 0)

    def test_create_artist_without_logging_in(self):
        # arrange
        data = {'owner': '/users/1/', 'name': 'The Band', 'members': []}
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Format.objects.count(), 0)

    def test_read_artist(self):
        # arrange
        Artist.objects.create(
            name='The Band',
            owner=self.user
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/artists/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('name', 'The Band'),
            ('members', []),
            ('albums', [])
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)


class MasterAlbumViewTests(APITestCase):
    url = reverse('masteralbum-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        self.artist = Artist.objects.create(
            name='The Band',
            owner=self.user
        )
        self.artist.save()

    def test_masteralbums_url(self):
        """
        Ensure that the master album list url is '/masteralbums/'.
        """
        # assert
        self.assertEqual(self.url, '/masteralbums/')

    def test_get_masteralbums_ok(self):
        """
        Ensure that GET /masteralbums/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_masteralbum(self):
        # arrange
        data = {'artists': ['/artists/1/'], 'album_name': 'The Last Waltz'}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MasterAlbum.objects.count(), 1)
        self.assertEqual(MasterAlbum.objects.get().album_name,
                         'The Last Waltz')

    def test_create_empty_masteralbum(self):
        # arrange
        data = {'artists': ['/artists/1/'], 'album_name': ''}
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MasterAlbum.objects.count(), 0)

    def test_create_masteralbum_without_logging_in(self):
        # arrange
        data = {'artists': ['/artists/1/'], 'album_name': 'The Last Waltz'}
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(MasterAlbum.objects.count(), 0)

    def test_read_masteralbum(self):
        # arrange
        album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=self.user
        )
        album.save()
        album.artists.add(self.artist)
        expected_response = [OrderedDict([
            ('url', 'http://testserver/masteralbums/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('artists', ['http://testserver/artists/1/']),
            ('album_name', 'The Last Waltz')
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)


class ReleaseViewTests(APITestCase):
    url = reverse('release-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        self.artist = Artist.objects.create(
            name='The Band',
            owner=self.user
        )
        self.artist.save()
        self.album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=self.user
        )
        self.album.save()
        self.album.artists.add(self.artist)
        self.label = Label.objects.create(
            name='MGM',
            owner=self.user
        )

    def test_releases_url(self):
        """
        Ensure that the release list url is '/releases/'.
        """
        # assert
        self.assertEqual(self.url, '/releases/')

    def test_get_releases_ok(self):
        """
        Ensure that GET /releases/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_release(self):
        # arrange
        data = {
            'master_album': '/masteralbums/1/',
            'label': '/labels/1/',
            'formats': [],
            'release_date': '1978-04-26',
            'tracks': [],
            'roles': []
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Release.objects.count(), 1)

    def test_create_empty_release(self):
        # arrange
        data = {
            'master_album': '',
            'label': '',
            'formats': [],
            'release_date': '',
            'tracks': [],
            'roles': []
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Release.objects.count(), 0)

    def test_create_release_without_logging_in(self):
        # arrange
        data = {
            'master_album': '/masteralbums/1/',
            'label': '/labels/1/',
            'formats': [],
            'release_date': '1978-04-26',
            'tracks': [],
            'roles': []
        }
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Release.objects.count(), 0)

    def test_read_release(self):
        # arrange
        Release.objects.create(
            master_album=self.album,
            label=self.label,
            release_date='1978-04-26',
            owner=self.user
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/releases/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('master_album', 'http://testserver/masteralbums/1/'),
            ('label', 'http://testserver/labels/1/'),
            ('formats', []),
            ('release_date', '1978-04-26'),
            ('tracks', []),
            ('roles', [])
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)


class TrackViewTests(APITestCase):
    url = reverse('track-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=self.user
        )
        artist.save()
        album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=self.user
        )
        album.save()
        album.artists.add(artist)
        label = Label.objects.create(
            name='MGM',
            owner=self.user
        )
        release = Release.objects.create(
            master_album=MasterAlbum.objects.get(),
            label=label,
            release_date='1978-04-26',
            owner=self.user
        )
        release.save()

    def test_tracks_url(self):
        """
        Ensure that the track list url is '/tracks/'.
        """
        self.assertEqual(self.url, '/tracks/')

    def test_get_track(self):
        """
        Ensure that GET /tracks/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_track(self):
        # arrange
        data = {
            'order': 1,
            'release': '/releases/1/',
            'side': 'A',
            'side_order': 1,
            'title': 'Theme from the last waltz',
            'duration': 120,
            'roles': []
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Track.objects.count(), 1)

    def test_create_empty_track(self):
        # arrange
        data = {
            'order': 1,
            'release': '',
            'side': '',
            'side_order': 1,
            'title': '',
            'duration': 120,
            'roles': []
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Track.objects.count(), 0)

    def test_create_track_without_logging_in(self):
        # arrange
        data = {
            'order': 1,
            'release': '/releases/1/',
            'side': 'A',
            'side_order': 1,
            'title': 'Theme from the last waltz',
            'duration': 120,
            'roles': []
        }
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Track.objects.count(), 0)

    def test_read_track(self):
        # arrange
        Track.objects.create(
            release=Release.objects.get(pk=1),
            side='A',
            side_order=1,
            order=1,
            title='Theme from the Last Waltz',
            duration=218,
            owner=self.user
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/tracks/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('order', 1),
            ('release', 'http://testserver/releases/1/'),
            ('side', 'A'),
            ('side_order', 1),
            ('title', 'Theme from the Last Waltz'),
            ('duration', 218),
            ('roles', [])
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)


class RoleViewTests(APITestCase):
    url = reverse('role-list')

    def setUp(self):
        self.user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        self.person = Person.objects.create(
            first_name='Levon',
            last_name='Helm',
            owner=self.user
        )

    def test_roles_url(self):
        """
        Ensure that the role list url is '/roles/'.
        """
        # assert
        self.assertEqual(self.url, '/roles/')

    def test_get_roles_ok(self):
        """
        Ensure that GET /roles/ responds with 200.
        """
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_role(self):
        # arrange
        data = {
            'name': 'Drummer',
            'person': '/people/1/'
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Role.objects.count(), 1)

    def test_create_empty_role(self):
        # arrange
        data = {
            'name': '',
            'person': ''
        }
        # act
        self.client.login(username=self.user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Role.objects.count(), 0)

    def test_create_role_without_logging_in(self):
        # arrange
        data = {
            'name': 'Drummer',
            'person': '/people/1/'
        }
        # act
        response = self.client.post(self.url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Role.objects.count(), 0)

    def test_read_role(self):
        # arrange
        Role.objects.create(
            name='Drummer',
            person=self.person,
            owner=self.user
        )
        expected_response = [OrderedDict([
            ('url', 'http://testserver/roles/1/'),
            ('id', 1),
            ('owner', self.user.username),
            ('name', 'Drummer'),
            ('person', 'http://testserver/people/1/')
        ])]
        # act
        response = self.client.get(self.url)
        # assert
        self.assertEqual(response.data, expected_response)
