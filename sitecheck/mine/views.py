from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from .temp import *
from .models import Site
from django.core.paginator import Paginator


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
    context = {'page_obj': page_obj}
    return render(request, 'mine/index.html', context)


