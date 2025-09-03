import email
import sqlite3

# -- Создание подключения --
connect = sqlite3.connect('database/my_database.db')
cursor = connect.cursor()

# -- CREATE (создание таблицы) --
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    gender TEXT)
''')
connect.commit()

# -- ALTER (изменение) --
# cursor.execute('ALTER TABLE users ADD COLUMN user_group TEXT NOT NULL')
# connect.commit()
# cursor.execute('ALTER TABLE users RENAME TO users_site')
# connect.commit()
# cursor.execute('ALTER TABLE users RENAME COLUMN gender TO gender_user')
# connect.commit()
# cursor.execute('ALTER TABLE users DROP COLUMN user_group')
# connect.commit()

# -- INSERT (вставка данных) --
# cursor.execute('INSERT INTO users (username, email, gender_user) VALUES ("Daria", "mail@mail.ru", "woman")')
# connect.commit()
# cursor.execute('INSERT INTO users (username, email, gender_user) VALUES (?, ?, ?)', ("Mihail", "my_mail@mail.ru", "man"))
# connect.commit()
# users = [
#     ('Anton', 'email1@mail.ru', 'man'),
#     ('Vera', 'email2@mail.ru', 'woman'),
# ]
# cursor.executemany('INSERT INTO users (username, email, gender_user) VALUES (?, ?, ?)', users)
# connect.commit()
# connect.close()

# -- SELECT (вывод данных) --
# cursor.execute('SELECT * FROM users ORDER BY id DESC') # ASC в порядке убывания
# result = cursor.fetchall()
# for user in result:
#     print(f'Имя пользователя: {user[1]} Email пользователя: {user[2]}')
# connect.close()

# email = "email2@mail.ru"
# cursor.execute('SELECT * FROM users WHERE `email` = ?', (email,))
# result = cursor.fetchone()
# print(result)
# connect.close()

# -- UPDATE (обновление данных) --
# new_name = 'Миша'
# cursor.execute('UPDATE users SET username = ? WHERE id = 2', (new_name,))
# connect.commit()

# -- DELETE (удаление данных) --
# id = 2
# cursor.execute('DELETE FROM users WHERE id = ?', (id,))
# connect.commit()
# connect.close()

# -- JOIN (объединение) --
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS sub(
#     id INTEGER PRIMARY KEY,
#     id_user INTEGER,
#     data_sub TEXT)
# ''')
# connect.commit()
#
# cursor.execute('INSERT INTO sub (id_user, data_sub) VALUES (?, ?)', ('1', '20.01.2024'))
# connect.commit()

# cursor.execute('SELECT users.id, users.username, users.email, sub.id AS sub_id, sub.id_user,'
#                'sub.data_sub FROM users INNER JOIN sub ON users.id = sub.id_user')
# print(cursor.fetchone())

# -- CREATE (создание таблицы) --
# cursor.execute('SELECT * FROM users WHERE username LIKE "%A%"')
# print(cursor.fetchall())
# connect.close()
