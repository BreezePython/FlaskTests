# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 22:23
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : db_maker.py


import sqlite3
from DBUtils.PooledDB import PooledDB


class DB_Maker:
    def __init__(self):
        self.POOL = PooledDB(
            check_same_thread=False,
            creator=sqlite3,
            maxconnections=10,
            mincached=2,
            maxcached=5,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            database='country.db',
        )
        self.check_db()

    def check_db(self):
        sql = "SELECT name FROM sqlite_master where name=?"
        if not self.fetch_one(sql, ('country_flag',)):
            self.create_table()

    def create_table(self):
        print("create table ...")
        sql = """create table country_flag (
                        [id]            integer PRIMARY KEY autoincrement,
                        [country]         varchar (10),
                        [capital]      varchar (30),
                        [population]      int (10),
                        [area]      int (10)
                    )"""
        self.fetch_one(sql)

    def db_conn(self):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def db_close(conn, cursor):
        cursor.close()
        conn.close()

    def fetch_one(self, sql, args=None):
        conn, cursor = self.db_conn()
        if not args:
            cursor.execute(sql)
        else:
            cursor.execute(sql, args)
        record = cursor.fetchone()
        self.db_close(conn, cursor)
        return record

    def fetch_all(self, sql, args):
        conn, cursor = self.db_conn()
        cursor.execute(sql, args)
        record_list = cursor.fetchall()
        self.db_close(conn, cursor)
        return record_list

    def insert(self, sql, args):
        conn, cursor = self.db_conn()
        row = cursor.execute(sql, args)
        conn.commit()
        self.db_close(conn, cursor)

    def insert(self, sql, args):
        conn, cursor = self.db_conn()
        row = cursor.execute(sql, args)
        conn.commit()
        self.db_close(conn, cursor)
