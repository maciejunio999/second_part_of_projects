# there is an issue and color changing do not work (for now 05.09.23)

import qrcode
 
data = "imnotageek"

qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)

qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
 
img.save('myqrcode2.png')
