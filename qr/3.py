from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(path)

result = decode(img)

print(result)
