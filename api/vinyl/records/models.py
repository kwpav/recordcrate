from django.db import models


class Record(models.Model):
    owner = models.ForeignKey('auth.User', related_name='records',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=200)
    label = models.CharField(max_length=50)
    release_date = models.DateField()
