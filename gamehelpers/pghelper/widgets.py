# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#   ___      _  _     _               
#  | _ \_  _| || |___| |_ __  ___ _ _ 
#  |  _/ || | __ / -_) | '_ \/ -_) '_|
#  |_|  \_, |_||_\___|_| .__/\___|_|  
#       |__/           |_|            

#
# Pyhelper - Packages that provide more helper tools for Python
# Copyright (C) 2023-2024   Gao Yuhan(高宇涵)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library Public
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
Finally, we refresh the screen using pghelper.display.update().
See the Pyhelper documentation for detailed usage of all components:
Or a docstring for the corresponding component class
"""
from abc import ABC, abstractmethod
import os
import sys
import time
from typing import *

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
    """
    This is the base class for all configuration classes and is also a private abstract class.
    This class should not be accessed, it is not an interface, but an implementation.
    So, if you are reading this document, you have violated the client programmer principle!!(╯▔皿▔)╯
    """

    @abstractmethod
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def set_config(self, config_name, value):
        """This method is used to configure the individual options"""
        if hasattr(self, config_name):
            setattr(self, config_name, value)
        else:
            raise ValueError(f'The {self.__class__.__name__} did not have attribute \'{config_name}\'')


class AnimateConfig(BaseConfig):
    """
    This is the configuration class for the Animate class.
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
    - duration(int): This property specifies that the image is switched every few seconds
    """

    def __init__(self, screen, images):
        super().__init__(screen)
        if isinstance(images[0], str):
            self.images = load_images(images)
        else:
            self.images = images
        self.autostart = False
        self.show_first_image_at_end = True
        self.loop = False
        self.nloop = 1
        self.duration = 0.1


class CustomButtonConfig(BaseConfig):
    """
    This is the configuration class for the CustomButton class. It includes the following configuration options
    In addition to the basic screen parameter, this class also requires the image_paths parameter, as described in
    the description of the image_paths property
    - image_paths: This is a tuple of paths for all images, which should be passed in "release state, hold state, hover
     state, lock state". If any of the last three are specified, it is automatically set to the first
    - sounds_on_chick: This is the sound effect that was played when the button was clicked and is a string pointing to
     the sound effect location. The default is None, which means no sound effect will be played.
    - command: is what needs to be done when the button is pressed, is of type Function, defaults to None, i.e.,
     does nothing.
    - args: This is a tuple containing all the arguments of the command function
    """

    def __init__(self, screen: pygame.SurfaceType, images: Union[List, Tuple]):
        super().__init__(screen)
        if not isinstance(images, list):
            images = list(images)
        self.text_color: Union[List, Tuple] = [(255, 255, 255), (190, 190, 190)]
        self.text: str = ''
        self.font: Optional[pygame.font.FontType] = None
        self.font_size: int = 20
        self.images: List = images
        self.sounds_on_chick: Optional[pygame.mixer.SoundType] = None
        self.command: Optional[Callable] = None
        self.args: Tuple = tuple()


class TextButtonConfig(BaseConfig):
    """
    This is the configuration class for the TextButton class. It includes the following configuration options
    - width (int): The length of the button
    - height (int): The height of the button
    - text (str): The text on the button
    - button_color(list): A list of button colors whose four elements represent the colors of the following states:
     normal, pressed, suspended, and locked
    - text_color (list): This is a list of button text colors, with four elements representing the colors of the
    following states: normal, pressed, suspended, locked
    - font (str): String representation of the text font
    - text_size (int): The size of the text

    - sounds_on_chick(str): This is the sound effect that was played when the button was clicked and is a string
    pointing to the sound effect location. The default is None, which means no sound effect will be played.

    the center of the screen.
    - command(function): is what needs to be done when the button is pressed, is of type Function, defaults to None,
    i.e., does nothing.
    - args(tuple): This is a tuple containing all the arguments of the command function.
    """

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.width = 180
        self.height = 50
        self.text_color = [(255, 255, 255), (190, 190, 190)]
        self.font = None
        self.text_size = 20
        self.sounds_on_chick = None
        self.button_color = [(50, 205, 50), (50, 205, 50), (0, 255, 0),
                             (169, 169, 169)]
        self.text = "Hello World!"
        self.command = None
        self.args = tuple()


class CheckBoxConfig(BaseConfig):
    """
    This is the configuration class for the CheckBox class. It includes the following configuration options
    - text(str): This is the text to display in the CheeckBox Default is 'CheckBox'.
    - font(str): This is the font name for the text property; the default font is used by default
    - image_path(str): This attribute is a tuple whose elements are unchecked, checked, locked to checked,
    and locked to the image in the checked state
    - text_color(tuple): This refers to the text new_color
    """

    def __init__(self, screen):
        super().__init__(screen)
        self.text = 'CheckBox'
        self.font = None
        self.image_paths = ('CheckBox',)
        self.text_color = (255, 255, 255)


class InputTextConfig(BaseConfig):
    """
    This is the configuration class for the CheckBox class. It includes the following configuration options
    -loc (tuple): This property indicates the initial top-left position of the text box component.It is represented by
     a tuple and defaults to (0, 0).
    -new_color (tuple): This property represents the background new_color of the text box.It is represented as an RGB
     tuple and defaults to (0, 0, 0).
    -text_color (tuple): This property is the new_color of the text in the text box.It is represented as an RGB tuple
     and defaults to (2255, 255, 255).
    -font (str): This property represents the name of the text font in string format and defaults to None, which is the
     system default font
    -value (str): This property represents the text in the initial state and defaults to.
    -width (int): This property is the length of the text box in pixels.It defaults to 250
    -font_size (int): This property represents the font size and also determines the height of the text box.It defaults
     to 30
    - focus_color(tuple): This property refers to the new_color of the outer border of the text box while it is
     selected, defaults to (0, 0, 0).
    -init_focus (bool): This property indicates whether the text box gets focus directly when initialized and defaults
     to False
    -mask (str): This property indicates the character in which the input should be rendered in the text field
     (* if it's a password field).It defaults to None, which means no mask is used
    - keep_foucs_on_submit(bool): This property indicates whether to keep focus when the Enter or Return key is pressed
     in a text box. It defaults to False
    -command (function): This is the function you want to call when the Enter or Return key is pressed in the text box.
     It defaults to None, indicating that no function was called
    -args (tuple): This is a tuple representing the arguments of the command
    """

    def __init__(self, screen):
        super().__init__(screen)
        self.loc = (0, 0)
        self.color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = None
        self.value = ''
        self.width = 250
        self.font_size = 30
        self.command = None
        self.args = tuple
        self.focus_color = (0, 0, 0)
        self.init_focus = False
        self.mask = None
        self.keep_focus_on_submit = False


class Animate:
    """An animation class based on a series of loaded images"""

    def __init__(self, ac: AnimateConfig):
        self.screen = ac.screen
        self.images = []
        self.duration = ac.duration
        self.rect = []
        self._pause = False
        self.nimage = 0
        self.xloop = False
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
                self.index = 1
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

    def __init__(self, bs: CustomButtonConfig):
        self.screen = bs.screen
        self.screen_rect = bs.screen.get_rect()
        self.__is_check_down = False
        self.font = pygame.font.SysFont(bs.font, bs.font_size)
        self.text = bs.text
        self.command = bs.command
        self.args = bs.args
        self.text_color = bs.text_color
        self.sounds_on_chick = bs.sounds_on_chick
        self.up_image = bs.images[0]
        try:
            self.down_image = bs.images[1]
        except IndexError:
            self.down_image = bs.images[0]
        try:
            self.over_image = bs.images[2]
        except IndexError:
            self.over_image = bs.images[0]
        try:
            self.lock_image = bs.images[3]
        except IndexError:
            self.lock_image = bs.images[0]
        if isinstance(self.up_image, str):
            self.up_image = pygame.image.load(self.up_image).convert().convert_alpha()
        if isinstance(self.down_image, str):
            self.down_image = pygame.image.load(self.down_image).convert().convert_alpha()
        if isinstance(self.over_image, str):
            self.over_image = pygame.image.load(self.over_image).convert().convert_alpha()
        if isinstance(self.lock_image, str):
            self.lock_image = pygame.image.load(self.lock_image).convert().convert_alpha()
        self.image = self.up_image
        self.rect = self.image.get_rect()
        self.hidden = False
        self.lock = False

    def is_chick(self, event) -> bool:
        """Return Whether to click"""
        if self.hidden or self.lock:
            return False
        if event.type != pygame.MOUSEBUTTONUP:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def _is_check_down(self, event):
        if not self.__is_check_down:
            return False
        if self.hidden or self.lock:
            return False
        if event.type != pygame.MOUSEBUTTONDOWN:
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

    def update(self, event: pygame.event.EventType):
        """
        Update the Button
        :param event: pygame event
        """
        if self.hidden:
            return
        if self.lock:
            self.image = self.lock_image
        elif self._is_check_down(event):
            self.__is_check_down = True
            self.image = self.down_image
            if self.sounds_on_chick is not None:
                sound = pygame.mixer.Sound(self.sounds_on_chick)
                sound.play()
        elif self.is_chick(event):
            self.__is_check_down = False
            self.image = self.up_image

            if self.command is not None:
                self.command(*self.args)
        elif self.is_hover():
            self.image = self.over_image
        else:
            self.image = self.up_image

    def draw(self):
        """Draw the Button"""
        if self.hidden:
            return
        msg_color = self.text_color[0] if not self.lock else self.text_color[1]
        msg_image = self.font.render(self.text, True, msg_color)
        msg_rect = msg_image.get_rect()
        msg_rect.center = self.rect.center

        self.screen.blit(self.image, self.rect)
        self.screen.blit(msg_image, msg_rect)


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

    def is_chick_down(self, event) -> bool:
        """
        :return bool: whether it was clicked
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def update(self, event) -> bool:
        """Update the Button"""
        if self.hidden:
            return False
        if self.lock:
            self.mode = TextButton.BUTTON_LOCK
            return False
        if self.is_chick_down(event):
            self.mode = TextButton.BUTTON_DOWN
            if self.sounds_on_chick is not None:
                pygame.mixer.Sound(self.sounds_on_chick).play()
        elif self.button_is_chick(event):
            self.mode = TextButton.BUTTON_UP
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
        if event.type != pygame.MOUSEBUTTONUP:
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def button_is_hover(self, event):
        """Return Whether to hover"""
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            return False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def draw(self) -> None:
        """Draw Button"""
        if self.hidden:
            return
        if self.mode == TextButton.BUTTON_UP:
            pygame.draw.rect(self.screen, self.color[0], self.rect, width=0)
            pygame.draw.line(self.screen, (169, 169, 169), self.rect.bottomleft,
                             self.rect.bottomright, width=4)
            pygame.draw.line(self.screen, (169, 169, 169),
                             self.rect.bottomright, self.rect.topright,
                             width=4)
            msg_image = self.font.render(self.text, True, self.text_color[0])
            msg_rect = msg_image.get_rect()
            msg_rect.center = self.rect.center
            self.screen.blit(msg_image, msg_rect)
        elif self.mode == TextButton.BUTTON_DOWN:
            pygame.draw.rect(self.screen, self.color[1], self.rect, width=0)
            pygame.draw.line(self.screen, (169, 169, 169), self.rect.topleft,
                             self.rect.topright, width=4)
            pygame.draw.line(self.screen, (169, 169, 169), self.rect.bottomleft,
                             self.rect.topleft, width=4)
            msg_image = self.font.render(self.text, True, self.text_color[2])
            msg_rect = msg_image.get_rect()
            msg_rect.centery = self.rect.centery + 3
            msg_rect.centerx = self.rect.centerx + 3
            self.screen.blit(msg_image, msg_rect)
        elif self.mode == TextButton.BUTTON_OVER:
            pygame.draw.rect(self.screen, self.color[2], self.rect, width=0)
            pygame.draw.line(self.screen, (169, 169, 169), self.rect.bottomleft,
                             self.rect.bottomright, width=4)
            pygame.draw.line(self.screen, (169, 169, 169),
                             self.rect.bottomright, self.rect.topright,
                             width=4)
            msg_image = self.font.render(self.text, True, self.text_color[3])
            msg_rect = msg_image.get_rect()
            msg_rect.center = self.rect.center
            self.screen.blit(msg_image, msg_rect)
        else:
            pygame.draw.rect(self.screen, self.color[3], self.rect, width=0)
            pygame.draw.line(self.screen, (169, 169, 169), self.rect.bottomleft,
                             self.rect.bottomright, width=4)
            pygame.draw.line(self.screen, (169, 169, 169),
                             self.rect.bottomright, self.rect.topright,
                             width=4)
            msg_image = self.font.render(self.text, True, self.text_color[1])
            msg_rect = msg_image.get_rect()
            msg_rect.center = self.rect.center
            self.screen.blit(msg_image, msg_rect)


class DisplayText:
    """
    Display Text on the scene
    :param: screen(pghelper.Suface): The surface of the scene to be drawn
    :param: font(str): Draws a string representation of the font default: None
    :param: size(int): The font size
    :param: text(str): The text
    :param: new_color(tuple): The text new_color
    """

    def __init__(self, screen: pygame.Surface, *, font=None, size=20, text='', color=(255, 255, 255)):
        pygame.font.init()
        self.screen = screen
        self.font = pygame.font.SysFont(font, size)
        self.text = ''
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.set_value(text, color)

    def set_value(self, new_text: str, new_color=None):
        """
        Reset the text content and color
        :param new_text: new text
        :param new_color: new Color, default: The original color
        """
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


class Dragger:
    """
    A draggable image component
    :param screen (pghelper.Surface): The surface of the scene to be drawn
    :param images (tuple): A set of image paths or Suface objects representing the states of the component,
    where the element images are in order: normal state, pressed state, suspended state, locked state
    """

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
        if self.hidden:
            return
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

    def __init__(self, screen, loc, image_path, rect=None):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        if rect is not None:
            self.rect = rect
        else:
            self.rect = self.image.get_rect()
            self.rect.topleft = loc
        self.hidden = False

    def flip(self, flip_horizontal: bool = False, flip_vertical: bool = False):
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
        """Get the rectangle of the image"""
        return self.rect

    def draw(self):
        """Draw the image"""
        if self.hidden:
            return
        self.screen.blit(self.image, self.rect)


class RadioButtons:
    """
    Set of radio boxes based on checkboxes
    :param screen (pghelper.Surface): The surface of the scene to be drawn
    :param buttons (List[CheckBox]): A set of CheckBox instances
    """

    def __init__(self, screen: pygame.Surface, buttons: List[CheckBox]):
        self.screen = screen
        self.buttons = buttons
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
                    button.image = button.on_down_image
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

    def __init__(self, itc: InputTextConfig):
        self.__cursor_loc = None
        self.__focused_image_rect = None
        self.rect = None
        self.image_rect = None
        self.loc = None
        self.__next_field_on_tab = None
        self.__cursor_ms_counter = None
        self.cursor_position = None
        self.__text = None
        self.__focus = None
        self.__cursor_visible = None
        self._init(itc.screen, itc.loc, itc.value, itc.font, itc.font_size,
                   itc.width, itc.text_color, itc.color, itc.focus_color,
                   itc.init_focus, itc.mask, itc.keep_focus_on_submit, itc)

    def _init(self, window, loc, value, font_name, font_size, width, text_color,
              background_color, focus_color, initial_focus, mask,
              keep_focus_on_submit, itc):
        """
        initialization
        This method shouldn't be accessed, it's not an interface, it's an implementation.
        So if you ARE READING THIS DOCUMENT, you HAVE violated the CLIENT PROGRAMMER PRINCIPLE!!(╯▔皿▔)╯
        """

        self.is_enabled = True
        self.hidden = False

        self.screen = window
        self.loc = loc
        self.__text = value
        self.font = pygame.font.SysFont(font_name, font_size)

        self.command = itc.command
        self.args = itc.args

        self.width = width
        self.__focus = initial_focus
        self.__text_color = text_color
        self.__background_color = background_color
        self.__focus_color = focus_color  # new_color of __focus rectangle around __text
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

        self._update_image()  # create the image of the starting __text

    def _update_image(self):
        """
        Internal method to render __text as an image.
        This method shouldn't be accessed, it's not an interface, it's an implementation.
        So if you ARE READING THIS DOCUMENT, you HAVE violated the CLIENT PROGRAMMER PRINCIPLE!!(╯▔皿▔)╯
        """
        if self.__background_color is not None:
            self.__text_image.fill(self.__background_color)

        # Render the __text as a single line, and blit it onto the __text_image surface
        if self.mask is None:
            line_surface = self.font.render(self.__text, True, self.__text_color)
        else:
            n_chars = len(self.__text)
            masked_text = self.mask * n_chars
            line_surface = self.font.render(masked_text, True, self.__text_color)
        self.__text_image.blit(line_surface, (0, 0))

    def update(self, event):
        """Update the InputBox"""
        if not self.is_enabled:
            return False
        if self.hidden:
            return False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (
                event.button == 1):  # user clicked
            the_x, the_y = event.pos

            if self.image_rect.collidepoint(the_x, the_y):
                if not self.__focus:
                    self.__focus = True  # give this field __focus
                    pygame.key.set_repeat(InputText.KEY_REPEAT_DELAY,
                                          InputText.KEY_REPEAT_RATE)
                else:
                    # Field already has __focus, must position the cursor where the user clicked
                    n_pixels_from_left = the_x - self.loc[0]
                    n_chars = len(self.__text)

                    last_char_offset = self.font.size(self.__text)[0]
                    if n_pixels_from_left >= last_char_offset:
                        self.cursor_position = n_chars
                    else:
                        for this_char_num in range(0, n_chars):
                            this_char_offset = \
                                self.font.size(self.__text[:this_char_num])[0]
                            if this_char_offset >= n_pixels_from_left:
                                self.cursor_position = this_char_num  # Found the proper position for the cursor
                                break
                    self.__cursor_visible = True  # Show the cursor at the click point

            else:
                self.__focus = False
            return False  # means:  handled click, nothing for client to do

        if not self.__focus:  # if this field does not have __focus, don't do anything
            return False

        if event.type == pygame.KEYDOWN:
            current_key = event.key

            if current_key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.__focus = self.__keep_focus_on_submit  # defaults to False - lose __focus with Enter/Return
                if not self.__focus:
                    pygame.key.set_repeat(0)  # turn off repeating characters
                self._update_image()

                if self.command is not None:
                    self.command(*self.args)

                # User is done typing, return True to signal that __text is available (via a call to get_value)
                return True

            elif current_key == InputText.CANCELLED_TAB:
                # See code below setting up CANCELLED_TAB
                # If we get a CANCELLED_TAB as the current key, ignore it, already shifted __focus
                pass

            elif current_key == pygame.K_BACKSPACE:
                self.__text = self.__text[:max(self.cursor_position - 1, 0)] + \
                              self.__text[self.cursor_position:]

                # Subtract one from cursor_pos, but do not go below zero:
                self.cursor_position = max(self.cursor_position - 1, 0)
                self._update_image()

            elif current_key == pygame.K_DELETE:  # forward delete key
                self.__text = self.__text[:self.cursor_position] + \
                              self.__text[self.cursor_position + 1:]
                self._update_image()

            elif current_key == pygame.K_RIGHT:
                if self.cursor_position < len(self.__text):
                    self.cursor_position += 1

            elif current_key == pygame.K_LEFT:
                if self.cursor_position > 0:
                    self.cursor_position -= 1

            elif current_key == pygame.K_END:
                self.cursor_position = len(self.__text)

            elif current_key == pygame.K_HOME:
                self.cursor_position = 0

            elif current_key in (pygame.K_UP, pygame.K_DOWN):
                pass

            elif current_key == pygame.K_TAB:
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
                unicode_of_key = event.unicode  # remember for potential repeating key
                self.__text = self.__text[:self.cursor_position] + unicode_of_key + self.__text[self.cursor_position:]
                self.cursor_position += len(unicode_of_key)
                self._update_image()

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
            self.__cursor_ms_counter += self.clock.get_time()
            if self.__cursor_ms_counter >= self.__cursor_switch_ms:
                self.__cursor_ms_counter %= self.__cursor_switch_ms
                self.__cursor_visible = not self.__cursor_visible

            if self.__cursor_visible:
                cursor_offset = self.font.size(self.__text[:self.cursor_position])[
                    0]
                if self.cursor_position > 0:  # Try to get between characters
                    cursor_offset -= 1
                if cursor_offset < self.width:  # if the loc is within the __text area, draw it
                    self.__cursor_loc[0] = self.loc[0] + cursor_offset
                    self.screen.blit(self.cursor_surface, self.__cursor_loc)

            self.clock.tick()

    # Helper methods
    def get_value(self):
        """Returns the text entered by the user"""
        return self.__text

    def set_value(self, new_text):
        """Sets new __text into the field"""
        self.__text = new_text
        self.cursor_position = len(self.__text)
        self._update_image()

    def is_focus(self) -> bool:
        """

        :return:
        """
        return self.__focus

    def clear(self, keep_focus=False):
        """Clear the text in the field"""
        self.__text = ''
        self.__focus = keep_focus
        self._update_image()

    def remove_focus(self):
        """
        remove focus
        """
        self.__focus = False

    def give_focus(self):
        """
        Give focus to this field
        Make sure focus is removed from any previous field before calling this
        """
        self.__focus = True

    def set_next_field_on_tab(self, next_field_on_tab):
        """
        :param next_field_on_tab: 
        """
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


if __name__ == '__main__':
    import sys

    import pygame

    from gamehelpers.pghelper import *
    from gamehelpers import *

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    config = TextButtonConfig(screen)
    config.command = print
    config.args = ('Hello, TextButton!',)
    config.text = 'Hello, TextButton'

    text_button = TextButton(config)
    text_button.rect.center = screen.get_rect().center
    text_button.rect.top = screen.get_rect().top + 10

    config = CheckBoxConfig(screen)
    config.text = 'RadioButton 1'
    config.image_paths = (
        r'..\images\checkBoxOnUp.png',
        r'..\images\checkBoxOnDown.png',
        r'..\images\checkBoxOffUp.png',
        r'..\images\checkBoxOffDown.png'
    )
    radio_buttons = []

    checkbox = CheckBox(config)
    checkbox.rect.center = screen.get_rect().center
    checkbox.rect.top -= 30
    radio_buttons.append(checkbox)

    config.text = 'RadioButton 2'
    checkbox = CheckBox(config)
    checkbox.rect.center = screen.get_rect().center
    radio_buttons.append(checkbox)

    config.text = 'RadioButton 3'
    checkbox = CheckBox(config)
    checkbox.rect.center = screen.get_rect().center
    checkbox.rect.top += 30
    radio_buttons.append(checkbox)
    radio_button = RadioButtons(screen, radio_buttons)

    config = CustomButtonConfig(screen, [
        r'..\images\ButtonUp.png',
        r'..\images\ButtonDown.png',
        r'..\images\ButtonOver.png',
        r'..\images\ButtonLock.png'
    ])
    config.text = 'Get Radio Button'
    config.font_size = 20
    config.command = lambda: print(radio_button.get_focus())
    config.args = ()

    custom_button = CustomButton(config)
    custom_button.rect.center = screen.get_rect().center
    custom_button.rect.top = screen.get_rect().top + 60

    dragger = Dragger(screen, (
        r'..\images\dragMeUp.png',
        r'..\images\dragMeDown.png',
        r'..\images\dragMeOver.png',
        r'..\images\dragMeDisabled.png'
    ))
    dragger.rect.bottomright = screen.get_rect().bottomright

    text = DisplayText(screen, text="", font=None)
    text.set_value('a')

    text2 = DisplayText(screen, text='', font=None)
    text2.set_value('b')
    text2.rect.topright = screen.get_rect().topright

    image = Image(screen, (0, 0), r'..\images\pythonIcon.png')
    image.rect.bottomleft = (10, screen.get_height() - 10)

    config = InputTextConfig(screen)
    config.value = '652098gyh'
    config.loc = (300, 200)

    input_text = InputText(config)

    _ = (
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
    images = load_images(_)
    config = AnimateConfig(screen, images)
    config.loop = True

    animate = Animate(config)

    count_up = CountUpTimer()
    count_down = CountDownTimer('1:30:20.5', command=lambda: print('OK!'))
    count_up.start()
    count_down.start()

    while True:
        animate.update()
        count_down.update()
        text.set_value(f'Count Up Timer: {count_down.get_time(mode='HHMMSS')}')
        text2.set_value(f'Count Down Timer: {count_up.get_time(mode='HHMMSS')}')
        text2.rect.topright = screen.get_rect().topright
        for event in pygame.event.get():
            text_button.update(event)
            custom_button.update(event)
            radio_button.update(event)
            dragger.update(event)
            input_text.update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                animate.play()
            elif event.type == pygame.KEYUP:
                animate.pause()
        draw_background(screen, '..\\images\\background.jpg')
        text_button.draw()
        custom_button.draw()
        radio_button.draw()
        dragger.draw()
        text.draw()
        text2.draw()
        image.draw()
        input_text.draw()
        animate.draw()
        pygame.display.update()
