from django.shortcuts import render, get_object_or_404, redirect
from .forms import *


class ObjDelMixin():
    model = None
    template = None
    template_red = None

    def get (self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return  render(self.request,"blog/confirm_form.html",context={"obj":obj,"template_red":self.template_red})



    def post(self,request, slug):
        obj = self.model.objects.get(slug=slug)
        obj.delete()
        return redirect(self.template_red)


class ObjectDetailMixin:
    model = None
    template = None
    def get(self,request,slug):

        obj = get_object_or_404(self.model,slug__iexact=slug)
        return render(request, self.template,context={self.model.__name__.lower(): obj})


class ObjCreateMixin:
    template = None
    template_red= None
    model_form= None

    def get(self,request):
        form=self.model_form()
        return render(request,self.template, context={"form":form})


    def post(self,request):
        bound_form=self.model_form(request.POST)
        if bound_form.is_valid():
            print(bound_form.cleaned_data)
            new_tag = bound_form.save()

            return redirect(self.template_red)  #Было return redirect(new_tag) и отправляло на tag_detail_url
                                                   #Было return redirect(new_tag) и отправляло на tag_detail_url
                                              # поъоже на коас котрый прописан в url через метод которого
                                              # была вызван post через метод TagDetail.as_view()

        return render(request, self.template,context={"form":bound_form})


class ObjUpdateMixin():
    model:None
    model_form:None
    template:None
    template_red:None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={"form": bound_form, "tag": obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form =self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(self.template_red)


