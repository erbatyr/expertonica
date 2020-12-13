import pandas as pd
# import sqlite3
import sqlalchemy
import requests
import socket
import datetime
import time


def migrate_from_file_to_db(filepath):
    connection = sqlalchemy.create_engine("sqlite:///C:\\Users\\erbatyr\\PycharmProjects\\Expertonica\\sitecheck\\db.sqlite3")
    data_from_excel = pd.read_excel(filepath, header=0)
    data_from_sql = pd.read_sql_table("mine_site", con=connection)
    data_without_duplicates = pd.concat([data_from_sql, data_from_excel]).drop_duplicates()
    # data_without_duplicates['http_code'] = None
    # data_without_duplicates['date'] = None
    # data_without_duplicates['timeout'] = None
    # data_without_duplicates['ip_address'] = None
    # for i in data_without_duplicates.index:
    #     start_time = time.time()
    #     r = requests.get("https://"+data_without_duplicates.loc[i, "url"])
    #     http_code = r.status_code
    #     date_time = datetime.datetime.now()
    #     end_time = time.time()
    #     timeout = start_time - end_time
    #     data_without_duplicates.loc[i, "http_code"] = http_code
    #     data_without_duplicates.loc[i, 'date'] = date_time
    #     data_without_duplicates.loc[i, 'timeout'] = timeout
    # print(data_without_duplicates.head())
    data_without_duplicates.to_sql("mine_site", con=connection, if_exists="replace", index=False)


# migrate_from_file_to_db("C:\\Users\\erbatyr\\PycharmProjects\\Expertonica\\sitecheck\\mine\\resources\\Website-2020-12-03.xlsx")