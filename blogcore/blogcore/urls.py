from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', redirect_blog),
    path('about/', about_us,name='about_us'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),

]
