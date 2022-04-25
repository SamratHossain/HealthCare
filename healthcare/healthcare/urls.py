from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from patient import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student/', views.StudentApi)
router.register('mark/', views.MarksApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/doctors/', include('doctor.urls')),
    path('', include(router.urls)),
    path('api/patient/', include('patient.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
