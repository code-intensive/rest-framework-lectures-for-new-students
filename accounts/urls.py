from django.urls import path
from .views import CreateUser, UserList, UpdateUser


app_name = 'accounts'
urlpatterns = [
    path('createuser/', CreateUser.as_view(), name='create-user'),
    path('viewusers/', UserList.as_view(), name='users'),
    path('updateuser/<int:pk>/', UpdateUser.as_view(), name='update-user'),
]
