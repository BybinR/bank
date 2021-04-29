import sqlite3


db = sqlite3.connect('server.db')

sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS pictures (
 name TEXT, 
 inf TEXT,
 x FLOAT,
 y FLOAT,
 photo TEXT
)""")

db.commit()

print('Что делаем: 1:Добавление изображения в базу данных. 2:Удаление изображения из базы данных. 3:Поиск по координатоам в базе данных')

go_fu=int(input())

if go_fu == 1:
    pic_name = input('Название изображения: ')

    pic_inf = input('Дополнительная информация: ')

    pic_x = input('Введите x координату: ')

    pic_y = input('Введите y координату: ')

    pic_way = input('Укажите путь к изображению: ')

    sql.execute("SELECT name FROM pictures WHERE name ='{pic_name}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO pictures VALUES (?, ?, ?, ?, ?)",(pic_name, pic_inf,pic_x,pic_y,pic_way))
        db.commit()

        print('Добавлено')
    else :
            print('Такая запись уже имеется')

            for value in sql.execute("SELECT * FROM pictures"):
                print(value)


if go_fu ==2 :
    led=input('Введите название изображения, которое необходимо удалить: ' )
    sql.execute("DELETE FROM pictures WHERE name='led'")


if go_fu ==3:
    pox1=int(input('Введите значение x первой координаты: ' ))
    poy1=int(input('Введите значение y первой координаты: ' ))
    pox2=int(input('Введите значение x второй координаты: ' ))
    poy2=int(input('Введите значение y второй координаты: ' ))
