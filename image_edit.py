from PIL import Image
img=Image.open(r'C:\Users\dharmesh\Documents\PYTHON\dharmesh.jpg')
MAX_=(250,250)
img.thumbnail(MAX_)
img.save(r'C:\Users\dharmesh\Documents\PYTHON\dog.png')
#img.show()
img2=img
from PIL import ImageEnhance
enhance=ImageEnhance.Sharpness(img2)
enhance.enhance(3).save(r'dharmesh_sharpnes.png')
enhance1=ImageEnhance.Contrast(img2)
enhance1.enhance(0).save(r'dharmesh_contrash.png')
enhance3=ImageEnhance.Brightness(img2)
enhance3.enhance(2).save('dharmesh_brightnes.png')
from PIL import ImageFilter
img4=open(r'C:\Users\dharmesh\Documents\PYTHON\dharmesh.jpg')
img4.filter(ImageFilter.GaussianBlur(radius=4)).save('dharmesh_maupulating_filter.jpg')
