from django import forms
from .models import Tag, Post, Comment
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    post = forms.CharField(widget=forms.HiddenInput(), label='')
    class Meta:
        model = Comment
        fields = ["name_author","body_comment","post"]
        widgets = {
            'name_author': forms.TextInput(attrs={'class': 'form-control'}),
            'body_comment': forms.Textarea(attrs={'class': 'form-control'}),

        }


class PostForm(forms.ModelForm):
        class Meta:
            model = Post

            fields = ["title","body","tags"]
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'slug': forms.TextInput(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),
                'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }



        def clean_slug(self):  # clean_ соглащение джанго об очистке данныз от sql inJ
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError("Slug not be create ")
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError("Такой slug уже есть ")
            return new_slug

class TagForm(forms.ModelForm):
# Первая реализация а стандартная через
# class TagForm(forms.Form):
#     title=forms.CharField(max_length=50)
#     slug=forms.CharField(max_length=50)
#
#     title.widget.attrs.update({"class":"form-control"})
#     slug.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):                            # clean_ соглащение джанго об очистке данныз от sql inJ
        new_slug=self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError("Slug not be create ")
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Такой slug уже есть ")
        return new_slug


    #  Пример реализации save()
    # def save(self):
    #         new_tag = Tag.objects.create(
    #             title=self.cleaned_data["title"],
    #             slug=self.cleaned_data["slug"]
    #         )
    #         return new_tag