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

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Format(models.Model):
    """
    The format of the record,
    i.e. 33rpm. 45rpm, colored vinyl, etc
    """
    description = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='formats',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description


class Person(models.Model):
    """
    A person involved in the creation of an album.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='people',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


class Role(models.Model):
    """
    The role a person played on a release or a track.

    e.g.:
    - Guitarist
    - Vocalist
    - Engineer
    - etc.
    """
    name = models.CharField(max_length=50)
    person = models.ForeignKey(Person, related_name='roles')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='roles',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(self.person, self.name)


class Artist(models.Model):
    """
    The artist who made the album.
    """
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='artists',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Label(models.Model):
    """
    The label that released the album.
    """
    name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='labels',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class MasterAlbum(models.Model):
    """
    The album that all releases are from.
    """
    artists = models.ManyToManyField(
        Artist,
        related_name='albums',
        blank=True
    )
    album_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='masteralbums',
        on_delete=models.CASCADE
    )

    def __str__(self):
        # TODO OPTIMIZE THIS: it will probably cause performance issues...
        artist_names = ', '.join(str(artist) for artist in self.artists.all())
        return '{} - {}'.format(artist_names, self.album_name)


class Release(models.Model):
    """
    The release of an album.
    """
    master_album = models.ForeignKey(
        MasterAlbum,
        related_name='album_releases'
    )
    label = models.ForeignKey(
        Label,
        related_name='label_releases'
    )
    formats = models.ManyToManyField(
        Format,
        blank=True,
        related_name='release_formats'
    )
    roles = models.ManyToManyField(
        Role,
        blank=True,
        related_name='release_roles'
    )
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='releases',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} ({})'.format(
            self.master_album,
            self.release_date[:4]
        )


class Track(models.Model):
    """
    The tracks (songs) on the release.
    """
    release = models.ForeignKey(
        Release,
        related_name='tracks',
        on_delete=models.CASCADE
    )
    side = models.CharField(max_length=2)
    side_order = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    roles = models.ManyToManyField(
        Role,
        blank=True,
        related_name='track_roles'
    )
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='tracks',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('release', 'order')
        ordering = ['order']

    def __str__(self):
        return '{}{}. {}'.format(self.side, self.side_order, self.title)


class Profile(models.Model):
    """
    The user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wanted = models.ManyToManyField(
        Release,
        blank=True,
        related_name='wanted_by')
    collected = models.ManyToManyField(
        Release,
        blank=True,
        related_name='collected_by'
    )

    def __str__(self):
        return self.user.username


# Define signals so our Profile model will be automatically created/updated
# when creating/updating User instances
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a profile when creating a user.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Update a profile when updating a user.
    """
    instance.profile.save()
