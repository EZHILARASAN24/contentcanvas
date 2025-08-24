from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from blog.models import Category,Blog
from django.db.models import Q
from blog.forms import RegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    categories=Category.objects.all()
    blog=Blog.objects.all().filter(trending=True,status='Published').order_by('-created_at')
    pposts=Blog.objects.all().filter(trending=False,status='Published').order_by('-created_at')
    context={
        'categories':categories,
        'blog':blog,
        'pposts':pposts
    }
    return render(request,'home.html',context)

def posts_by_category(request,cname):
    categories=Category.objects.all()
    category=Category.objects.get(cname=cname)
    blogs=Blog.objects.all().filter(category=category.id,status='Published')
    context={
        'categories':categories,
        'blogs':blogs,
        'category':category
    }

    return render(request,'posts_by_category.html',context)

def single_blog(request,slug):
    categories=Category.objects.all()
    blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'categories':categories,
        'blog':blog,

    }
    return render(request,'single_blog.html',context)


def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.all().filter(Q (title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')

    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render (request,'search.html',context)

def register(request):
    form=RegisterationForm()
    if request.method=='POST':
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    context={
        'form':form
    }
    return render(request,'register.html',context)


def loginpage(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    context={
        'form':form
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')
