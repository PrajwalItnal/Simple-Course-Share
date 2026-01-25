from django.contrib import admin
from .models import Courses, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Courses)