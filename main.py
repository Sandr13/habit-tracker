import sqlite3

connect = sqlite3.connect('database/habits.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY,
    habit_name TEXT NOT NULL,
    frequency TEXT NOT NULL)
''')
connect.commit()

# cursor.execute('ALTER TABLE habits ADD COLUMN description TEXT')
# connect.commit()

# cursor.execute('INSERT INTO habits (habit_name, frequency, description) VALUES (?, ?, ?)', ("10 страниц книги", "каждый день", ""))
# connect.commit()
# cursor.execute('ALTER TABLE habits DROP COLUMN frequency')
# connect.commit()

cycle = True
while True:
    if cycle:
        cmd = input("Чтобы добавить новую привычку введите /add <Название> \n"
                "Для просмотра текущих привычек введите /list\n"
                    "Чтобы удалить привычку укажите /remove <ID>\n").split()
    else:
        cmd = input().split()
    cycle = False

    #print(f"Вы ввели: {cmd}")

    connect = sqlite3.connect('database/habits.db')
    cursor = connect.cursor()

    command = cmd[0]
    if command == "/add":
        habit_name = ' '.join(cmd[1:])
        #print(habit_name)
        cursor.execute('INSERT INTO habits (habit_name, description) VALUES (?, ?)', (habit_name, ""))
        connect.commit()
    elif command == "/list":
        cursor.execute('SELECT * FROM habits ORDER BY id ASC')
        result = cursor.fetchall()
        for habit in result:
            print(habit)
    elif command == "/remove":
        habit_id = int(cmd[1])
        cursor.execute('DELETE FROM habits WHERE id = ?', (habit_id,))
        connect.commit()
    elif command == "/exit":
        break
    connect.close()
