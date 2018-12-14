# djangodemo
Python - Web 框架

创建视图顺序：

0.settings.py下TEMPLATES-DIRS中新增BASE_DIR+"/templates"

1.在templates目录下新增HTML文件

2.在view.py中定义方法index，相当于Spring中Controller内的public String index(){}的类名

3.在urls.py中定义url(r'^index/', index)，相当于Spring中@RequestMapping("/index")的请求名

url(正则表达式,view.py中的方法)
