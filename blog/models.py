from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cname=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cname
    
Status_choices=[
    ('Draft','Draft'),
    ('Published','Published')
]
    
class Blog(models.Model):
    title=models.CharField(max_length=3000)
    slug=models.SlugField(max_length=3000)
    image=models.ImageField(upload_to='media/images/%y/%m/%d')
    short_description=models.CharField(max_length=2000)
    blog_body=models.CharField(max_length=30000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    trending=models.BooleanField(default=False)
    status=models.CharField(choices=Status_choices,default='Draft')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)