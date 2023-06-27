# sqlite3
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# c.execute('INSERT INTO student VALUES (?, ?, ?)', (1, 'John', 20))
# c.execute('INSERT INTO student VALUES (?, ?, ?)', (2, 'Mary', 25))

# conn.commit()

c.execute('SELECT * FROM student')
result = c.fetchall()
print(result)
c.close()

conn.close()
