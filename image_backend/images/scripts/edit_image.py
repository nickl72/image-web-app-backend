# This file will process all requests to edit images
import PIL 
from datetime import datetime
from ..models import User, Image as Img


image_path = 'image_db'
def open_image(image):
    return PIL.Image.open(f'{image_path}/{image.path}')

# new_image is a PIL.Image, original_image is a imageField_object
def save_image(new_image, original_image):
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    location = f'{image_path}/{now}.jpg'
    new_image.save(location)
    img = Img(title=original_image.title, path=location, description=original_image.description, edited=True, creator=User.objects.filter(id=2)[0])
    img.save()
    return

# image is a django database imageField object
def brightness(image,value):
    image = open_image(image)
    return
def blur(image, value):
    image = open_image(image)
    return
def color(image, request, r=0, g=0, b=0):
    print(image.title)
    img = open_image(image)
    save_image(img, image)
    print('image: ', image)
    print('r: ', r)
    print('g: ', g)
    print('b: ', b)

