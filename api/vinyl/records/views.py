from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from records.permissions import IsOwnerOrReadOnly
from records.models import Format
from records.models import Person
from records.models import Artist
from records.models import Label
from records.models import MasterAlbum
from records.models import Release
from records.models import Track
from records.models import Role
from records.models import Profile
from records.serializers import FormatSerializer
from records.serializers import PersonSerializer
from records.serializers import LabelSerializer
from records.serializers import TrackSerializer
from records.serializers import MasterAlbumSerializer
from records.serializers import ReleaseSerializer
from records.serializers import ArtistSerializer
from records.serializers import UserSerializer
from records.serializers import RoleSerializer
from records.serializers import ProfileSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'formats': reverse('format-list', request=request, format=format),
        'people': reverse('person-list', request=request, format=format),
        'artists': reverse('artist-list', request=request, format=format),
        'labels': reverse('label-list', request=request, format=format),
        'masteralbums': reverse(
            'masteralbum-list',
            request=request,
            format=format
        ),
        'releases': reverse('release-list', request=request, format=format),
        'tracks': reverse('track-list', request=request, format=format),
        'roles': reverse('role-list', request=request, format=format),
        'profiles': reverse('profile-list', request=request, format=format),
    })


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MasterAlbumViewSet(viewsets.ModelViewSet):
    queryset = MasterAlbum.objects.all()
    serializer_class = MasterAlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
