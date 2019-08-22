
from django.contrib import admin
from django.urls import path
from notes.views import myLogin, myRegister, myHome, newNote, viewNote, leave


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', myLogin, name = "myLogin"),
    path('register/', myRegister, name = 'myRegister'),
    path("home/", myHome, name = 'myHome'),
    path("newnote/", newNote, name='newNote'),
    path("viewnote/<str:id>", viewNote, name = 'viewNote'),
    path("leave/", leave, name = 'leave'),
    
]





