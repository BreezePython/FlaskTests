# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/2 20:59
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : index.py

from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify

account = Blueprint('account', __name__)


@account.route('/home')
def home():
    return "<h2>欢迎访问系统主页</h2>"


@account.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('account.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'qingfeng' and pwd == 'python':
            session['user'] = user
            return jsonify({"code": 200, "error": ""})
        else:
            return jsonify({"code": 401, "error": "用户名或密码错误"})


@account.route('/logout')
def logout():
    del session['user']
    return redirect(url_for('account.login'))
