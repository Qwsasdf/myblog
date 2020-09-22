from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', about_us,name='about_us'),
    path('admin/', admin.site.urls),
    path('bs/',bs),
    path('',include('blog.urls')),

]
