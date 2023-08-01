# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠻⣛⡛⢿⡛⣿⣿⠛⣿⠸⣛⡻⢿⡿⢟⣛⠿⣿⠄⣿⠻⢟⣛⢻⣿⠟⣛⡻⣿⡟⢟⣻⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⢸⣿⣷⢸⣧⡸⠏⣾⣿⢰⣿⡇⢸⡇⢨⣭⣤⣿⠄⣿⢰⣿⣿⡆⡏⢨⣭⣥⣽⡇⣾⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⢸⣭⣵⣾⣿⡇⣼⣿⣿⣼⣿⣧⣼⣷⣮⣭⣽⣿⣤⣿⢰⣯⣥⣾⣿⣦⣭⣭⣿⣧⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

#
# Pyhelper - Packages that provide more helper tools for Python
# Copyright (C) 2023-2024   Gao Yuhan(高宇涵)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# DON'T EVEN HAVE A PERMIT TOO!
#
# Gao Yuhan(高宇涵)
# 2602422835@qq.com
# nanocode38
"""
PgWidgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module provides a number of efficient Pygame GUI components that help you develop Pygame games.
This module has the following classes:
Animate: An animation class based on a series of loaded images
Textbutton-a button created from text; no image can be specified
CustomButton: A button created from an image
CheckBox: A checkbox created from an image
Dragger: An image that you can drag around
Image: An image that can be modified
InputText: An input field for the user to enter
RadioButtons: A set of radio boxes based on checkboxes
All classes ending in Config are configuration classes, which correspond to the first argument of each component class.
All Config classes take screen as their first parameter and also have a property called screen, which is the Suface
of the scene to be drawn
All Config classes have a set_config method that allows you to set a property using the format 'instance.set_config (
property name as a string, value to set)', which will raise a ValueError if it doesn't exist
All components should be created and called in the standard Pygame manner.The basic usage is as follows:
It is first created after setting up all components before the main loop starts
The main loop then starts
Draws the lowest level background image or background color
Start checking for all events.If the component's update method requires an event parameter, it needs to be called
when checking for events.
After checking the event, intervene and execute for the state of all components and be prepared
Then, the update() method is called for the other components to update the screen
Next, the component is drawn by calling the draw() method
Finally, we refresh the screen using pygame.display.update().
See the Pyhelper documentation for detailed usage of all components:
Or a docstring for the corresponding component class"""
from abc import ABC, abstractmethod
import os
import sys
from typing import *

from pyhelper import RGBColor as Color
import pygame


__all__ = [
    'Animate',
    'AnimateConfig',

    'CustomButton',
    'CustomButtonConfig',

    'TextButtonConfig',
    'TextButton',

    'CheckBox',
    'CheckBoxConfig',

    'Dragger',

    'DisplayText',

    'Image',

    'InputText',
    'InputTextConfig',

    'RadioButtons',
    'get_doc'
]

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')

# @!---------------------Config-------------------------------!@#
class BaseConfig(ABC):
    """This is the base class for all configuration classes and is also a private abstract class.
This class should not be accessed, it is not an interface, but an implementation.
So, if you are reading this document, you have violated the client programmer principle!!(╯▔皿▔)╯"""
    __slots__ = ['screen']
    @abstractmethod
    def __init__(self, screen:pygame.Surface):
        self.screen = screen

    def set_config(self, config_name, value):
        """This method is used to configure the individual options"""
        if hasattr(self, config_name):
            setattr(self, config_name, value)
        else:
            raise ValueError(f'The {self.__class__.__name__} did not have attribute \'{config_name}\'')



class AnimateConfig(BaseConfig):
    """This is the configuration class for the Animate class.
This class requires a set of images in addition to the basic screen parameter, as described in the images property
It includes the following configuration options

- images(tuple): This property can be a set of image paths to animate or a set of loaded image objects. If you
need to
animate as a Sprite, use the pghelper.disassemble_sprite_sheet() function
- autostart(bool): This property indicates if the animation will start automatically and defaults to False
- show_first_image_at_end(bool): This property is a Boolean indicating whether to show the first image after the
animation is playing.It defaults to True
- loop(bool): This property is a Boolean indicating whether the animation should loop indefinitely and defaults to
False
- nloop(int): This property specifies how many times the animation should loop and defaults to 1
- duration(int): This property specifies that an image should be toggles every few seconds"""
    __slots__  = ['images', 'autostart', 'show_first_image_at_end',
                  'loop', 'nloop', 'duration']
    def __init__(self, screen, images):
        super().__init__(screen)
        if type(images[0]) == str:
            self.images = load_images(images)
        else:
            self.images = images
        self.autostart = False
        self.show_first_image_at_end = True
        self.loop = False
        self.nloop = 1
        self.duration = 0.1
    
