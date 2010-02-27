# vim:ts=4:sw=4:et
from pyglet import window
from pyglet import clock
from pyglet import font

class Wall(window.Window):
    
    def __init__(self,*args,**kwargs):

        window.Window.__init__(self,*args,**kwargs)

    def main_loop(self):
        
        ft = font.load('Arial',28)
        fps_text = font.Text(ft,y=10)

        while not self.has_exit:
            self.dispatch_events()
            self.clear()
        
            clock.tick()
    
            fps_text.text = ("fps: %d") % (clock.get_fps())
            fps_text.draw()
        
            self.flip()

class Sprite(object):

    def __init__(self,image_file,image_data=None, **kwards):
        self.image_file = image_file
        if (image_data is None):
            self.image = helper.load_image(image_file)
        else:
            self.image = image_data
        self.x = 0
        self.y = 0

if __name__ == "__main__":
    
    w = Wall()
    w.main_loop()
