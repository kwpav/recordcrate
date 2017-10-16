from rest_framework import serializers
from records.models import Record
from django.contrib.auth.models import User


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Record
        fields = ('url', 'id', 'owner', 'artist',
                  'album', 'label', 'release_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(many=True,
                                                  view_name='record-detail',
                                                  read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'records')