class CustomButtonConfig(BaseConfig):
    """This is the configuration class for the CustomButton class. It includes the following configuration options
In addition to the basic screen parameter, this class also requires the image_paths parameter, as described in
the description of the image_paths property
- image_paths: This is a tuple of paths for all images, which should be passed in "release state, hold state, hover state, lock state". If any of the last three are specified, it is automatically set to the first
- sounds_on_chick: This is the sound effect that was played when the button was clicked and is a string pointing to the sound effect location. The default is None, which means no sound effect will be played.
- command: is what needs to be done when the button is pressed, is of type Function, defaults to None, i.e., does nothing.
- args: This is a tuple containing all the arguments of the command function"""
    __slots__ = ['image_paths', 'sounds_on_chick', 'command', 'args']

    def __init__(self, screen: pygame.Surface, image_paths:Union[tuple, list]):
        super().__init__(screen)
        if type(image_paths) != list:
            image_paths:list = list(image_paths)
        self.image_paths = image_paths
        self.sounds_on_chick = None
        self.command = None
        self.args:tuple = tuple()
        
class TextButtonConfig(BaseConfig):
    """This is the configuration class for the TextButton class. It includes the following configuration options
- width(int): This is a tuple of paths for all images, which should be passed in "release state, hold state,
hover state, lock state". If any of the last three are specified, it is automatically set to the first
- global_coord(tuple): This is a Boolean value that specifies whether the button is in the global coordinate
system. If not, the bx, by property is superimposed at the center of the screen and defaults to False
- sounds_on_chick(str): This is the sound effect that was played when the button was clicked and is a string
pointing to the sound effect location. The default is None, which means no sound effect will be played.
- bx(tuple): The X position of the center of the button. If global_coord is False, the X coordinate is
superimposed at the center of the screen.
- by(tuple): The Y position of the button's center. If global_coord is False, the Y coordinate is superimposed at
the center of the screen.
- command(function): is what needs to be done when the button is pressed, is of type Function, defaults to None,
i.e., does nothing.
- args(tuple): This is a tuple containing all the arguments of the command function."""
    __slots__ = ['width', 'height', 'text_color', 'font', 'text_size',
                  'sounds_on_chick', 'button_color', 'text', 'command',
                 'args']

    def __init__(self, screen:pygame.Surface):
        super().__init__(screen)
        self.width = 180
        self.height = 50
        self.text_color = [Color.White, Color.Gray]
        self.font = None
        self.text_size = 30
        self.sounds_on_chick = None
        self.button_color = [Color.LineGreen, Color.LineGreen, Color.Green,
                    Color.DarkGray]
        self.text = "Hello World!"
        self.command = None
        self.args = tuple()

        
class CheckBoxConfig(BaseConfig):
    """This is the configuration class for the CheckBox class. It includes the following configuration options
- text(str): This is the text to display in the CheeckBox Default is 'CheckBox'.
- font(str): This is the font name for the text property; the default font is used by default
- image_path(str): This attribute is a tuple whose elements are unchecked, checked, locked to checked,
and locked to the image in the checked state
- text_color(tuple): This refers to the text new_color"""
    __slots__ = ['text', 'font', 'image_paths', 'text_color']
    def __init__(self, screen):
        super().__init__(screen)
        self.text = 'CheckBox'
        self.font = None
        self.image_paths = ('CheckBox',)
        self.text_color = Color.White





class InputTextConfig(BaseConfig):
    """This is the configuration class for the CheckBox class. It includes the following configuration options
-loc (tuple): This property indicates the initial top-left position of the text box component.It is represented by a tuple and defaults to (0, 0).
-new_color (tuple): This property represents the background new_color of the text box.It is represented as an RGB tuple and defaults to (0, 0, 0).
-text_color (tuple): This property is the new_color of the text in the text box.It is represented as an RGB tuple and defaults to (2255, 255, 255).
-font (str): This property represents the name of the text font in string format and defaults to None, which is the system default font
-value (str): This property represents the text in the initial state and defaults to.
-width (int): This property is the length of the text box in pixels.It defaults to 250
-font_size (int): This property represents the font size and also determines the height of the text box.It defaults to 30
- focus_color(tuple): This property refers to the new_color of the outer border of the text box while it is selected, defaults to (0, 0, 0).
-init_focus (bool): This property indicates whether the text box gets focus directly when initialized and defaults to False
-mask (str): This property indicates the character in which the input should be rendered in the text field (* if it's a password field).It defaults to None, which means no mask is used
- keep_foucs_on_submit(bool): This property indicates whether to keep focus when the Enter or Return key is pressed in a text box. It defaults to False
-command (function): This is the function you want to call when the Enter or Return key is pressed in the text box.It defaults to None, indicating that no function was called
-args (tuple): This is a tuple representing the arguments of the command"""
    __slots__ = ['loc', 'color', 'text_color', 'font', 'value', 'width',
                 'font_size', 'focus_color', 'init_focus', 'mask',
                 'keep_focus_on_submit', 'command', 'args']
    def __init__(self, screen):
        super().__init__(screen)
        self.loc = (0, 0)
        self.color = Color.White
        self.text_color = Color.Black
        self.font = None
        self.value = ''
        self.width = 250
        self.font_size = 30
        self.command = None
        self.args = tuple
        self.focus_color = Color.Black
        self.init_focus = False
        self.mask = None
        self.keep_focus_on_submit = False


