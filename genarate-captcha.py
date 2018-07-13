#coding:utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random,time,os

# 验证码中的字符, 就不用汉字了
number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# 验证码一般都无视大小写；验证码长度4个字符
'''
def random_captcha_text(char_set=number+alphabet+ALPHABET, captcha_size=4):
	captcha_text = []
	for i in range(captcha_size):
		c = random.choice(char_set)
		captcha_text.append(c)
	return captcha_text
'''
def random_captcha_text(char_set=number, captcha_size=4):
    captcha_text = []
    captcha_size = random.randint(4,6)
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

# 生成字符对应的验证码
def gen_captcha_text_and_image():
	image = ImageCaptcha()

	captcha_text = random_captcha_text()
	captcha_text = ''.join(captcha_text)

	captcha = image.generate(captcha_text)

	captcha_image = Image.open(captcha)
	captcha_image = np.array(captcha_image)
	return captcha_text, captcha_image

if __name__ == '__main__':
    # 测试
    #while(1):
    for i in range(100):
        text, image = gen_captcha_text_and_image()
        #print('begin ',time.ctime(),type(image))
        f = plt.figure()
        ax = f.add_subplot(111)
        #ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
        plt.imshow(image)
        plt.axis('off')
        plt.savefig(os.path.join("C:\\Users\\asus\\Desktop\\test","{}".format(text)),bbox_inches = 'tight')
        plt.show()
        #print('end ',time.ctime())
        
        


#转换图片位深度为8，并修改图片格式为bmp
import os
from PIL import Image
import re
ImageFilePath = "C:\\Users\\asus\\Desktop\\test"
currentfiles = os.listdir(ImageFilePath)
filesVector = []
for file_name in currentfiles:
    fullPath = os.path.join(ImageFilePath, file_name)
    if os.path.isdir(fullPath):
        newfiles = getFilesAbsolutelyPath(fullPath)
        filesVector.extend(newfiles)
    else:
        filesVector.append(fullPath)

for filename in filesVector:
    im = Image.open(filename)
    im = im.convert("L")
    #im = im.resize((28,28),Image.ANTIALIAS)
    #im.show()
    file = re.split('\\.',filename)
    name = file[0].split('\\')[-1]
    #file = filename.re.split('\\','.')
    out_image=name+".bmp"
    new_name = "C:\\Users\\asus\\Desktop\\test\\"+out_image
    im.save(new_name)
#删除源图像
[os.remove(filename) for filename in filesVector]

'''
#按比例缩放图片，但不理想
import os  #打开文件时需要
from PIL import Image
import re

Start_path='C:\\Users\\asus\\Desktop\\test\\'
width=28
depth=28
list=os.listdir(Start_path)
#print list
count=0
for pic in list:
    path=Start_path+pic
    print(path)
    im=Image.open(path)
    img_w,img_h=im.size
    out = im.resize((28,28),Image.ANTIALIAS)
    #new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
    #new_path=Start_path+new_pic
    
    out.save(new_path)
""""""""""""""""""
    if img_w>width:
        print(pic)
        print("图片名称为"+pic+"图片被修改")
        h_new=int(width*img_h/img_w)
        w_new=int(width*img_w/img_h)
        count=count+1
        out = im.resize((w_new,h_new),Image.ANTIALIAS)
        new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
        #print new_pic
        new_path=Start_path+new_pic
        out.save(new_path)

    if img_h>depth:
        print(pic)
        print("图片名称为"+pic+"图片被修改")
        w=int(depth*img_w/img_h)
        h=int(depth)
        count=count+1
        out = im.resize((width,depth),Image.ANTIALIAS)
        #out = im.resize((w_new,h_new),Image.ANTIALIAS)
        new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
        #print new_pic
        new_path=Start_path+new_pic
        out.save(new_path)
"""""""""""""""""""""""
print('END')
count=str(count)
print("共有"+count+"张图片尺寸被修改")
'''
