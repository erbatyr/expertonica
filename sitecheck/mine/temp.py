import pandas as pd
import sqlalchemy


def migrate_from_file_to_db(filepath):
    connection = sqlalchemy.create_engine("sqlite:///C:\\Users\\erbatyr\\PycharmProjects\\Expertonica\\sitecheck\\db.sqlite3")
    data_from_excel = pd.read_excel(filepath, header=0)
    data_from_sql = pd.read_sql_table("mine_site", con=connection, columns=["url", "http_code", "date", "ip_address", "timeout"])
    data_without_duplicates = pd.concat([data_from_sql, data_from_excel]).drop_duplicates(subset=["url"])
    data_without_duplicates.to_sql("mine_site", con=connection, if_exists="replace", index=True, index_label="id")