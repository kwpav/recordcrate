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


class FormatModelTests(APITestCase):
    def test_format_str(self):
        """
        Ensure that the __str__() method returns the description of the format.
        """
        # arrange
        expected_str = "33"
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        format = Format.objects.create(
            description=expected_str,
            owner=user
        )

        # assert
        self.assertEqual(format.__str__(), expected_str)


class PersonModelTests(APITestCase):
    def test_person_str(self):
        """
        Ensure that the __str__() method returns the name of the person.
        """
        # arrange
        expected_str = "Omegon, Alpharius"
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        person = Person.objects.create(
            first_name='Alpharius',
            last_name='Omegon',
            owner=user
        )

        # assert
        self.assertEqual(person.__str__(), expected_str)


# no, not that kind of role model
class RoleModelTests(APITestCase):
    def test_role_str(self):
        """
        Ensure that the __str__() method returns the name of the role.
        """
        # arrange
        expected_str = "Young, Neil - Musician"
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
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
        self.assertEqual(role.__str__(), expected_str)


class ArtistModelTests(APITestCase):
    def test_artist_str(self):
        """
        Ensure that the __str__() method returns the name of the artist.
        """
        # arrange
        expected_str = "The Band"
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        # act
        artist = Artist.objects.create(
            name=expected_str,
            owner=user
        )

        # assert
        self.assertEqual(artist.__str__(), expected_str)


class LabelModelTests(APITestCase):
    def test_label_str(self):
        """
        Ensure that the __str__() method returns the name of the label.
        """
        # arrange
        expected_name = "MGM"
        User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        label = Label.objects.create(
            name=expected_name,
            owner=User.objects.get()
        )

        # assert
        self.assertEqual(label.__str__(), expected_name)


class MasterAlbumModelTests(APITestCase):
    def test_artist_str(self):
        """
        Ensure that the __str__() method returns
        the name of the artist and album.
        """
        # arrange
        expected_str = 'The Band - The Last Waltz'
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        # act
        album = MasterAlbum.objects.create(
            #artists=artist,
            album_name='The Last Waltz',
            owner=user
        )

        # assert
        self.assertEqual(album.__str__(), expected_str)


class ReleaseModelTests(APITestCase):
    def test_release_str(self):
        """
        Ensure that the __str__() method returns
        the name of the artist and album.
        """
        # arrange
        expected_str = 'The Band - The Last Waltz'
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        album = MasterAlbum.objects.create(
            #artists=artist,
            album_name='The Last Waltz',
            owner=user
        )
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
        self.assertEqual(release.__str__(), expected_str)


class TrackModelTests(APITestCase):
    def test_track_str(self):
        """
        Ensure that the __str__() method returns
        order and name of the track.
        """
        # arrange
        expected_str = 'A1. Theme from The Last Waltz'
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        album = MasterAlbum.objects.create(
            #artists=artist,
            album_name='The Last Waltz',
            owner=user
        )
        album.save()
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
        self.assertEqual(track.__str__(), expected_str)


class ProfileModelTests(APITestCase):
    def test_create_user_profile(self):
        """
        Ensure that a profile is created whenever a user is created.
        """
        # act
        User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # assert
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().user.username, 'alpharius')

    def test_update_user_profile(self):
        """
        Ensure that a profile is updated whenever a user is updated.
        """
        # act
        User.objects.create_user(
            'alpharius',
            'iamalpharius@alpha.legion',
            'q1234567'
        )
        profile = Profile.objects.get(pk=1)
        User.objects.filter(username='alpharius').update(username='iamalpharius')
        # profile.username is still alpharius but
        # the username value in the database has changed
        # and needs to be reloaded.
        profile.refresh_from_db()

        # assert
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.user.username, 'iamalpharius')

    def test_profile_str(self):
        # act
        User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # assert
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().__str__(), 'alpharius')
