from django.shortcuts import render 
from .forms import UploadFileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import qrcode 
from django.core.files.storage import default_storage
import os

def upload_file(request):
    form = UploadFileForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method=="POST":
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        url = fs.url(name)        
        context['url'] = url
        print(name)

        f = default_storage.open(os.path.join( name), 'r')
        print(f.read())
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4, )  
        data = f.read() 
        qr.add_data(data) 
        qr.make(fit=True) 
        img = qr.make_image(fill='black', back_color='white') 
        fs.save(uploaded_file.name,img)
    return render(request,'index.html',context)
