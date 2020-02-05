import qrcode
import time
name = time.strftime("%Y%m%d%H%M%S")

for i in name:
    if i in ['-',':','.']:
        i='_'

qr = qrcode.QRCode(
	version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=10,
	border=4,
)

f = open('hello.txt','r')
print(f.read())

data = f.read()
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('./'+(name)+'.png')