class Animate:
    """An animation class based on a series of loaded images"""
    __slots__ = ['screen', 'images', 'duration', 'rect', '_pause', 'nimage',
                 'elapsed', 'loop', 'nloop', 'start_time', 'playing', 'index',
                 'show_first_image_at_end']
    def __init__(self, ac:AnimateConfig):
        self.screen = ac.screen
        self.images = []
        self.duration = ac.duration
        self.rect = []
        self._pause = False
        self.nimage = 0
        self.elapsed = 0
        for image in ac.images:
            thisimage = image
            thisrect = thisimage.get_rect()
            self.rect.append(thisrect)
            self.images.append(thisimage)
            self.nimage += 1
        self.loop = ac.loop
        self.nloop = ac.nloop
        self.start_time = 0
        self.show_first_image_at_end = ac.show_first_image_at_end
        self.playing = False
        self.index = 0
        if ac.autostart:
            self.play()
            self.update()
            self.draw()

    def play(self):
        """Playing the animate"""
        self.playing = True
        if self._pause:
            self._pause = False
            return
        self.start_time = time.time()
        self.index = 0

    def pause(self):
        """Pause the animate"""
        self._pause = True
    def update(self):
        """Update the animate, Should be called from the main game loop"""
        if not self.playing or self._pause:
            return

        self.elapsed = time.time() - self.start_time
        if self.elapsed > self.duration:
            self.index += 1
            if self.index >= self.nimage:
                self.nloop -= 1
                self.index -= 1
                if self.nloop <= 0 and not self.loop:
                    self.playing = False
                    if self.show_first_image_at_end:
                        self.index = 0
                        self.draw()
            else:
                self.start_time = time.time()

    def draw(self):
        """Draw the animate"""
        self.screen.blit(self.images[self.index], self.rect[self.index])




class CustomButton:
    """An image-based custom button class"""
    __slots__ = ['screen', 'screen_rect', 'text', 'command', 'sounds_on_chick',
                'up_image', 'down_image', 'over_image', 'lock_image',
                'image', 'rect', 'hidden', 'lock', 'args']
    def __init__(self, bs: CustomButtonConfig):
        self.screen = bs.screen
        self.screen_rect = bs.screen.get_rect()
        self.text = ''
        self.command = bs.command
        self.args = bs.args
        self.sounds_on_chick = bs.sounds_on_chick
        self.up_image = bs.image_paths[0]
        try:
            self.down_image = bs.image_paths[1]
        except IndexError:
            self.down_image = bs.image_paths[0]
        try:
            self.over_image = bs.image_paths[2]
        except IndexError:
            self.over_image = bs.image_paths[0]
        try:
            self.lock_image = bs.image_paths[3]
        except IndexError:
            self.lock_image = bs.image_paths[0]
        self.up_image = pygame.image.load(self.up_image)
        self.down_image = pygame.image.load(self.down_image)
        self.over_image = pygame.image.load(self.over_image)
        self.lock_image = pygame.image.load(self.lock_image)
        self.image = self.up_image
        self.rect = self.image.get_rect()
        self.hidden = False
        self.lock = False


    def is_chick(self) -> bool:
        """Return Whether to click"""
        if self.hidden or self.lock:
            return False
        if pygame.mouse.get_pressed()[0] == False:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def is_hover(self) -> bool:
        """Return Whether to hover"""
        if self.hidden or self.lock:
            return False
        if pygame.mouse.get_pressed()[0]:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def update(self):
        """Update the Button"""
        if self.hidden: return
        if self.lock:
            self.image = self.lock_image
        elif self.is_chick():
            self.image = self.down_image
            if self.sounds_on_chick is not None:
                sound = pygame.mixer.Sound(self.sounds_on_chick)
                sound.play()
            if self.command is not None:
                self.command(*self.args)
        elif self.is_hover():
            self.image = self.over_image
        else:
            self.image = self.up_image

    def draw(self):
        """Draw the Button"""
        if self.hidden: return
        self.screen.blit(self.image, self.rect)


