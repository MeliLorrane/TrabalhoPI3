from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path('api/login/', drf_views.obtain_auth_token, name='api_token_auth'),
    path('api/register/', include('profiles.urls')),  # registro via endpoint customizado opcional
]
