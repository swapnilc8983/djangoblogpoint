from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from blogs.models import Blog, Category

class Categoryform(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		widgets = {
            'category': forms.TextInput(
				attrs={'class': 'form-control'}),}

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = '__all__'
		widgets = {
            'title': forms.TextInput(
				attrs={'class': 'form-control'}),

            'content': forms.Textarea(
				attrs={'class': 'form-control'}),

			'description': forms.TextInput(
				attrs={'class': 'form-control'}),

			'slug': forms.TextInput(
				attrs={'class': 'form-control'}),
			
			# 'category': forms.Select(
			# 	attrs={'class' : 'dropdown-menu'})
			}
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'username', 'email', 'password1', 'password2']

