# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/15 19:42
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : manage.py


from HttpServer import HttpServerApp

app = HttpServerApp()

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
