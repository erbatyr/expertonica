from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .temp import *
from .models import Site
from django.core.paginator import Paginator
import requests
from .serializers import SiteSerializer
from rest_framework import viewsets


def upload_file(request):
    if request.method == 'POST' and request.FILES['uploaded_file']:
        uploaded_file = request.FILES['uploaded_file']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(file_name)
        migrate_from_file_to_db(uploaded_file_url)
        return redirect(index)
    return render(request, 'mine/file_upload.html')


def index(request):
    all_table = Site.objects.order_by('url')
    paginator = Paginator(all_table, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    url_from_query = request.GET.get('url')
    if url_from_query is not None:
        site = Site.objects.get(url=url_from_query)
        try:
            start_time = time.time()
            r = requests.get("http://" + site.url)
            end_time = time.time()
            site.timeout = str(end_time - start_time)
            site.http_code = r.status_code
            site.date = datetime.datetime.now()
            site.save()

        except requests.exceptions.ConnectionError:
            print("connection error")

    context = {'page_obj': page_obj}
    return render(request, 'mine/index.html', context)


class SiteListViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer

    def get_queryset(self):
        queryset = Site.objects.all()
        url = self.request.GET.get('url')
        if url is not None:
            queryset = queryset.filter(url=url)
        return queryset