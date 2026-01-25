from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Courses

class CustomSignupForm(UserCreationForm):
    # We add the extra "choice" field here
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('publisher', 'Publisher'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES, 
        widget=forms.RadioSelect, # This makes it a clickable circle (Radio button)
        required=True
    )

    bio = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself...', 'class': 'form-control', 'rows': 3}),
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role' , 'bio')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'description', 'video_url']
        widgets = {
            'title' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Course title'}),
            'description' : forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Course description'}),
            'video_url' : forms.URLInput(attrs = {'class' : 'form-control', 'placeholder' : 'YouTube video link'})
        }