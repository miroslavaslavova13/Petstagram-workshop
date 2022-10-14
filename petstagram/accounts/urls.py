from django.urls import path, include

from petstagram.accounts.views import user_login, user_register, user_details, user_edit, user_delete

urlpatterns = (
    path('login/', user_login, name='login user'),
    path('register/', user_register, name='register user'),
    path('profile/<int:pk>/', include([
        path('', user_details, name='details user'),
        path('edit/', user_edit, name='edit user'),
        path('delete/', user_delete, name='delete user')
    ])),
)