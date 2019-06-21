# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/20 22:24
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : app.py

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    number_list = random.sample(list(range(1, 10)), 9)
    return render_template('index.html', num_list=number_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=90)
