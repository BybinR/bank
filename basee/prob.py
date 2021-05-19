import sqlite3
import pyglet



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

print('Что делаем: 1:Добавление изображения в базу данных. 2:Удаление изображения из базы данных. 3:Поиск по координатоам в базе данных. 4:Вывод изображения по имени. ')

go_fu=int(input())

if go_fu == 1:
    pic_name = input('Название изображения: ')

    pic_inf = input('Дополнительная информация: ')

    pic_x = input('Введите x координату: ')

    pic_y = input('Введите y координату: ')

    pic_way = input('Поместие фойл в папку pick и укажите полное имя файла: ')

    sql.execute("SELECT name FROM pictures WHERE name ='{pic_name}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO pictures VALUES (?, ?, ?, ?, ?)",(pic_name, pic_inf,pic_x,pic_y,pic_way))
        db.commit()
        window_boss = pyglet.window.Window()
        window_boss.set_minimum_size(640, 480)
      

        pyglet.resource.path = ['./pikc'] 
        pyglet.resource.reindex()

        gamer_image = pyglet.resource.image(pic_way)
        gamer = pyglet.sprite.Sprite(gamer_image, x=0, y=0)
        @window_boss.event

        def on_draw():
                window_boss.clear()
                gamer.draw()
        pyglet.app.run()
        
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
    


if go_fu == 4:
        ima=input('Введите название изображения: ')
        window_boss = pyglet.window.Window()
        window_boss.set_minimum_size(640, 480)
      

        pyglet.resource.path = ['./pikc'] 
        pyglet.resource.reindex()

        gamer_image = pyglet.resource.image(ima)
        gamer = pyglet.sprite.Sprite(gamer_image, x=0, y=0)
        @window_boss.event

        def on_draw():
                window_boss.clear()
                gamer.draw()
        pyglet.app.run()
       
       
       
