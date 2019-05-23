# -*- coding: utf-8 -*-
# @Author  : 王翔
# @JianShu : 一梦七年诗
# @Date    : 2019/5/23 23:56
# Software : PyCharm
# version  ：Python 3.6.8
# @File    : app.py

from flask import Flask, render_template
import datetime

app = Flask(__name__)

_now = datetime.datetime.now()


@app.template_filter("time_filter")
def time_filter(time):
    if not isinstance(time, datetime.datetime):
        return time
    _period = (_now - time).total_seconds()
    if _period < 60:
        return "刚刚"
    elif 60 <= _period < 3600:
        return "%s分钟前" % int(_period / 60)
    elif 3600 <= _period < 86400:
        return "%s小时前" % int(_period / 3600)
    elif 86400 <= _period < 2592000:
        return "%s天前" % int(_period / 86400)
    else:
        return _now.strftime('%Y-%m-%d %H:%M')


@app.route('/')
def index():
    timeList = [
        'abcd',
        _now,
        _now - datetime.timedelta(minutes=5),
        _now - datetime.timedelta(hours=10),
        _now - datetime.timedelta(days=15),
        _now - datetime.timedelta(days=150)
    ]

    return render_template('index.html', timeList=timeList)


if __name__ == '__main__':
    app.run(port=9000)
