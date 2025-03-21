import psycopg2
import variables
from psycopg2 import Error
from config import Settings
from datetime import datetime
time = datetime.now()

class DataBase:

# state_code ='WAITING' или 'SUCCESS'
    def database_insert(self, state_code ='WAITING', request_dates =  "1111-11-11 11:11:11.111"):
        try:
            connection = psycopg2.connect(dbname=f"mtr_int_{Settings.stand}", user="mtr", password="password",
                                          host="192.168.5.248", port="5432")
            print("Подключение к базе данных установлено")
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO public.message_tracking_info (request_id, request_date, item_id,state_code) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (variables.request_ids, request_dates, variables.item_ids, state_code)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            print(f"Запись успешно добавлена в таблицу message_tracking_info")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с базой данных закрыто")




#Например query_param="where request_id = '88005353535'
    def database_select(self, query_param = None):
        try:
            connection = psycopg2.connect(dbname=f"mtr_int_{Settings.stand}", user="mtr", password="password",
                                          host="192.168.5.248", port="5432")
            print("Подключение к базе данных установлено")
            cursor = connection.cursor()
            cursor.execute(f"select * from public.message_tracking_info {query_param}")
            return cursor.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с базой данных закрыто")


    def database_update(self, sql_query, *args):
        try:
            connection = psycopg2.connect(dbname=f"mtr_int_{Settings.stand}", user="mtr", password="password",
                                          host="192.168.5.248", port="5432")
            print("Подключение к базе данных установлено")
            cursor = connection.cursor()
            postgres_update_query = f"{sql_query}"
            record_to_insert = (args)
            cursor.execute(postgres_update_query, record_to_insert)
            connection.commit()
            print(f"Запись успешно обновлена")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с базой данных закрыто")