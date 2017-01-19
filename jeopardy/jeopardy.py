import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM category LIMIT 10")
results = cursor.fetchall()

print("Example categories : ")
for category in results:
    print(category[1])

connection.close()