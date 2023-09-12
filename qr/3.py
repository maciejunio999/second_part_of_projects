from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/maciej.antosz/Desktop/priv/proj2/QR/myqrcode1.png')

result = decode(img)

print(result)