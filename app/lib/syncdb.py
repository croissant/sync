# -*- coding: utf-8 -*-
import os
import sys
import sqlite3

def get_con():
    db_path = "%s/db/test.db" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return sqlite3.connect(db_path)

def get_list(cid):
    con = get_con()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM phrases WHERE cid = ?", (cid,))
    return cursor.fetchall()

if __name__ == '__main__':
    print(get_list())

