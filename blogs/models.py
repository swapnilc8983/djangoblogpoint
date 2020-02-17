from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    category = models.CharField(max_length= 25, unique=True, blank= False)

    def __str__(self):
        return self.category

class Blog(models.Model):
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('Pending', 'Pending')
    )
    # CATEGORY = (
    #     ('Term Insurance', 'Term Insurance'),
    #     ('Health Insurance', 'Health Insurance'),
    #     ('Travel Insurance', 'Travel Insurance'),
    #     ('Car Insurance', 'Car Insurance'),
    #     ('Bike Insurance', 'Bike Insurance'),
    #     ('Investment Plan', 'Investment Plan'),
    #     ('Child Plan','Child Plan')
    #     ('Other Blog','Other Blog') 
    # )
    title = models.CharField(max_length= 100, blank= False )
    description = models.CharField(max_length= 160 , blank= False)
    content = RichTextField()
    slug = models.SlugField(max_length= 100, unique= True, blank= False)
    image = models.ImageField(null= True, blank= True, upload_to= 'images/')
    status = models.CharField(max_length= 15, choices= STATUS, blank= False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category = models.CharField(max_length= 25, choices= CATEGORY, blank= False)
    Date = models.DateField(auto_now= True)
    
    def __str__(self):
        return self.title


class Enquiries(models.Model):
    first_name = models.CharField(max_length= 20, blank=True)
    last_name = models.CharField(max_length= 20, blank=True)
    contact_no = models.CharField(max_length= 20, blank= True)
    service = models.CharField(max_length = 30 , blank=True)
    Date = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name