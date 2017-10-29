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

from rest_framework import serializers
from django.contrib.auth.models import User
from records.models import Artist
from records.models import Track
from records.models import Label
from records.models import Format
from records.models import Person
from records.models import MasterAlbum
from records.models import Release
from records.models import Role
from records.models import Profile


class FormatSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Format
        fields = ('url', 'id', 'owner', 'description')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Person
        fields = ('url', 'id', 'owner',
                  'first_name', 'last_name')


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Label
        fields = ('url', 'id', 'owner', 'name')


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Track
        fields = ('url', 'id', 'owner',
                  'order', 'release', 'side', 'side_order',
                  'title', 'duration', 'roles')


class MasterAlbumSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MasterAlbum
        fields = ('url', 'id', 'owner', 'artists', 'album_name')


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # master_album = MasterAlbumSerializer(read_only=True)
    # tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Release
        fields = ('url', 'id', 'owner',
                  'master_album', 'label', 'formats', 'release_date',
                  'tracks', 'roles')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = MasterAlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'id', 'owner', 'name', 'members', 'albums')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Role
        fields = ('url', 'id', 'owner', 'name', 'person')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'id', 'user', 'wanted', 'collected')
