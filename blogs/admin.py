from django.contrib import admin
from blogs.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','category', 'status', 'Date')

class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name' , 'contact_no', 'service', 'Date')

admin.site.register(Blog, PostAdmin)
admin.site.register(Category)
admin.site.register(Enquiries,EnquiriesAdmin)

# Register your models here.
