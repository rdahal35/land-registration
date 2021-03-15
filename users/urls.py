from django.urls import path, include
from .views import signup, home
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/',  signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home')
]
