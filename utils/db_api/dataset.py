import datetime
import threading
from array import array

import pymysql
from pymysql import OperationalError
from pymysql.cursors import DictCursor

# from loader import db
import requests

pymysql_connection = pymysql.connect(
    host='195.161.114.206',
    # port=8889,
    user='j31677409_horosk',
    password='gjnjkjr76',
    db='j31677409_horoskope',
    # charset='utf8mb4',

    # write_timeout=60,
    cursorclass=DictCursor
)


def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop():  # executed in another thread
                while not stopped.wait(interval):  # until stopped
                    function(*args, **kwargs)

                    now = datetime.datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    print("TMRS = =  IM ", dt_string)

            t = threading.Thread(target=loop)
            t.daemon = True  # stop if the program exits
            t.start()
            return stopped

        return wrapper

    return decorator


@setInterval(300)
def pinger():
    print("TMRS = = ")
    pymysql_connection.ping(reconnect=True)


now = datetime.datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("TMRS =  P = ", dt_string)
pinger()


def createUser():
    # try:
    #     with db.cursor() as cursor:
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = """
    CREATE TABLE IF NOT EXISTS Appusers(
    id int AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    tgids int ,
    zodiak varchar (255),
    access int,
    subs int,
    PRIMARY KEY (id)

    );
    """
    pymysql_cursor.execute(sql)
    pymysql_cursor.close()


def add_user(na: str, tg: int, zo: str, ass: int, subs: int):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    # try:
    #     with db.cursor() as cursor:
    sql = "INSERT INTO Appusers (username, tgids, zodiak, access, subs) VALUES ('" + na + "' ,'" + str(
        tg) + " ','" + zo + "', '"+ str(ass) +"','" +str(subs)+"')"
    pymysql_cursor.execute(sql)
    pymysql_connection.commit()
    pymysql_cursor.close()

    # finally:
    #     cursor.close()


def ifUser(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `Appusers` WHERE `tgids`=%s"
    user_id = (id)
    pymysql_cursor.execute(sql, user_id)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    if result is None:
        return False
    else:
        return True


def getSubs():
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `Appusers` WHERE `subs`=%s"
    subsa = 1
    pymysql_cursor.execute(sql, subsa)
    result = pymysql_cursor.fetchall()
    pymysql_cursor.close()
    return result


def getUser(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `Appusers` WHERE `tgids`=%s"
    user_id = (id)
    pymysql_cursor.execute(sql, user_id)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    return result

    # try:
    #     # with db.cursor() as cursor:
    #         sql = "SELECT * FROM `Appusers` WHERE `tgids`=%s"
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchone()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def updateUser(zod: str, ids: int):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "UPDATE `Appusers` SET `zodiak`=%s WHERE tgids=%s "
    pymysql_cursor.execute(sql, args=[zod, ids])
    pymysql_connection.commit()
    pymysql_cursor.close()


def updateSubs(suba: int, ids: int):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "UPDATE `Appusers` SET `subs`=%s WHERE tgids=%s "
    pymysql_cursor.execute(sql, args=[suba, ids])
    pymysql_connection.commit()
    pymysql_cursor.close()


def if_admin(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `Appusers` WHERE `tgids`=%s"
    user_id = (id)
    pymysql_cursor.execute(sql, user_id)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    if result['access'] == 2:
        return True
    else:
        return False
    # try:
    #     with db.cursor() as cursor:
    #
    #         sql = "SELECT * FROM `Appusers` WHERE `tgids`=%s"
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchone()
    #         # if result['access'] == 2:
    #         #     return True
    #         # else:
    #         #     return False
    #
    # finally:
    #     cursor.close()
    #     if result['access'] == 2:
    #         return True
    #     else:
    #         return False


def get_all_users():
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `Appusers`"
    pymysql_cursor.execute(sql)
    result = pymysql_cursor.fetchall()
    pymysql_cursor.close()
    return result
    # try:
    #     with db.cursor() as cursor:
    #         sql = "SELECT * FROM `Appusers`"
    #         cursor.execute(sql)
    #         result = cursor.fetchall()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def get_country():
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `country`"
    pymysql_cursor.execute(sql)
    result = pymysql_cursor.fetchall()
    pymysql_cursor.close()
    return result

    # try:
    #     with db.cursor() as cursor:
    #         sql = "SELECT * FROM `country`"
    #         cursor.execute(sql)
    #         result = cursor.fetchall()
    #
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def get_country_by_ids(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `country` WHERE `id`=%s"
    c_ids = (id)
    pymysql_cursor.execute(sql, c_ids)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    return result
    # try:
    #     with db.cursor() as cursor:
    #         sql = "SELECT * FROM `country` WHERE `id`=%s"
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchone()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def get_country_by_name(name: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `country` WHERE `name`=%s"
    co_name = (name)
    pymysql_cursor.execute(sql, co_name)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    return result
    # try:
    #     with db.cursor() as cursor:
    #         sql = "SELECT * FROM `country` WHERE `name`=%s"
    #         cursor.execute(sql, (name,))
    #         result = cursor.fetchone()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def add_catalogs(cover: str, names: str, urla: str, date: str, cat: int):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "INSERT INTO catalog (covers, name, radio_url, added, cat_id ) VALUES ('" + cover + "' ,'" + names + " ','" + urla + "','" + date + "','" + str(
        cat) + "')"
    pymysql_cursor.execute(sql)
    pymysql_connection.commit()
    pymysql_cursor.close()

    # try:
    #     with db.cursor() as cursor:
    #         sql = "INSERT INTO catalog (covers, name, radio_url, added, cat_id ) VALUES ('" + cover + "' ,'" + names + " ','" + urla + "','" + date + "','" + str(
    #             cat) + "')"
    #         cursor.execute(sql)
    #         db.commit()
    #         # print(cursor)
    #
    # finally:
    #     cursor.close()


def get_catalog(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `catalog` WHERE `cat_id`=%s ORDER BY added DESC"
    cats = (id)
    pymysql_cursor.execute(sql, cats)
    result = pymysql_cursor.fetchall()
    pymysql_cursor.close()
    return result
    # try:
    #     with db.cursor() as cursor:
    #         sql = "SELECT * FROM `catalog` WHERE `cat_id`=%s ORDER BY added DESC"
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchall()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def get_catalog_by_id(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `catalog` WHERE `id`=%s "
    cao = (id)
    pymysql_cursor.execute(sql, cao)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    return result

    # try:
    #     with db.cursor() as cursor:
    #         sql = "SELECT * FROM `catalog` WHERE `id`=%s "
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchone()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def delete_catalog_by_id(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "DELETE  FROM `catalog` WHERE `id`=%s "
    cas = (id)
    pymysql_cursor.execute(sql, cas)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    return result
    # try:
    #     with db.cursor() as cursor:
    #         sql = "DELETE  FROM `catalog` WHERE `id`=%s "
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchone()
    #         # return result
    #
    # finally:
    #     cursor.close()
    #     return result


def get_pages(id: str):
    PARAMS = {'id': id}
    photos = []
    print("PRAM = ", id)

    x = requests.get('https://cp.oriflames.ml/api/catalog/getitem?X-API-KEY=aza', PARAMS)
    json = x.json()
    for paje in json:
        photos.append(paje['image'])

    return photos


def user_access(id: str):
    pymysql_cursor = pymysql.cursors.DictCursor(pymysql_connection)
    sql = "SELECT * FROM `Appusers` WHERE `tgids`=%s"
    usa = (id)
    pymysql_cursor.execute(sql, usa)
    result = pymysql_cursor.fetchone()
    pymysql_cursor.close()
    return result
