from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, routers

from project.login.views import LoginView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view())
]