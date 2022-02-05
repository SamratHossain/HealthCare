from django.contrib import admin
from .models import (Qualification, 
                        Specialist, 
                        Experience,
                        DoctorInfo,
                        Review,
                        Category)

# Register your models here.

admin.site.register(Qualification)
admin.site.register(Specialist)
admin.site.register(Experience)
admin.site.register(DoctorInfo)
admin.site.register(Review)
admin.site.register(Category)
