from PIL import Image
import pytesseract
# 上面都是导包，只需要下面这一行就能实现图片文字识别
def ocrtest(filename):
    im = Image.open(filename)  # 用pil打开这个图片
    im = im.convert('L')
    text = pytesseract.image_to_string(im,"chi_sim")
    return text
