from django.shortcuts import render
from blog.forms import TagForm, PostForm

def about_us(request):
    return render(request, 'about.html')

def bs(request):
    form=PostForm()
    return render(request,'bs.html',context={"form":form})