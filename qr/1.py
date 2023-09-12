import qrcode

data1 = 'Don\'t suck'

img1 = qrcode.make(data1)

img1.save(path)