class TextButton:
    """A text button created from text"""
    BUTTON_UP = 0
    BUTTON_DOWN = 1
    BUTTON_OVER = 2
    BUTTON_LOCK = 3

    def __init__(self, tbc: TextButtonConfig):
        self.screen = tbc.screen
        self.width, self.height = tbc.width, tbc.height
        self.rect = pygame.Rect(250, 200, self.width, self.height)
        self.sounds_on_chick = tbc.sounds_on_chick
        self.font = pygame.font.SysFont(tbc.font, tbc.text_size)
        self.command = tbc.command
        self.args = tbc.args
        self.text = tbc.text
        self.hidden = False
        self.color = [tbc.button_color[0]]
        try:
            self.color.append(tbc.button_color[1])
        except IndexError:
            self.color.append(tbc.button_color[0])
        try:
            self.color.append(tbc.button_color[2])
        except IndexError:
            self.color.append(tbc.button_color[0])
        try:
            self.color.append(tbc.button_color[3])
        except IndexError:
            self.color.append(tbc.button_color[0])
        self.text_color = [tbc.text_color[0]]
        try:
            self.text_color.append(tbc.text_color[1])
        except IndexError:
            self.text_color.append(tbc.text_color[0])
        try:
            self.text_color.append(tbc.text_color[2])
        except IndexError:
            self.text_color.append(tbc.text_color[0])
        try:
            self.text_color.append(tbc.text_color[3])
        except IndexError:
            self.text_color.append(tbc.text_color[0])

        self.mode = TextButton.BUTTON_UP
        self.lock = False
        self.__is_check = False

    @property
    def is_chick(self):
        return self.__is_check

    def update(self, event) -> bool:
        """Update the Button"""
        if self.hidden: return False
        if self.lock:
            self.mode = TextButton.BUTTON_LOCK
            return False
        elif self.button_is_chick(event):
            self.mode = TextButton.BUTTON_DOWN
            if self.sounds_on_chick is not None:
                sound = pygame.mixer.Sound(self.sounds_on_chick)
                sound.play()
            if self.command is not None:
                self.command(*self.args)
            return True
        elif self.button_is_hover(event):
            self.mode = TextButton.BUTTON_OVER
        else:
            self.mode = TextButton.BUTTON_UP
        return False

    def button_is_chick(self, event):
        """Return Whether to chick"""
        if not event.type == pygame.MOUSEBUTTONDOWN:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def button_is_hover(self, event):
        """Return Whether to hover"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def draw(self):
        """Draw Button"""
        if self.hidden: return
        if self.mode == TextButton.BUTTON_UP:
            pygame.draw.rect(self.screen, self.color[0], self.rect, width=0)
            pygame.draw.line(self.screen, Color.DarkGray, self.rect.bottomleft,
                             self.rect.bottomright, width=4)
            pygame.draw.line(self.screen, Color.DarkGray,
                             self.rect.bottomright, self.rect.topright,
                             width=4)
            msg_image = self.font.render(self.text, True, self.text_color[0])
            msg_rect = msg_image.get_rect()
            msg_rect.center = self.rect.center
            self.screen.blit(msg_image, msg_rect)
        elif self.mode == TextButton.BUTTON_DOWN:
            pygame.draw.rect(self.screen, self.color[1], self.rect, width=0)
            pygame.draw.line(self.screen, Color.DarkGray, self.rect.topleft,
                             self.rect.topright, width=4)
            pygame.draw.line(self.screen, Color.DarkGray, self.rect.bottomleft,
                             self.rect.topleft, width=4)
            msg_image = self.font.render(self.text, True, self.text_color[2])
            msg_rect = msg_image.get_rect()
            msg_rect.centery = self.rect.centery + 3
            msg_rect.centerx = self.rect.centerx + 3
            self.screen.blit(msg_image, msg_rect)
        elif self.mode == TextButton.BUTTON_OVER:
            pygame.draw.rect(self.screen, self.color[2], self.rect, width=0)
            pygame.draw.line(self.screen, Color.DarkGray, self.rect.bottomleft,
                             self.rect.bottomright, width=4)
            pygame.draw.line(self.screen, Color.DarkGray,
                             self.rect.bottomright, self.rect.topright,
                             width=4)
            msg_image = self.font.render(self.text, True, self.text_color[3])
            msg_rect = msg_image.get_rect()
            msg_rect.center = self.rect.center
            self.screen.blit(msg_image, msg_rect)
        else:
            pygame.draw.rect(self.screen, self.color[3], self.rect, width=0)
            pygame.draw.line(self.screen, Color.DarkGray, self.rect.bottomleft,
                             self.rect.bottomright, width=4)
            pygame.draw.line(self.screen, Color.DarkGray,
                             self.rect.bottomright, self.rect.topright,
                             width=4)
            msg_image = self.font.render(self.text, True, self.text_color[1])
            msg_rect = msg_image.get_rect()
            msg_rect.center = self.rect.center
            self.screen.blit(msg_image, msg_rect)


class DisplayText:
    """Display Text on the scene
