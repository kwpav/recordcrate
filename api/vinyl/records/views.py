from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from records.permissions import IsOwnerOrReadOnly
from records.models import Record
from records.serializers import RecordSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('record-list', request=request, format=format),
    })


class RecordViewSet(viewsets.ModelViewSet):
    """
    Provide 'list', 'create', 'retrieve', and 'destroy' actions.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provide 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
