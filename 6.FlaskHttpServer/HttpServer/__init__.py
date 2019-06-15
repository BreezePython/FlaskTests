# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/15 19:37
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : __init__.py

from flask import Flask, render_template, session, request, redirect, url_for
from .views.account import account as account_blueprint
from .views.home import home as home_blueprint


def HttpServerApp():
    app = Flask(__name__)
    app.register_blueprint(account_blueprint, url_prefix='/manage')
    app.register_blueprint(home_blueprint)
    app.config.from_object('settings.BasicConfig')

    @app.before_request
    def check():
        if (not session.get('user') and not request.path.startswith('/static')
                and request.path != '/manage/login'):
            return redirect(url_for('account.login'))

    @app.template_filter("split_path")
    def split_path(path):
        path_list = path.split('/')
        path_list = [[path_list[i - 1], '/'.join(path_list[:i])] for i in range(1, len(path_list)+1)]
        return path_list

    @app.errorhandler(404)
    def error(error_no):
        return "请使用正确的url访问: /index?"

    return app
