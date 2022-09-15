from django.contrib import admin
from django.urls import path, include
from watchlist_app.views import ListUsers, CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.urls')),
    path('api/users/', ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view())
]
