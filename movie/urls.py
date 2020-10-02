from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers
from movie import views

router = routers.DefaultRouter()
router.register(r'movie-turns', views.MovieTurnViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'turns', views.TurnViewSet)
schema_view = get_schema_view(
    openapi.Info(
        title="Movies API",
        default_version='v1',
        description="Movies Services Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
extra_urlpatterns = [
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
api_urlpatters = [
    path('', include(router.urls)),
    path('register', views.UserRegisterView.as_view(),
         name='register-user'),

]

urlpatterns = [
    path('', include(extra_urlpatterns)),
    path('api/v1/', include(api_urlpatters)),
    path('movies-admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
