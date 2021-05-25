from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginUser, name='Login'),
    path('login/', views.loginUser, name='Login'),
    path('signup/', views.signupUser, name='Sign Up'),
    path('logout/', views.logoutUser, name='Logout')
]