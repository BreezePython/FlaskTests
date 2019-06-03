# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/2 20:59
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : index.py

from flask import Flask, render_template, request, session, redirect, url_for
import calendar
from datetime import datetime

calendar.setfirstweekday(firstweekday=6)
app = Flask(__name__)

week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


def calc_calender(date):
    year = date.year
    yearInfo = dict()
    for month in range(1, 13):
        days = calendar.monthcalendar(year, month)
        if len(days) != 6:
            days.append([0 for _ in range(7)])
        month_addr = calendar.month_abbr[month]
        yearInfo[month_addr] = days
    return yearInfo


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        date = datetime.today()
        this_month = calendar.month_abbr[date.month]
        return render_template('index.html', this_month=this_month, date=date, content=calc_calender(date))


if __name__ == '__main__':
    app.run(debug=True)
