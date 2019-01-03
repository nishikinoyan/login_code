from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import os
from io import BytesIO

def random_str():
    all_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz1234567890'
    i = 0
    login_code = ''
    while i < 4:
        login_code = login_code + random.choice(all_str)
        i = i + 1
    return login_code

def random_color():
    return (random.randint(1,255),random.randint(1,255),random.randint(1,255))

def login_code_img():
    image_width = 160
    image_height = 40
    login_code_image = Image.new('RGB',(image_width,image_height),(255,255,255))
    login_code_font = ImageFont.truetype('./font/login_code_font.TTF',32)
    login_code_draw = ImageDraw.Draw(login_code_image)
    for x in range(image_width):
        for y in range(image_height):
            login_code_draw.point((x,y),fill=random_color())

    login_random_code = random_str()

    for write_temp in range(4):
        login_code_draw.text((40 * write_temp + 5, 5),login_random_code[write_temp],font=login_code_font,fill=random_color())

    #login_code_image = login_code_image.filter(ImageFilter.BLUR)  #模糊滤镜
    return login_random_code,login_code_image

if __name__ == '__main__':
    f = BytesIO()
    login_random_code,login_random_image = login_code_img()
    print(login_random_code)
    login_random_image.save(f,'jpeg')
    try:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'test.jpg'),'wb') as o:
            o.write(f.getvalue())

    except Exception as e:
        print(str(e))
