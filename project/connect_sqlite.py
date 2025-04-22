import sqlite3

import psycopg2

# Подключение к базе данных
conn = psycopg2.connect('db.sqlite3')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Выполнение SQL-запроса
cursor.execute("SELECT * FROM db_train_alternative_entry")  # Выполняем запрос
rows = cursor.fetchall()  # Получаем данные
print(rows)  # Печатаем данные.
# Заметьте возвращаться только список значений из базы данных, не объект как в случае с ORM. Это аналогично
# выполнению команды values_list() в Django ORM.


# Закрытие соединения
conn.close()