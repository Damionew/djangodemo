"""
视图对象
"""
from django.http import HttpResponse
import base64
import datetime
import ocr.useocr as aa
def hello(request):
    # 相当于Spring中RequestMapping、ResponseBody返回json字符串
    return HttpResponse("Hello world ! ")

def index(request):
    # 相当于Spring中RequestMapping返回页面
    # print(request.GET.get("filename"))
    # return render(request, 'index.html')
    # print(request.body)
    imgBase64 = request.body
    img = base64.b64decode(imgBase64)
    filename = datetime.datetime.now().strftime('%H%M%S')+'.jpg';
    file = open(filename,'wb')
    file.write(img)
    file.close()
    result = str(aa.ocrtest(filename))
    print(result)
    return HttpResponse('图片识别结果：'+result)
