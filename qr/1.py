import qrcode

data1 = 'Don\'t suck'

img1 = qrcode.make(data1)

img1.save('C:/Users/maciej.antosz/Desktop/priv/proj2/QR/myqrcode1.png')