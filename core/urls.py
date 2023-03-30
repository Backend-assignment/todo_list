
from django.contrib import admin
from django.urls import path

from api.views import tasks,home,index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', tasks),
    path('home/', home),
    path('index/', index),
]
