from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def translit(s):
    rus ={" ":"-","а":"a","б":"b","в":"v","г":"g","д":"d","е":"e",
           "ж":"zh","з":"z","и":"i","й":"y","к":"k","л":"l",
           "м":"m","н":"n","о":"o","п":"p","р":"r","с":"s",
           "т":"t","у":"u","ф":"f","х":"h","ц":"c","ч":"ch",
           "ы":"ii","э":"ie","ю":"iu","я":"ya",
           }

    eng = {"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g",
           "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n",
           "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u",
           "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",
           }

    num = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7",
           "8": "8", "9": "9", "0":"0"
           }

    # num = {str(a): b for (a, b) in zip(range(10), range(10))} через генератор
    # strokaeng="abcdefghijklmnopqrstuvwxyz"
    # eng = {a:a for a in strokaeng} через генератор

    vocab =rus.copy()
    vocab.update(eng)
    vocab.update(num)

    engstr=''
    s=s.lower()
    for i in s:
        if not vocab.get(i)==None:
           engstr+=vocab.get(i)

    return engstr







def gen_slug(s,timeinsug):
    new_slag = slugify(s,allow_unicode=True)
    if timeinsug==True:
        return translit(new_slag) +"-"+str(int(time()))
    else:

        return translit(new_slag)

class Post(models.Model):
        title=models.CharField(max_length=150,db_index=True,verbose_name="Заголовок")
        slug=models.CharField(max_length=150,blank=True,unique=True)
        body=models.TextField(blank=True,db_index=True,verbose_name="Текст статьи")
        date_pub=models.DateTimeField(auto_now_add=True)
        tags=models.ManyToManyField('Tag',blank=True,related_name='posts', verbose_name="Теги")

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse("post_detail_url", kwargs={"slug": self.slug})

        def get_update_url(self):
            return reverse("tag_update_url", kwargs={"slug": self.slug})

        def save(self, *args, **kwargs):
            # if not self.id:
            self.slug = gen_slug(self.title,False)
            super().save(*args, **kwargs)

        class Meta:
          verbose_name="Статья"
          verbose_name_plural = "Статьи"

class Comment(models.Model):

    name_author=models.CharField(max_length=50,blank=None)
    body_comment=models.CharField(max_length=300,blank=None)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comm_date_pub = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_author

class Tag(models.Model):
    title=models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse( "tag_update_url", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        # if not self.id:
        self.slug = gen_slug(self.title,False)
        super().save(*args, **kwargs)