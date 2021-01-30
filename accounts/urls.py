from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)