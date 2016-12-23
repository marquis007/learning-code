from __future__ import print_function
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
im = Image.open("C:/Users/wang/Pictures/Saved Pictures/test.jpg")
print(im.format, im.size, im.mode)


# im.show()
###在图片的右上角加上数字
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype("C:/windows/fonts/Arial.ttf", size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    num = random.randint(0,99)
    draw.text((width - 50, 0), str(num), font=myfont, fill=fillcolor)
    img.save("result.jpg", "jpeg")

#### 使图片变模糊
# im = Image.open("C:/Users/wang/Pictures/Saved Pictures/test.jpg")
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('C:/Users/wang/Pictures/Saved Pictures/blur.jpg', 'jpeg')
if __name__ == "__main__":
    image = Image.open("C:/Users/wang/Pictures/Saved Pictures/test.jpg")
    add_num(image)

####补充教学网址：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000
