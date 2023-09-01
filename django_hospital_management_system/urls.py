from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('doctor_profile/',include('doctor_profile.urls')),
    path('patient_details/',include('patient_details.urls')),
    path('doctors/',include('doctors.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
