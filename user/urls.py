from django.urls import path, include
from django.conf.urls import url

from .views import logout, login, signup

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name="signup"),
]