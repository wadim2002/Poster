import psycopg2
import json

# Функция по созданию постов
def sql_post_insert(userid,text):
    # подключение к БД
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="pass", host="db", port="5432")
    # создание курсора
    cursor = conn.cursor()
    # строка запроса
    query = "INSERT INTO post (id_user, text) VALUES ('" + str(userid) + "','" + text + "')"
    cursor.execute(query)
    conn.commit()  

    cursor.close()
    conn.close()

    return True

# Функция по получению постов
def sql_post_read(id):
    # подключение к БД
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="pass", host="db", port="5432")
    # создание курсора
    cursor = conn.cursor()
    # строка запроса
    query = "SELECT * FROM post WHERE id_user ='" + str(id) + "'"

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.commit()  

    cursor.close()
    conn.close()

    return json.dumps(rows)