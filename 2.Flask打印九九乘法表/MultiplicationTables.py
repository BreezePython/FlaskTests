# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 一梦七年诗
# @Date     : 2019/5/24 22:25
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : MultiplicationTables.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
