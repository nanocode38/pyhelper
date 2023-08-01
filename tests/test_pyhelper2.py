from pyhelper.pygwidgets import InputText
import sys
import time
from pyhelper.pghelper import *
from pyhelper import*
import pygame



pygame.init()
screen = pygame.display.set_mode((500, 500))

background_path = "D:\\Program Files\\Python311\\Lib\\pyhelper" + \
                  "\\tests\\images\\background.jpg"
s = (
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f1.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f2.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f3.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f4.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f5.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f6.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f7.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f8.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f9.gif',
    r'D:\Programming\Python\资源\Object-Oriented-Python-Code-master\Chapter_14\AnimationExample\images\TRex\f10.gif',
)
images = load_images(s)
animatec = AnimateConfig(screen, images)

animate = Animate(animatec)


while True:
    draw_background(screen, background_path)

    animate.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                animate.play()
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

    animate.draw()
    pygame.display.update()