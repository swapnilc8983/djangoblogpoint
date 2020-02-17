
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
   
    # user Login, Logout, Register
    path('register/', views.Register, name= 'register'),
    path('login/', views.Login, name= 'login'),
    path('logout/', views.Logout, name= 'logout'),

    #------- CURD Operations for Blogs ------
    path('blogslist/', views.BlogList, name= 'bloglist'),
    path('create-blog/', views.Createblog, name= 'createblog'),
    path('update/<slug:slug>/', views.Updateblog, name= 'updateblog'),
    path('delete/<slug:slug>/', views.Deleteblog, name= 'deleteblog'),
    
    #------- CURD Operations for Category ------
    path('categorylist/', views.Categorylist, name= 'categorylist'),
    path('create-category/', views.Createcategory, name= 'createcategory'),
    path('category/update/<int:id>/', views.Updatecategory, name= 'updatecategory'),
    # path('category/delete/<int:id>/', views.Deletecategory, name= 'deletecategory'),
    #------- Operations for Enquiry ------
    path('enquiry/' , views.Enquiry, name="enquiry")
]