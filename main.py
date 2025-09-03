import sqlite3
import os
from datetime import datetime

os.makedirs("database", exist_ok=True)
with sqlite3.connect('database/habits.db') as connect:
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY,
        habit_name TEXT NOT NULL,
        description TEXT)
    ''')
    connect.commit()

with sqlite3.connect('database/habits.db') as connect:
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS completions (
        id INTEGER PRIMARY KEY,
        habit_id INTEGER NOT NULL,
        done_date TEXT NOT NULL,
        FOREIGN KEY (habit_id) REFERENCES habits(id))
    ''')
    connect.commit()


# cursor.execute('ALTER TABLE habits ADD COLUMN frequency TEXT NOT NULL')
# connect.commit()

# cursor.execute('INSERT INTO habits (habit_name, frequency, description) VALUES (?, ?, ?)', ("10 страниц книги", "каждый день", ""))
# connect.commit()
# cursor.execute('ALTER TABLE habits DROP COLUMN frequency')
# connect.commit()

cycle = True
while True:
    with sqlite3.connect('database/habits.db') as connect:
        cursor = connect.cursor()

    if cycle:
        cmd = input("Чтобы добавить новую привычку введите /add <Название> \n"
                "Для просмотра текущих привычек введите /list\n"
                    "Чтобы удалить привычку укажите /remove <ID>\n"
                    "Чтобы отметить привычку выполненной /done <ID>\n"
                    "Чтобы посмотреть выполненные привычки /status\n").split()
    else:
        cmd = input().split()
    cycle = False

    #print(f"Вы ввели: {cmd}")
    if not cmd:
        continue
    command = cmd[0]
    if command == "/add":
        if len(cmd) > 1:
            habit_name = ' '.join(cmd[1:])
            #print(habit_name)
            cursor.execute('INSERT INTO habits (habit_name, description) VALUES (?, ?)', (habit_name, ""))
            connect.commit()
        else:
            print("Введите название привычки.")
            continue
    elif command == "/list":
        cursor.execute('SELECT * FROM habits ORDER BY id ASC')
        result = cursor.fetchall()
        for habit in result:
            print(f"{habit[0]}) {habit[1]}")
    elif command == "/remove":
        if len(cmd) < 2:
            print("Укажите ID привычки.")
            continue
        try:
            habit_id = int(cmd[1])
            if cursor.execute('SELECT * FROM habits WHERE id = ?', (habit_id,)).fetchone() is not None:
                cursor.execute('DELETE FROM habits WHERE id = ?', (habit_id,))
                connect.commit()
            else:
                print("Не найдено привычки с указанным ID.")
        except ValueError:
            print("Неверное значение ID.")
    elif command == "/done":
        if len(cmd) < 2:
            print("Укажите ID привычки.")
            continue
        try:
            habit_id = int(cmd[1])
            today = datetime.today()
            exists = cursor.execute('SELECT * FROM completions WHERE habit_id = ? AND done_date = ?',(habit_id, today)).fetchone()
            if exists:
                print(exists)
                print("Сегодня привычка уже сделана.")
            elif cursor.execute('SELECT * FROM habits WHERE id = ?', (habit_id,)).fetchone() is not None:
                cursor.execute('INSERT INTO completions (habit_id, done_date) VALUES (?, ?)', (habit_id, datetime.now().isoformat()))
                connect.commit()
            else:
               print("Не найдено привычки с указанным ID.")
        except ValueError:
            print("Неверное значение ID.")
    elif command == "/exit":
        break
    else:
        print("Неверная команда.")