:param screen(pygame.Suface): The surface of the scene to be drawn
:param font(str): Draws a string representation of the font default: None
:param size(int): The font size
:param text(str): The text
:param new_color(tuple): The text new_color"""
    def __init__(self, screen:pygame.Surface, font=None, size=10, text='', color=(255, 255, 255)):
        pygame.font.init()
        self.screen = screen
        self.font = pygame.font.SysFont(font, size)
        self.text = ''
        self.color = color
        self.set_value(text, color)

    def set_value(self, new_text, new_color=None):
        """Reset the text content and color
        :param new_text(str): new text
        :param new_color(tuple): new Color, default: The original color"""
        if new_color is None:
            new_color = self.color
        if self.text == new_text:
            return
        self.text = new_text
        self.image = self.font.render(self.text, True, new_color)
        self.rect = self.image.get_rect()

    def draw(self):
        """Draw the Text"""
        self.screen.blit(self.image, self.rect)



class CheckBox:
    """A checkbox created based on an image"""
    __slots__ = ['screen', 'text', 'image', 'on_down_image', 'rect','lock',
                 'off_up_image', 'off_down_image',  'is_check', 'on_up_image',
                 'image_rect', 'msg_image', 'msg_rect']
    def __init__(self, cc: CheckBoxConfig):
        self.screen = cc.screen
        self.text = cc.text
        if cc.image_paths[0] == 'CheckBox':
            self.on_up_image = os.path.join(_PYTHON_PATH, 'images',
                                            'CheckBoxOnUp.png')
            self.off_up_image = os.path.join(_PYTHON_PATH, 'images',
                                            'CheckBoxOffUp.png')
            self.on_down_image = os.path.join(_PYTHON_PATH, 'images',
                                            'CheckBoxOnDown.png')
            self.off_down_image = os.path.join(_PYTHON_PATH, 'images',
                                            'CheckBoxOffDown.png')
            self.on_up_image = pygame.image.load(self.on_up_image)
            self.on_down_image = pygame.image.load(self.on_down_image)
            self.off_up_image = pygame.image.load(self.off_up_image)
            self.off_down_image = pygame.image.load(self.off_down_image)

        else:
            self.on_up_image = pygame.image.load(cc.image_paths[0])
            self.on_down_image = pygame.image.load(cc.image_paths[1])
            self.off_up_image = pygame.image.load(cc.image_paths[2])
            self.off_down_image = pygame.image.load(cc.image_paths[3])

        self.lock = False
        self.is_check = False
        self.image_rect = self.on_up_image.get_rect()
        font = pygame.font.SysFont(cc.font, self.image_rect.height - 1)
        self.msg_image = font.render(cc.text, True, cc.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.left = self.image_rect.right + 5
        self.msg_rect.centery = self.image_rect.centery
        self.rect = pygame.Rect(self.image_rect.left, self.image_rect.top,
                                self.msg_rect.right, self.image_rect.bottom)
        self.image = self.on_up_image

    def update(self, event) -> bool:
        """Update the CheckBox"""
        if self.lock and self.is_check:
            self.image = self.off_down_image
        elif self.lock and not self.is_check:
            self.image = self.off_up_image
        elif not self.lock and self.is_check:
            self.image = self.on_down_image
        elif not self.lock and not self.is_check:
            self.image = self.on_up_image
        self.image_rect.topleft = self.rect.topleft
        self.msg_rect.left = self.image_rect.right + 3
        self.msg_rect.centery = self.image_rect.centery


        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.lock:
                self.is_check = not self.is_check
                return True
        return False

    def draw(self):
        """Draw the CheckBox"""
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(self.msg_image, self.msg_rect)


# @!---------------------Dragger--------------------------------!@#

class Dragger:
    """A draggable image component
