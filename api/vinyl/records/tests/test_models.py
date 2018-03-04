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
from helpers import TestDataHelper


class FormatModelTests(APITestCase):
    def test_format_creation(self):
        # arrange
        expected_str = "33"
        user = TestDataHelper.create_user()
        # act
        format = Format.objects.create(
            description=expected_str,
            owner=user
        )
        # assert
        self.assertTrue(isinstance(format, Format))
        self.assertEqual(format.__str__(), expected_str)


class PersonModelTests(APITestCase):
    def test_person_creation(self):
        # arrange
        expected_str = "Omegon, Alpharius"
        user = TestDataHelper.create_user()
        # act
        person = Person.objects.create(
            first_name='Alpharius',
            last_name='Omegon',
            owner=user
        )
        # assert
        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person.__str__(), expected_str)


# no, not that kind of role model
class RoleModelTests(APITestCase):
    def test_role_creation(self):
        # arrange
        expected_str = "Young, Neil - Musician"
        user = TestDataHelper.create_user()
        person = Person.objects.create(
            first_name='Neil',
            last_name='Young',
            owner=user
        )
        # act
        role = Role.objects.create(
            name='Musician',
            person=person,
            owner=user
        )
        # assert
        self.assertTrue(isinstance(role, Role))
        self.assertEqual(role.__str__(), expected_str)


class ArtistModelTests(APITestCase):
    def test_artist_creation(self):
        # arrange
        expected_str = "The Band"
        user = TestDataHelper.create_user()
        # act
        artist = Artist.objects.create(
            name=expected_str,
            owner=user
        )
        # assert
        self.assertTrue(isinstance(artist, Artist))
        self.assertEqual(artist.__str__(), expected_str)


class LabelModelTests(APITestCase):
    def test_label_creation(self):
        # arrange
        expected_name = "MGM"
        TestDataHelper.create_user()
        # act
        label = Label.objects.create(
            name=expected_name,
            owner=User.objects.get()
        )
        # assert
        self.assertTrue(isinstance(label, Label))
        self.assertEqual(label.__str__(), expected_name)


class MasterAlbumModelTests(APITestCase):
    def test_masteralbum_creation(self):
        # arrange
        expected_str = 'The Band - The Last Waltz'
        user = TestDataHelper.create_user()
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()
        # act
        album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=user
        )
        album.save()
        album.artists.add(artist)
        # assert
        self.assertTrue(isinstance(album, MasterAlbum))
        self.assertEqual(album.__str__(), expected_str)


class ReleaseModelTests(APITestCase):
    def test_release_creation(self):
        # arrange
        expected_str = 'The Band - The Last Waltz (1978-04-26)'
        user = TestDataHelper.create_user()
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()
        album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=user
        )
        album.save()
        album.artists.add(artist)
        label = Label.objects.create(
            name='MGM',
            owner=user
        )
        # act
        release = Release.objects.create(
            master_album=album,
            label=label,
            release_date='1978-04-26',
            owner=user
        )
        # assert
        self.assertTrue(isinstance(release, Release))
        self.assertEqual(release.__str__(), expected_str)


class TrackModelTests(APITestCase):
    def test_track_creation(self):
        # arrange
        expected_str = 'A1. Theme from The Last Waltz'
        user = TestDataHelper.create_user()
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()
        album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=user
        )
        album.save()
        album.artists.add(artist)
        label = Label.objects.create(
            name='MGM',
            owner=user
        )
        release = Release.objects.create(
            master_album=MasterAlbum.objects.get(),
            label=label,
            release_date='1978-04-26',
            owner=user
        )
        release.save()
        # act
        track = Track.objects.create(
            release=Release.objects.get(pk=1),
            side='A',
            side_order=1,
            order=1,
            title='Theme from The Last Waltz',
            duration=218,
            owner=user
        )
        # assert
        self.assertTrue(isinstance(track, Track))
        self.assertEqual(track.__str__(), expected_str)


class ProfileModelTests(APITestCase):
    def test_create_user_profile(self):
        """
        Ensure that a profile is created whenever a user is created.
        """
        # act
        TestDataHelper.create_user()
        # assert
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().user.username, 'alpharius')

    def test_update_user_profile(self):
        """
        Ensure that a profile is updated whenever a user is updated.
        """
        # act
        User.objects.create_user(
            'alpha',
            'iamalpharius@alpha.legion',
            'q1234567'
        )
        profile = Profile.objects.get(pk=1)
        User.objects.filter(username='alpha').update(username='iamalpharius')
        # profile.username is still alpharius but
        # the username value in the database has changed
        # and needs to be reloaded.
        profile.refresh_from_db()
        # assert
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.user.username, 'iamalpharius')

    def test_profile_creation(self):
        # act
        TestDataHelper.create_user()
        # assert
        self.assertEqual(Profile.objects.get().__str__(), 'alpharius')
