import qrcode    
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os

fs = FileSystemStorage()
f = open('hello.txt','r')
print(f.read())
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4, )  
data = f.read() 
qr.add_data(data) 
qr.make(fit=True) 
img = qr.make_image(fill='black', back_color='white') 
fs.save("hey.jpg")