:param screen (pygame.Surface): The surface of the scene to be drawn
:param images (tuple): A set of image paths or Suface objects representing the states of the component,
where the element images are in order: normal state, pressed state, suspended state, locked state"""
    __slots__ = ['screen', 'text_color', 'font', 'up_image', 'down_image',
                 'over_image', 'lock_image', 'image', 'rect', 'hidden',
                 '__diffx', '__diffy', '__loop', '__is_drag', 'lock',
                 'msg_image', 'msg_image_rect']
    def __init__(self, screen, images):
        self.screen = screen
        self.up_image = images[0]
        try:
            self.down_image = images[1]
        except IndexError:
            self.down_image = images[0]
        try:
            self.over_image = images[2]
        except IndexError:
            self.over_image = images[0]
        try:
            self.lock_image = images[3]
        except IndexError:
            self.lock_image = images[0]
        if not isinstance(self.up_image, pygame.Surface):
            self.up_image = pygame.image.load(self.up_image)
            self.down_image = pygame.image.load(self.down_image)
            self.lock_image = pygame.image.load(self.lock_image)
            self.over_image = pygame.image.load(self.over_image)
        self.image = self.up_image
        self.rect = self.image.get_rect()
        self.__loop = 0
        self.__diffx = 0
        self.__diffy = 0
        self.__is_drag = False
        self.hidden = False
        self.lock = False



    def is_drag(self, event) -> bool:
        """Return Whether to drag"""
        if self.hidden or self.lock:
            return False
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def is_hover(self, event) -> bool:
        """Return Whether to hover"""
        if self.hidden or self.lock:
            return False
        if event == pygame.MOUSEBUTTONDOWN:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False


    def update(self, event):
        """Update Component"""
        if self.hidden: return
        if self.is_drag(event) or self.__is_drag:
            mousex, mousey = pygame.mouse.get_pos()
            if self.__loop == 0:
                self.__diffx = mousex - self.rect.left
                self.__diffy = mousey - self.rect.top
            self.image = self.down_image
            self.__is_drag = True
            self.rect.topleft = (mousex - self.__diffx, mousey - self.__diffy)
            self.__loop += 1
        elif self.is_hover(event):
            self.image = self.over_image
        elif self.lock:
            self.image = self.lock_image
        else:
            self.image = self.up_image
        if not pygame.mouse.get_pressed()[0]:
            self.__is_drag = False
            self.__loop = 0

    def draw(self):
        """Draw Component"""
        if self.hidden:
            return
        self.screen.blit(self.image, self.rect)

class Image:
    """An image that can be modified"""
    __slots__ = ['screen', 'image', 'rect', 'hidden']
    def __init__(self, screen, loc, image_path, rect=None):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        if rect is not None:
            self.rect = rect
        else:  
            self.rect = self.image.get_rect()
            self.rect.topleft = loc
        self.hidden = False

    def flip(self, flip_horizontal:bool=False, flip_vertical:bool=False):
        """Flipping images"""
        self.image = pygame.transform.flip(self.image, flip_horizontal,
                flip_vertical)

    def set_move(self, x=0, y=0):
        """Overlay position"""
        self.rect.centery += y
        self.rect.centerx += x

    def rot_center(self, angle):
        """rotate an image while keeping its center and size"""
        self.image = pygame.transform.rotate(self.image, angle)
        loc = self.rect.topleft
        self.rect = self.image.get_rect()
        self.rect = loc

    def set_position(self, x=0, y=0):
        """move in position"""
        self.rect.center = (x, y)

    def scale(self, x, y):
        """Resizing images"""
        self.image = pygame.transform.scale(self.image, (x, y))
        loc = self.rect.topleft
        self.rect = self.image.get_rect()
        self.rect.topleft = loc

    def get_rect(self):
        return self.rect

    def draw(self):
        if self.hidden: return
        self.screen.blit(self.image, self.rect)


class RadioButtons:
    """Set of radio boxes based on checkboxes
:param screen (pygame.Surface): The surface of the scene to be drawn
:param buttons (List[CheckBox]): A set of CheckBox instances"""
    __slots__ = ['screen', 'buttons', '_last_button']
    def __init__(self, screen :pygame.Surface, buttons:list):
        self.screen = screen
        self.buttons =buttons
        self._last_button = None
    def update(self, event):
        """Update Radio boxes"""
        for button in self.buttons:
            _event = pygame.event.Event(pygame.KEYDOWN)
            button.update(_event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(pygame.mouse.get_pos()) and not button.is_check:
                    button.is_check = True
                    if self._last_button is not None:
                        self._last_button.is_check = False
                    self._last_button = button
                    break

    def get_focus(self):
        """Returns which radio box is selected"""
        for i in range(len(self.buttons)):
            if self.buttons[i].image == self.buttons[i].on_down_image:
                return i
            if self.buttons[i].image == self.buttons[i].off_down_image:
                return i
        return None

    def draw(self):
        """Draw Radio boxes"""
        for button in self.buttons:
            button.draw()




class InputText:
    """An input box for the user to enter"""
    CANCELLED_TAB = -1
    KEY_REPEAT_DELAY = 500  # ms before starting to repeat
    KEY_REPEAT_RATE = 50  # ms between repeating keys

    def __init__(self, itc:InputTextConfig):
        self.__init(itc.screen, itc.loc, itc.value, itc.font, itc.font_size,
                    itc.width, itc.text_color, itc.color, itc.focus_color,
                    itc.init_focus, itc.mask, itc.keep_focus_on_submit, itc)

    def __init(self, window, loc, value, fontName, fontSize, width, textColor,
                backgroundColor, focusColor, initialFocus, mask,
                keep_focus_on_submit, itc):
        """initialization
