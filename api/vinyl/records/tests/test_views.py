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
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Label.objects.count(), 1)
        self.assertEqual(Label.objects.get().name, 'MGM')

    def test_create_empty_label(self):
        # arrange
        data = {'name': ''}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
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


class FormatViewTests(APITestCase):
    url = reverse('format-list')

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
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Format.objects.count(), 1)
        self.assertEqual(Format.objects.get().description, '33')

    def test_create_empty_format(self):
        # arrange
        data = {'description': ''}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
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


class PersonViewTests(APITestCase):
    url = reverse('person-list')

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
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'Levon')
        self.assertEqual(Person.objects.get().last_name, 'Helm')

    def test_create_empty_person(self):
        # arrange
        data = {'first_name': '', 'last_name': ''}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
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


class ArtistViewTests(APITestCase):
    url = reverse('artist-list')

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
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(Artist.objects.get().name, 'The Band')

    def test_create_empty_artist(self):
        # arrange
        data = {'owner': '/users/1/', 'name': '', 'members': []}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
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


class MasterAlbumViewTests(APITestCase):
    url = reverse('masteralbum-list')

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
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()

        # act
        self.client.login(username=user.username, password='q1234567')
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
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(self.url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MasterAlbum.objects.count(), 0)

    def test_create_masteralbum_without_logging_in(self):
        # arrange
        data = {'artists': ['/artists/1/'], 'album_name': 'The Last Waltz'}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()

        # act
        response = self.client.post(self.url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(MasterAlbum.objects.count(), 0)


class ReleaseViewTests(APITestCase):
    url = reverse('release-list')

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


class TrackViewTests(APITestCase):
    url = reverse('track-list')

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


class RoleViewTests(APITestCase):
    url = reverse('role-list')

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
