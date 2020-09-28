from django.shortcuts import render
from blog.forms import TagForm, PostForm
from django.shortcuts import redirect
def about_us(request):
    return render(request, 'about.html')

def redirect_blog(request):
       return redirect('post_lists_url',permanent=True)