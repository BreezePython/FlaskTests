# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/11 3:24
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : CountryFlagFlask.py

from flask import Flask, render_template, g
from db_maker import DB_Maker as DB

app = Flask(__name__)


@app.before_request
def connect():
    g.db = DB()


@app.route('/')
@app.route('/<int:country_id>')
def index(country_id=1):
    result = g.db.fetch_one("select * from country_flag where id=%s" % country_id)
    print(result)
    return render_template("index.html", content=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
