from django.shortcuts import render, redirect
from blogs.models import Blog , Enquiries
from dashboard.filters import BlogFilter
from dashboard.forms import BlogForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    blogs = Blog.objects.filter(status = "Publish").order_by('-id')

    paginator = Paginator(blogs, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    
  
    return render (request, 'index.html', { 'bloglist' : blog_list, })

def blog(request , slug):
    blogpage = Blog.objects.filter(slug=slug).first()
    
    #sidebar bloglist
    
    blogs = Blog.objects.filter(status = "Publish", category = blogpage.category).exclude(slug=slug).order_by('-id')[:5]
    
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        contact_no = request.POST.get('cust_mobile')
        service = request.POST.get('services')
        contactform = Enquiries(first_name= first_name , last_name= last_name, contact_no= contact_no, service=service)
        contactform.save()
        messages.info(request, 'Succesfully Submited') 
        # return redirect('/')

    contex = {'sidebarblog': blogs, 'blogpage' : blogpage}
    
    return render (request, 'blogpage.html', contex)

