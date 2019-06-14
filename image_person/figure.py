import os
from PIL import Image

def file_rename():
  path = 'src/'
  fileList = os.listdir(path)
  count = 0 
  for i in fileList:
    count = count + 1
    try:
      if i.split('.',1)[1] != 'png':
        os.rename(os.path.join('src/'+ i), os.path.join('src/'+ str(count) + '.jpg'))
        im = Image.open(os.path.join('src/'+ str(count) + '.jpg'))
        im.save(os.path.join('src/'+ str(count) + '.png'))
    except IOError:
      print("Error file")
def delete_img(path):
  fileList = os.listdir(path)
  for i in fileList:
    if i.split('.',1)[1] != 'png':
      os.remove(os.path.join('src/'+ i)) 
def file_name():
  path = 'src/'
  fileList = os.listdir(path)
  count = 0 
  for i in fileList:
    os.rename(os.path.join('src/'+ i), os.path.join('src/'+ str(count) + '.png'))
    count = count + 1
#file_rename()
#delete_img('src/')
file_name()