from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from records.models import Label
from records.models import Format
from records.models import Person
from records.models import Profile


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


class ProfileTests(APITestCase):
    def test_profiles_url(self):
        """
        Ensure that the profile list url is '/profiles/'.
        """
        # arrange
        url = reverse('profile-list')

        # assert
        self.assertEqual(url, '/profiles/')

    def test_get_profiles_ok(self):
        """
        Ensure that GET /profiles/ responds with 200.
        """
        # arrange
        url = reverse('profile-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserTests(APITestCase):
    def test_users_url(self):
        """
        Ensure that the user list url is '/users/'.
        """
        # arrange
        url = reverse('user-list')

        # assert
        self.assertEqual(url, '/users/')

    def test_get_users_ok(self):
        """
        Ensure that GET /users/ responds with 200.
        """
        # arrange
        url = reverse('user-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LabelTests(APITestCase):
    def test_labels_url(self):
        """
        Ensure that the label list url is '/labels/'.
        """
        # arrange
        url = reverse('label-list')

        # assert
        self.assertEqual(url, '/labels/')

    def test_get_labels_ok(self):
        """
        Ensure that GET /labels/ responds with 200.
        """
        # arrange
        url = reverse('label-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_label(self):
        # arrange
        url = reverse('label-list')
        data = {'name': 'MGM'}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Label.objects.count(), 1)
        self.assertEqual(Label.objects.get().name, 'MGM')

    def test_create_empty_label(self):
        # arrange
        url = reverse('label-list')
        data = {'name': ''}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Label.objects.count(), 0)

    def test_create_label_without_logging_in(self):
        # arrange
        url = reverse('label-list')
        data = {'name': 'MGM'}

        # act
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Label.objects.count(), 0)


class FormatTests(APITestCase):
    def test_formats_url(self):
        """
        Ensure that the format list url is '/formats/'.
        """
        # arrange
        url = reverse('format-list')

        # assert
        self.assertEqual(url, '/formats/')

    def test_get_formats_ok(self):
        """
        Ensure that GET /format/ responds with 200.
        """
        # arrange
        url = reverse('format-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_format(self):
        # arrange
        url = reverse('format-list')
        data = {'description': '33'}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Format.objects.count(), 1)
        self.assertEqual(Format.objects.get().description, '33')

    def test_create_empty_format(self):
        # arrange
        url = reverse('format-list')
        data = {'description': ''}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Label.objects.count(), 0)

    def test_create_format_without_logging_in(self):
        # arrange
        url = reverse('format-list')
        data = {'name': '33'}

        # act
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Format.objects.count(), 0)


class PersonTests(APITestCase):
    def test_people_url(self):
        """
        Ensure that the person list url is '/people/'.
        """
        # arrange
        url = reverse('person-list')

        # assert
        self.assertEqual(url, '/people/')

    def test_get_people_ok(self):
        """
        Ensure that GET /people/ responds with 200.
        """
        # arrange
        url = reverse('person-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_person(self):
        """
        Ensure that we can create a person.
        """
        # arrange
        url = reverse('person-list')
        data = {'first_name': 'Levon', 'last_name': 'Helm'}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'Levon')
        self.assertEqual(Person.objects.get().last_name, 'Helm')

    def test_create_empty_person(self):
        # arrange
        url = reverse('format-list')
        data = {'first_name': '', 'last_name': ''}
        user = User.objects.create_user(
            'alpharius',
            'alpharius@alpha.legion',
            'q1234567'
        )

        # act
        self.client.login(username=user.username, password='q1234567')
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Label.objects.count(), 0)

    def test_create_person_without_logging_in(self):
        # arrange
        url = reverse('person-list')
        data = {'first_name': 'Levon', 'last_name': 'Helm'}

        # act
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Person.objects.count(), 0)


class TrackTests(APITestCase):
    def test_tracks_url(self):
        """
        Ensure that the track list url is '/tracks/'.
        """
        # arrange
        url = reverse('track-list')

        # assert
        self.assertEqual(url, '/tracks/')

    def test_get_track(self):
        """
        Ensure that GET /tracks/ responds with 200.
        """
        # arrange
        url = reverse('track-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MasterAlbumTests(APITestCase):
    def test_masteralbums_url(self):
        """
        Ensure that the master album list url is '/masteralbums/'.
        """
        # arrange
        url = reverse('masteralbum-list')

        # assert
        self.assertEqual(url, '/masteralbums/')

    def test_get_masteralbums_ok(self):
        """
        Ensure that GET /masteralbums/ responds with 200.
        """

        # arrange
        url = reverse('masteralbum-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReleaseTests(APITestCase):
    def test_releases_url(self):
        """
        Ensure that the release list url is '/releases/'.
        """
        # arrange
        url = reverse('masteralbum-list')

        # assert
        self.assertEqual(url, '/masteralbums/')

    def test_get_releases_ok(self):
        """
        Ensure that GET /releases/ responds with 200.
        """
        # arrange
        url = reverse('release-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArtistTests(APITestCase):
    def test_artists_url(self):
        """
        Ensure that the artist list url is '/artists/'.
        """
        # arrange
        url = reverse('artist-list')

        # assert
        self.assertEqual(url, '/artists/')

    def test_get_artists_ok(self):
        """
        Ensure that GET /artists/ responds with 200.
        """
        # arrange
        url = reverse('artist-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RoleTests(APITestCase):
    def test_artists_url(self):
        """
        Ensure that the role list url is '/roles/'.
        """
        # arrange
        url = reverse('role-list')

        # assert
        self.assertEqual(url, '/roles/')

    def test_get_roles_ok(self):
        """
        Ensure that GET /roles/ responds with 200.
        """
        # arrange
        url = reverse('role-list')

        # act
        response = self.client.get(url)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
