from PIL import Image
import os.path
import glob
def convertjpg(jpgfile, outdir, width=256, height=256):
    img = Image.open(jpgfile)
    try:
        w,h=img.size
        s=min(h,w)
        sh=(h-s)/2.0
        sw=(w-s)/2.0
        new_img=img.crop((sw,sh,sw+s,sh+s))
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)

for jpgfile in glob.glob(r"C:\\Users\\asus\\Desktop\\test\\*.bmp"):
    convertjpg(jpgfile, "woman")
