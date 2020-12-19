from django.urls import path

from . import views

from .views import SiteListViewSet

urlpatterns = [
    path('', views.index, name='index'),
    path('file_upload/', views.upload_file, name='file_upload'),
    path('api/sites/', SiteListViewSet.as_view({'get':'list'}), name='sites_list_api'),
]