This method shouldn't be accessed, it's not an interface, it's an implementation.
So if you ARE READING THIS DOCUMENT, you HAVE violated the CLIENT PROGRAMMER PRINCIPLE!!(╯▔皿▔)╯"""


        self.is_enabled = True
        self.hidden = False

        self.screen = window
        self.loc = loc
        self.__text = value
        self.font = pygame.font.SysFont(fontName, fontSize)

        self.command = itc.command
        self.args = itc.args

        self.width = width
        self.__focus = initialFocus
        self.__text_color = textColor
        self.__background_color = backgroundColor
        self.__focus_color = focusColor  # new_color of __focus rectangle around __text
        self.mask = mask
        self.__keep_focus_on_submit = keep_focus_on_submit
        self.__next_field_on_tab = None
        self.key_is_repeating = False
        self.repeating_key = None

        # Get the height of the field by getting the size of the font
        self.height = self.font.get_height()
        # Set the rect of the __text image
        self.image_rect = pygame.Rect(self.loc[0], self.loc[1], self.width,
                                      self.height)
        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.width,
                                self.height)
        # Set the rect of the __focus highlight rectangle (when the __text has been clicked on and has __focus)
        self.__focused_image_rect = pygame.Rect(self.loc[0] - 3, self.loc[1] - 3,
                                                self.width + 6, self.height + 6)

        # Cursor related things:
        self.cursor_surface = pygame.Surface((1, self.height))
        self.cursor_surface.fill(self.__text_color)
        self.cursor_position = len(
            self.__text)  # put the cursor at the end of the initial __text
        self.__cursor_visible = False
        self.__cursor_switch_ms = 500  # Blink every half-second
        self.__cursor_ms_counter = 0
        # this is a list because element 0 will change as the user edits
        self.__cursor_loc = [self.loc[0], self.loc[1]]
        self.clock = pygame.time.Clock()

        # Create one surface, blit the __text into it during _update_image
        # Special flags are needed to set the background alpha as transparent
        self.__text_image = pygame.Surface((self.width, self.height),
                                           flags=pygame.SRCALPHA)

        self._updateImage()  # create the image of the starting __text

    def _updateImage(self):
        """Internal method to render __text as an image.
