# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/11 2:19
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : CountryFlagCrawler.py.py

import requests
from bs4 import BeautifulSoup
import re
import os
from db_maker import DB_Maker as DB


class CountryFlagCrawler:
    def __init__(self):
        self.url = "http://114.xixik.com/country-flag/"
        self.headers = {
            'Host': "114.xixik.com",
            'Connection': 'keep-alive',
            'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
        }
        self.db = DB()
        self.save_path = 'static/images'

    def check_dir(self):
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

    def get_response(self, url, params=None):
        r = requests.get(url, headers=self.headers, params=params)
        r.encoding = 'gb2312'
        soup = BeautifulSoup(r.text, "lxml")
        return soup

    def down_load_flag(self):
        soup = self.get_response(self.url)
        tds = soup.findAll("div", {"class": "lindBox"})[5].findAll("td")
        for td in tds:
            try:
                picture_url = td.find('img')['src']
                country_name = '%s.gif' % re.sub('\s', '', td.text)
                print("Download %s" % country_name)
                r = requests.get(picture_url)
                with open(os.path.join(self.save_path, country_name), 'wb') as f:
                    f.write(r.content)
            except:
                pass
        # contury_info
        country_list = []
        trs = soup.findAll("div", {"class": "lindBox"})[6].findAll("tr")
        for tr in trs:
            try:
                info = list(map(lambda x: re.sub('\s|,', '', x.text), tr.findAll('td')[1:]))
                if len(info) == 4:
                    # 数据错误补充：
                    print(info)
                    if info[0] == '俄罗斯':
                        country_list.append([info[0], info[1], int(info[2]), 17098246])
                    else:
                        country_list.append([info[0], info[1], int(info[2]), int(info[3])])
            except:
                pass

        sql = "insert into country_flag (country,capital,population,area) values " \
              "(?,?,?,?)"
        for line in sorted(country_list, key=lambda x: x[3], reverse=True):
            self.db.insert(sql, line)


if __name__ == '__main__':
    main = CountryFlagCrawler()
    main.check_dir()
    main.down_load_flag()
