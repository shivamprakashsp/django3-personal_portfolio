from django.shortcuts import render
from portfolio.models import Project
from blog.models import Blogs

# Create your views here.

def home(request):
    projects = Project.objects.all()
    blogs = Blogs.objects.order_by('-blog_date')[:4]

    return render(request,'portfolio/index.html',{'projects':projects,'blogs':blogs})