This method shouldn't be accessed, it's not an interface, it's an implementation.
So if you ARE READING THIS DOCUMENT, you HAVE violated the CLIENT PROGRAMMER PRINCIPLE!!(╯▔皿▔)╯"""
        # Fill the background of the image
        if self.__background_color is not None:
            self.__text_image.fill(self.__background_color)

        # Render the __text as a single line, and blit it onto the __text_image surface
        if self.mask is None:
            lineSurface = self.font.render(self.__text, True, self.__text_color)
        else:
            nChars = len(self.__text)
            maskedText = self.mask * nChars
            lineSurface = self.font.render(maskedText, True, self.__text_color)
        self.__text_image.blit(lineSurface, (0, 0))

    def update(self, event):
        """Update the InputBox"""
        if not self.is_enabled:
            return False
        if self.hidden:
            return False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (
                event.button == 1):  # user clicked
            theX, theY = event.pos

            if self.image_rect.collidepoint(theX, theY):
                if not self.__focus:
                    self.__focus = True  # give this field __focus
                    pygame.key.set_repeat(InputText.KEY_REPEAT_DELAY,
                                          InputText.KEY_REPEAT_RATE)
                else:
                    # Field already has __focus, must position the cursor where the user clicked
                    nPixelsFromLeft = theX - self.loc[0]
                    nChars = len(self.__text)

                    lastCharOffset = self.font.size(self.__text)[0]
                    if nPixelsFromLeft >= lastCharOffset:
                        self.cursor_position = nChars
                    else:
                        for thisCharNum in range(0, nChars):
                            thisCharOffset = \
                            self.font.size(self.__text[:thisCharNum])[0]
                            if thisCharOffset >= nPixelsFromLeft:
                                self.cursor_position = thisCharNum  # Found the proper position for the cursor
                                break
                    self.__cursor_visible = True  # Show the cursor at the click point

            else:
                self.__focus = False
            return False  # means:  handled click, nothing for client to do

        if not self.__focus:  # if this field does not have __focus, don't do anything
            return False

        if event.type == pygame.KEYDOWN:
            currentKey = event.key

            if currentKey in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.__focus = self.__keep_focus_on_submit  # defaults to False - lose __focus with Enter/Return
                if not self.__focus:
                    pygame.key.set_repeat(0)  # turn off repeating characters
                self._updateImage()

                if self.command is not None:
                    self.command(*self.args)

                # User is done typing, return True to signal that __text is available (via a call to get_value)
                return True

            elif currentKey == InputText.CANCELLED_TAB:
                # See code below setting up CANCELLED_TAB
                # If we get a CANCELLED_TAB as the current key, ignore it, already shifted __focus
                pass

            elif currentKey == pygame.K_BACKSPACE:
                self.__text = self.__text[:max(self.cursor_position - 1, 0)] + \
                              self.__text[self.cursor_position:]

                # Subtract one from cursor_pos, but do not go below zero:
                self.cursor_position = max(self.cursor_position - 1, 0)
                self._updateImage()

            elif currentKey == pygame.K_DELETE:  # forward delete key
                self.__text = self.__text[:self.cursor_position] + \
                              self.__text[self.cursor_position + 1:]
                self._updateImage()

            elif currentKey == pygame.K_RIGHT:
                if self.cursor_position < len(self.__text):
                    self.cursor_position = self.cursor_position + 1

            elif currentKey == pygame.K_LEFT:
                if self.cursor_position > 0:
                    self.cursor_position = self.cursor_position - 1

            elif currentKey == pygame.K_END:
                self.cursor_position = len(self.__text)

            elif currentKey == pygame.K_HOME:
                self.cursor_position = 0

            elif currentKey in (pygame.K_UP, pygame.K_DOWN):
                pass

            elif currentKey == pygame.K_TAB:
                if self.__next_field_on_tab is not None:  # Move __focus to a different field
                    self.remove_focus()
                    self.__next_field_on_tab.give_focus()

                    # The TAB key is sent to all fields.  If this field is *before* the field
                    # gaining __focus, we cannot send the TAB to that field
                    # So, we change the key to something that will be ignored when it is
                    # received in the target field
                    event.key = InputText.CANCELLED_TAB

            else:  # standard key
                # If no special key is pressed, add unicode of key to input_string
                unicodeOfKey = event.unicode  # remember for potential repeating key
                self.__text = self.__text[:self.cursor_position] + \
                              unicodeOfKey + \
                              self.__text[self.cursor_position:]
                self.cursor_position = self.cursor_position + len(unicodeOfKey)
                self._updateImage()

        return False  # means: handled key, nothing for client code to do

    def draw(self):
        """Draws the Text in the screen."""
        if self.hidden:
            return

        # If this input __text has __focus, draw an outline around the __text image
        if self.__focus:
            pygame.draw.rect(self.screen, self.__focus_color,
                             self.__focused_image_rect, 1)

        # Blit in the image of __text (set earlier in _update_image)
        self.screen.blit(self.__text_image, self.loc)

        # If this field has __focus, see if it is time to blink the cursor
        if self.__focus:
            self.__cursor_ms_counter = self.__cursor_ms_counter + self.clock.get_time()
            if self.__cursor_ms_counter >= self.__cursor_switch_ms:
                self.__cursor_ms_counter = self.__cursor_ms_counter % self.__cursor_switch_ms
                self.__cursor_visible = not self.__cursor_visible

            if self.__cursor_visible:
                cursorOffset = self.font.size(self.__text[:self.cursor_position])[
                    0]
                if self.cursor_position > 0:  # Try to get between characters
                    cursorOffset = cursorOffset - 1
                if cursorOffset < self.width:  # if the loc is within the __text area, draw it
                    self.__cursor_loc[0] = self.loc[0] + cursorOffset
                    self.screen.blit(self.cursor_surface, self.__cursor_loc)

            self.clock.tick()

    # Helper methods
    def get_value(self):
        """Returns the text entered by the user"""
        return self.__text


    def set_value(self, newText):
        """Sets new __text into the field"""
        self.__text = newText
        self.cursor_position = len(self.__text)
        self._updateImage()

    def is_focus(self) -> bool:
        return self.__focus

    def clear(self, keepFocus=False):
        """Clear the text in the field"""
        self.__text = ''
        self.__focus = keepFocus
        self._updateImage()

    def remove_focus(self):
        self.__focus = False

    def give_focus(self):
        """ Give focus to this field
        Make sure focus is removed from any previous field before calling this
        """
        self.__focus = True

    def set_next_field_on_tab(self, next_field_on_tab):
        self.__next_field_on_tab = next_field_on_tab

    def set_loc(self, loc):
        """set position"""
        self.loc = loc
        self.rect[0] = self.loc[0]
        self.rect[1] = self.loc[1]

        self.image_rect = pygame.Rect(self.loc[0], self.loc[1], self.width,
                                      self.height)
        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.width,
                                self.height)
        # Set the rect of the __focus highlight rectangle (when the __text has been clicked on and has __focus)
        self.__focused_image_rect = pygame.Rect(self.loc[0] - 3, self.loc[1] - 3,
                                                self.width + 6, self.height + 6)
        # this is a list because element 0 will change as the user edits
        self.__cursor_loc = [self.loc[0], self.loc[1]]

def get_doc():
    """Get Doc"""
    import webbrowser
    webbrowser.open(os.path.join(_PYTHON_PATH, 'docs', 'Pyhelper PgWidgets Doc.html'))