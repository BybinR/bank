import pyglet
window_boss = pyglet.window.Window()
window_boss.set_minimum_size(640, 480)
window_boss.set_maximum_size(900, 600)

pyglet.resource.path = ['./pikc'] 
pyglet.resource.reindex()


gamer_image = pyglet.resource.image( 'ramka.png')

gamer = pyglet.sprite.Sprite(gamer_image, x=20, y=20)

@window_boss.event

def on_draw():
        window_boss.clear()
        gamer.draw()

            
pyglet.app.run()
            
