# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a Test for PyHelper
"""
import os
import webbrowser
import sys

from pyhelper import RGBColor as Color
from pyhelper import _PYTHON_PATH
from pyhelper.pgwidgets import*
from pyhelper.pghelper import *
import pygame

pygame.init()
screen = pygame.display.set_mode((850, 640))

inputtextc = InputTextConfig(screen)
inputtextc.loc = (59, 300)
inputtextc.value = '541881452'

texture = (
    r"D:\Program Files\Python311\Lib\site-packages\pyhelper\images\ButtonUp.png",
    r"D:\Program Files\Python311\Lib\site-packages\pyhelper\images\ButtonDown.png",
    r"D:\Program Files\Python311\Lib\site-packages\pyhelper\images\ButtonOver.png",
    r"D:\Program Files\Python311\Lib\site-packages\pyhelper\images\ButtonLock.png")
buttonc = TextButtonConfig(screen)


check_box_config = CheckBoxConfig(screen)
check_box_config.set_config('text', "This is a Check Box!")
check_box_config1 = CheckBoxConfig(screen)
check_box_config1.text = "This is a Check Box too!"

display = DisplayText(screen, None, 30, "Hello Word!")
display.rect.centery = 400
display.rect.centerx = 400

inputtext = InputText(inputtextc)

button = TextButton(buttonc)

dragger = Dragger(screen, texture)
dragger.rect.topleft  = (350, 10)

check_box = CheckBox(check_box_config)
check_box1 = CheckBox(check_box_config1)
check_box.rect.top += 10
check_box1.rect.top = check_box.rect.top
check_box1.rect.left = check_box.rect.right + 5

logo = Image(screen, (200, 200), "images\\pythonIcon.png")
logo.rect.bottomleft = (50, 600)

radio_button = RadioButtons(screen,[check_box, check_box1])

background_path = "D:\\Program Files\\Python311\\Lib\\pyhelper" + \
                  "\\tests\\images\\background.jpg"


while True:
    draw_background(screen, background_path)

    for event in pygame.event.get():
        radio_button.update(event)
        dragger.update(event)
        inputtext.update(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            from pyhelper import TKhelper
            TKhelper.inputbox("aisf", 'string')
            sys.exit()

        if button.button_is_chick(event) and not dragger.is_drag(event):
            logo.hidden = not logo.hidden

        if inputtext.is_focus():
            continue


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(str(radio_button.get_focus()))
                button.lock = True
            if event.key == pygame.K_RIGHT:
                button.lock = False
                display.set_value("Y", Color.Yellow)
            if event.key == pygame.K_UP:
                check_box.lock = True
            if event.key == pygame.K_DOWN:
                check_box.lock = False

        if not dragger.is_drag(event) and not dragger.is_hover(event):
            button.update(event)
    logo.draw()
    button.draw()
    # check_box.draw()
    # check_box1.draw()
    button.draw()
    dragger.draw()
    radio_button.draw()
    inputtext.draw()
    display.draw()
    pygame.display.update()