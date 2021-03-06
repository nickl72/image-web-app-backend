# This file will process all requests to edit images
import PIL 
from PIL import ImageEnhance, ImageFilter
from datetime import datetime
from ..models import User, Image as Img
from numpy import array


image_path = 'image_db'
def open_image(image):
    return PIL.Image.open(f'{image_path}/{image.path}')

# new_image is a PIL.Image, original_image is a imageField_object
def save_image(new_image, original_image, create_record = False):
    if create_record:
        filename = datetime.now().strftime('%Y%m%d%H%M%S')+'.jpeg'
    else:
        filename = f'{original_image.path}'

    location = f'{image_path}/{filename}'
    new_image.save(location)

    if create_record:
        img = Img(title=original_image.title, path=location, description=original_image.description, edited=True, creator=User.objects.filter(id=2)[0])
        img.save()

    new_image.close()
    return

# image is a django database imageField object
def edit_brightness(img, value):
    new_img = ImageEnhance.Brightness(img)
    new_image = new_img.enhance(value)
    return new_image

def edit_blur(img, value):
    new_img = img.filter(ImageFilter.BoxBlur(value))
    return new_img

def adjust_pixel(pixel, adjust):
    if (pixel + adjust < 256) and (pixel + adjust > -1):
        return pixel + adjust
    elif pixel + adjust > 255:
        return 255
    else:
        return 0
    

def color(img, r=0, g=0, b=0):
    data = array(img)
    for row in data:
        for pixel in row:
            pixel[0] = adjust_pixel(pixel[0], r)
            pixel[1] = adjust_pixel(pixel[1], g)
            pixel[2] = adjust_pixel(pixel[2], b)
    new_img = PIL.Image.fromarray(data)
    return new_img
    # save_image(new_img, image)

