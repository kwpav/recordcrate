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

from django.conf.urls import url, include
from records import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Record Collection API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'formats', views.FormatViewSet)
router.register(r'people', views.PersonViewSet)
router.register(r'labels', views.LabelViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'masteralbums', views.MasterAlbumViewSet)
router.register(r'releases', views.ReleaseViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'profiles', views.ProfileViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    ))
]
