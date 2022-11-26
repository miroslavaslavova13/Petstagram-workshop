from django.urls import path, include

from petstagram.accounts.views import LogInView, RegisterView, LogOutView, \
    UserDetailsView, EditUserView, UserDeleteView

urlpatterns = (
    path('login/', LogInView.as_view(), name='login user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout/', LogOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user')
    ])),
)

from .signals import *
