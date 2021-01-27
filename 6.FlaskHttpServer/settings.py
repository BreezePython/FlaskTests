# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/15 21:09
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : settings.py
from datetime import timedelta


class BasicConfig:
    BASEDIR = 'e:'
    SECRET_KEY = "Can't not guess it ."
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
