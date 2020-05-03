from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, routers

from project.login.views import LoginView
from project.cadastro.views import CadastroView
from project.ranking.views import RankingView
from project.meta.views import MetaView
from project.dica.views import DicaView
from project.checking.views import CheckingView
from project.gastos.views import GastosView

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

schema_view = get_schema_view(
   openapi.Info(
      title="MESALVE - APIs",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('cadastro/', CadastroView.as_view()),
    path('ranking/', RankingView.as_view()),
    path('meta/', MetaView.as_view()),
    path('dica/', DicaView.as_view()),
    path('checking/', CheckingView.as_view()),
    path('gastos/', GastosView.as_view()),
]