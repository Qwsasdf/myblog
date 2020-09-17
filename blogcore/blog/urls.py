from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('post/form/', post_submit,name='post_submit_url'),
    path('', post_list,name='post_lists_url'),
    path('post/del/<str:slug>/',PostDel.as_view(), name='tag_delete_url'),
    path('post/create/',PostCreate.as_view(), name='post_create_url'),
    path('post/update/<str:slug>/',PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/',PostDetail.as_view(), name='post_detail_url'),
    path('tag/',tags_list, name='tags_list_url'),
    path('tag/del/<str:slug>/',TagDel.as_view(), name='tag_delete_url'),
    path('tag/create/',TagCreate.as_view(), name='tag_create_url'),
    path('tag/update/<str:slug>/',TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/',TagDetail.as_view(), name='tag_detail_url'),




]
