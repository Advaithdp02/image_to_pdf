from PIL import Image
import os

img_file=os.getcwd()+'/images/'
img_item=os.listdir(img_file)
img_conv=[]
openimage=[]
print('ENTER THE NAME FOR THE PDF ')
name=input()


for i in img_item:
    openimage.append(Image.open(img_file+i))

for i in openimage:
    img_conv.append(i.convert('RGB'))


img_conv[0].save(os.getcwd()+'/{}.pdf'.format(name),save_all=True,append_images=img_conv[1:])

