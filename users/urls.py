from django.urls import path
from .views import GuestAPI, UserAPI


user_create = GuestAPI.as_view({
    'get': 'list',
    'post': 'create'
})

user_login =  GuestAPI.as_view({
    'post':'login',
    'get':'list',
})

user_details = UserAPI.as_view({
    'get':'details',
})

user_get_hash = UserAPI.as_view({
    'get': 'get_hash'
})

user_changepass = UserAPI.as_view({
    'post': 'changepass'
})

app_name = 'users'
urlpatterns = [
    path('create/', user_create, name='create'),
    path('login/', user_login, name='login'),
    path('<str:handle>/', user_details, name='details'),
    path('gethash/', user_get_hash, name='get_hash'),
    path('reset/<str:hash>', user_changepass, name='changepass'),
]