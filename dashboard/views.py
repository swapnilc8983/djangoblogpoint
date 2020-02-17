from django.shortcuts import render, redirect
from dashboard.models import *
from blogs.models import *
from dashboard.forms import BlogForm, CreateUserForm, Categoryform
from dashboard.filters import BlogFilter, EnquiryFilter
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url = 'login')
def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    contex = {'form': form}
    return render (request, 'register.html', contex)

def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')  
            password = request.POST.get('password')

            user = authenticate(request, username= username, password=password)  
            if user is not None:
                login(request, user) 
                return redirect('index')
            else:
                messages.info(request, 'Username OR Password Wrong')   
    return render (request, 'login.html')
    
@login_required(login_url = 'login')
def Logout(request):

    logout(request)

    return redirect('login')

@login_required(login_url = 'login')
def index(request):
    # Post Count 
    Publishcount  = Blog.objects.filter(status = 'Publish').count()
    Draftcount  = Blog.objects.filter(status = 'Draft').count()
    Pendingcount  = Blog.objects.filter(status = 'Pending').count()
    totalcount  = Blog.objects.all().count()
    contex = { 
              'Publishcount':Publishcount,
               'Draftcount' : Draftcount,
                'Pendingcount': Pendingcount,
                'totalcount' : totalcount }
    return render (request, 'dashboard.html',contex)


@login_required(login_url = 'login')
def BlogList(request):
    # Query For Database (Blog)
    bloglist = Blog.objects.all().order_by('-id')

    # For Filter
    myFilter = BlogFilter(request.GET, queryset = bloglist)
    bloglist =  myFilter.qs

    paginator = Paginator(bloglist, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    bloglist = paginator.get_page(page_number)

    Publishcount  = Blog.objects.filter(status = 'Publish').count()
    Draftcount  = Blog.objects.filter(status = 'Draft').count()
    Pendingcount  = Blog.objects.filter(status = 'Pending').count()
    totalcount  = Blog.objects.all().count()
    #Contex Data For Render 
    contex = { 
              'Publishcount':Publishcount,
               'Draftcount' : Draftcount,
                'Pendingcount': Pendingcount,
                'totalcount' : totalcount,
                'myFilter' : myFilter,
                'Blogs': bloglist }
    return render (request, 'viewblogs.html', contex )


@login_required(login_url = 'login')
def Createblog(request):
    #  Create Blog Using Form.py 
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('bloglist')    

    contex = {'form': form }

    return render (request, 'create-blog.html', contex )


@login_required(login_url = 'login')
def Updateblog(request, slug):
    # Request To Slug
    blog = Blog.objects.get(slug=slug)
    # set instance for fetch blog data 
    form = BlogForm(instance = blog)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            # return redirect('bloglist')    
    contex = {'form': form, 'blog': blog }

    return render (request, 'update-blog.html', contex )


@login_required(login_url = 'login')
def Deleteblog(request,slug):
    # Delete Blog
    blog = Blog.objects.get(slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('bloglist')
    contex = {'blog': blog}
    return render (request, 'delete-blog.html',contex )

# @login_required(login_url = 'login')
# def list(request):
#     Blog_list = Blog.objects.all()
#     paginator = Paginator(Blog_list, 2) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     # return render(request, 'list.html', {'page_obj': page_obj})

#     return render(request, 'viewblogs.html', { 'Blogs': page_obj })

@login_required(login_url = 'login')
def Categorylist(request):
    categorylist = Category.objects.all().order_by('-id')

    contex = {'categorylist': categorylist}
    return render( request, 'categorylist.html', contex )

@login_required(login_url = 'login')
def Createcategory(request):
    form = Categoryform()
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('categorylist')

    contex= {'form': form}
    return render( request, 'create-category.html', contex )

@login_required(login_url = 'login')
def Updatecategory(request, id):
    category = Category.objects.filter(id = id)[0]
    form = Categoryform(instance = category)
    if request.method == 'POST':
        form = Categoryform(request.POST, instance= category)
        if form.is_valid():
            form.save()
            return redirect ('categorylist')

    contex= {'form': form, 'category': category}
    return render( request, 'update-category.html', contex )

@login_required(login_url = 'login')
def Enquiry(request):
    enquiry = Enquiries.objects.all().order_by('-id')
    
    myFilter = EnquiryFilter(request.GET, queryset = enquiry)
    enquiry =  myFilter.qs

    contex= {'enquiry' : enquiry}
    return render( request, 'enquiry.html', contex )



