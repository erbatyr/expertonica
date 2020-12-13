from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file_upload/', views.upload_file, name='file_upload')
]
