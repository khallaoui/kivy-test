import kivy


from kivy.app import App
from kivy.uix.widget import Widget

#App().run()


class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame() 

if __name__ == '__main__':
 PongApp().run()

#=========================================================    

from jnius import autoclass
Hardware = autoclass('org.renpy.android.Hardware')
print 'DPI is', Hardware.getDPI()

 #=========================================================    

class Myapp(App):
    #print("hello")
    pass
#Myapp().run()

#Button:
 #text: ‘Hello Berlin’   

if __name__=='__main__':
    Myapp().run()

