import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON users (email)")

# Заполните её 10 записями:
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) values (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000)) # добавление таблицы

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
users = cursor.execute("SELECT username, id FROM Users WHERE id % 2  != 0")
for user in users.fetchall():
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, user[0]))

# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute("DELETE FROM Users WHERE id % 3 == 1")

# Выбрать все записи, где возраст не равен 60
cursor.execute("SELECT * FROM Users WHERE age!=60")
results = cursor.fetchall()

# Вывести результаты в консоль
for result in results:
    print(f"Имя: {result[1]} | Почта: {result[2]} | Возраст: {result[3]} | Баланс: {result[4]}")

connection.commit()
connection.close()