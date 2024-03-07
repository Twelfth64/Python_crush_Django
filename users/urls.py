"""urlpatterns for users"""

from django.urls import path, include


app_name='users'
urlpatterns = [
    # Enable URL for authoization by default
    path('', include('django.contrib.auth.urls')),
]
