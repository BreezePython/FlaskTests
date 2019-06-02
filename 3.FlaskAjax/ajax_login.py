# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/2 20:59
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : basic_login.py

from flask import Flask, render_template, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "Can't not guess it ."


@app.before_request
def check():
    if (not session.get('user') and not request.path.startswith('/static')
            and request.path != '/login'):
        return redirect(url_for('login'))


@app.errorhandler(404)
def error(error_no):
    return "您访问的路径不存在..."


@app.route('/home')
def home():
    return "<h2>欢迎访问系统主页</h2>"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('ajax_index.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'qingfeng' and pwd == '123':
            session['user'] = user
            return jsonify({"code": 200, "error": ""})
        else:
            return jsonify({"code": 401, "error": "用户名或密码错误"})


if __name__ == '__main__':
    app.run(debug=True)
