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


class TestDataHelper:
    @classmethod
    def create_user(cls,
                    username='alpharius',
                    email='alpharius@alpha.legion',
                    password='q1234567'):
        return User.objects.create_user(
                username,
                email,
                password
            )

    def create_artist(self):
        user = User.objects.get(pk=1)
        artist = Artist.objects.create(
            name='The Band',
            owner=user
        )
        artist.save()
        return artist

    def create_album(self):
        user = User.objects.get(pk=1)
        artist = self.create_artist()
        album = MasterAlbum.objects.create(
            album_name='The Last Waltz',
            owner=user
        )
        album.artists.add(artist)
        album.save()
        return album

    def create_label(self):
        user = User.objects.get(pk=1)
        label = Label.objects.create(
            name='MGM',
            owner=user
        )
        label.save()
        return label

    def create_release(self):
        user = User.objects.get(pk=1)
        album = self.create_album()
        label = self.create_label()
        release = Release.objects.create(
            master_album=album,
            label=label,
            release_date='1978-04-26',
            owner=user
        )
        release.save()
        return release
