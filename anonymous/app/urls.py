from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('register/', register, name='register' ),
    path('login/', login, name='login' ),
    path('logout/', logout, name='logout'),
    path('add/<str:username>', addMessage, name='add'),
    path('', home, name='home'),
    path('list/', message_list, name='list')
    
]