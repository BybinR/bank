import sqlite3


db = sqlite3.connect('server.db')

sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS pictures (
 name TEXT, 
 inf TEXT,
 x FLOAT,
 y FLOAT,
 photo FLOAT
)""")

db.commit()

pic_name = input('Название изображения: ')
pic_inf = input('Дополнительная информация: ')

sql.execute("SELECT name From pictures")

if sql.fetchone() is None:
    sql.execute(f"INSERT INTO pictures VALUES (?, ?, ?, ?, ?)",(pic_name, pic_inf,0,0,0))
    db.commit()

    print('Добавлено')
else :
        print('Такая запись уже имеется')

        for value in sql.execute("SELECT * FROM pictures"):
            print(value)