from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from  django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm






def post_list(request):
    posts=Post.objects.order_by("-date_pub")
    return render(request,'blog/post_list.html',context={"var_for_html_templ": posts})

def tags_list(request):
    tags= Tag.objects.all()
    return render(request, 'blog/tags_list.html',context={"tags":tags})

# def post_detail(request,slug):
#      # post=Post.objects.get("slug"==slug)
#      post = Post.objects.get(slug__iexact = slug)
#      return render(request, 'blog/post_detail.html',context={"post": post})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact = slug)
#     return render(request, 'blog/tags_detail.html', context={"tag": tag})

# Поменяли методы на классы классы наследовали от еще одного класаа

class PostDetail(ObjectDetailMixin,View):
   model = Post
   template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tags_detail.html'
    template_red = 'tags_list_url'

class PostCreate(ObjCreateMixin,View):
    model_form = PostForm
    template = 'blog/post_create.html'
    template_red = 'post_lists_url'

class TagCreate(ObjCreateMixin,View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    template_red = 'tags_list_url'

class  TagUpdate(ObjUpdateMixin,View):
    model = Tag
    model_form = TagForm
    template = "blog/tag_update_form.html"
    template_red = "tags_list_url"

class PostUpdate(ObjUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = "blog/post_update_form.html"
    template_red = "post_lists_url"


class TagDel(ObjDelMixin,View):
    model = Tag
    template = 'blog/tags_list.html'
    template_red = 'tags_list_url'

class PostDel(ObjDelMixin,View):
    model = Post
    template = 'blog/post_list.html'
    template_red = 'post_lists_url'







# def tagdel(request, slug):
#         tag = a = Tag.objects.get(slug=slug)
#         tag.delete()
#         tags = Tag.objects.all()
#         return render(request, 'blog/tags_list.html', context={"tags": tags})

     # def get (self,request,slug):
     #     tag=Tag.objects.get(slug__iexact=slug)
     #     bound_form=TagForm(instance=tag)
     #     return render(request,"blog/tag_update_form.html",context={"form":bound_form,"tag":tag})
     #
     # def post (self,request,slug):
     #     tag=Tag.objects.get(slug__iexact=slug)
     #     bound_form=TagForm(request.POST,instance=tag)
     #     if bound_form.is_valid():
     #         new_tag=bound_form.save()
     #         return redirect("tags_list_url")
     #     return render(request,"blog/tag_update_form.html",context={"form":bound_form,"tag":tag})

###########