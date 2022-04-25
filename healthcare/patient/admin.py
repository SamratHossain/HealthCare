from django.contrib import admin
from .models import StudentModel, MarksModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(MarksModel)
