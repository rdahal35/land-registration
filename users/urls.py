from django.urls import path, include
from .views import signup, home, login
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/',  signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home')
]
