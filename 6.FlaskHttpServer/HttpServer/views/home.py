# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/15 19:52
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : home.py

from flask import Blueprint, render_template, current_app, send_from_directory, request, jsonify
import os
import time

home = Blueprint('home', __name__)


class DocumentReader:
    def __init__(self, real_path):
        self.real_path = real_path

    def analysis_dir(self):
        dirs = []
        files = []
        os.chdir(self.real_path)
        for name in sorted(os.listdir('.'), key=lambda x: x.lower()):
            _time = time.strftime("%Y/%m/%d %H:%M", time.localtime(os.path.getctime(name)))
            if os.path.isdir(name):
                dirs.append([name, _time, '文件夹', '-'])
            elif os.path.isfile(name):
                file_type = os.path.splitext(name)[1]
                size = self.get_size(os.path.getsize(name))
                files.append([name, _time, file_type, size])
        return dirs, files

    @staticmethod
    def get_size(size):
        if size < 1024:
            return '%d  B' % size
        elif 1024 <= size < 1024 * 1024:
            return '%.2f KB' % (size / 1024)
        elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
            return '%.2f MB' % (size / (1024 * 1024))
        else:
            return '%.2f GB' % (size / (1024 * 1024 * 1024))


@home.route('/index')
@home.route('/index/<path:path_uri>')
def index(path_uri=''):
    base_dir = current_app.config['BASEDIR']
    real_path = os.path.join(base_dir, path_uri).replace('\\', '/')
    if not os.path.exists(real_path):
        return render_template('index.html', error_info="错误的路径...")
    file_reader = DocumentReader(real_path)
    dirs, files = file_reader.analysis_dir()
    return render_template('index.html', path=path_uri, dirs=dirs, files=files, error_info=None)


@home.route('/download/<filename>')
@home.route('/download/<path:path>/<filename>')
def download(filename, path=None):
    if not path:
        real_path = current_app.config['BASEDIR']
    else:
        real_path = os.path.join(current_app.config['BASEDIR'], path)
    return send_from_directory(real_path, filename, mimetype='application/octet-stream')


@home.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return "is upload file ... "
    else:
        path = request.form.get('upload_path')
        file = request.files['upload_file']
        file_name = file.filename
        base_dir = current_app.config['BASEDIR']
        file.save(os.path.join(base_dir, path, file_name))
        return jsonify({"code": 200, "info": "文件：%s 上传成功" % file_name})


@home.errorhandler(500)
def error(error):
    return render_template('index.html', error_info="错误的路径...")
