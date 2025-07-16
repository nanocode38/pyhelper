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
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation;
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# DON'T EVEN HAVE A PERMIT TOO!
#
# Gao Yuhan(高宇涵)
# nanocode38@88.com
# nanocode38
"""
This is a collection of Pygame-based game development tool functions that rely on Python Pygame third-party libraries
Copyright (C)
"""
import sys
from abc import ABC, abstractmethod
from typing import *

import pygame

__all__ = [
    "disassemble_sprite_sheet",
    "draw_background",
    "load_images",
    "Scene",
    "SceneMgr",
]


def disassemble_sprite_sheet(image_path: str, width: int, height: int, num_of_image) -> list:
    """
    This function processes a Sprite image into a set of loaded Surface objects

    Args:
        image_path: the path to the total Sprite graph
        width: The length of an image
        height: The height of an image
        num_of_image: The total number of photos

    Returns:
        list: Surface objects for all images
    """
    images = []
    sprite_sheet_image = pygame.image.load(image_path)
    n_cols = sprite_sheet_image.get_width() // width

    row, col = 0, 0
    for image_num in range(num_of_image):
        x = col * height
        y = row * width

        # Create a subsurface from the bigger spriteSheet
        subsurface_rect = pygame.Rect(x, y, width, height)
        image = sprite_sheet_image.subsurface(subsurface_rect)
        images.append(image)

        col += 1
        if col == n_cols:
            col = 0
            row += 1

    return images


def load_images(image_paths: Iterator[str]):
    """
    Loading a series of images

    Args:
        image_paths: A list of paths for a series of images

    Returns:
        Iterator[pygame.Surface]: A list of loaded Surface objects
    """
    images = []
    for path in image_paths:
        images.append(pygame.image.load(path))
    return images


class Background:
    """
    Draw the game background

    Args:
        screen: the Surface of the scene to paint
        image_path: image path for background image
        width: The background width, default: 0, the original width, can be pygame.FULLSCREEN is the screen width
        height: The background height, default: 0, the original height, can be pygame.FULLSCREEN is the screen height
    """

    def __init__(self):
        self.image = None

    def __call__(
        self,
        screen: pygame.SurfaceType,
        image_path: str,
        width: int = 0,
        height: int = 0,
    ) -> None:
        if self.image is None:
            self.image = pygame.image.load(image_path)
            if width != 0:
                if width == pygame.FULLSCREEN:
                    width = screen.get_width()
                self.image = pygame.transform.scale(self.image, (width, self.image.get_height()))
            if height != 0:
                if height == pygame.FULLSCREEN:
                    height = screen.get_height()
                self.image = pygame.transform.scale(self.image, (self.image.get_width(), height))
        screen.blit(self.image, (0, 0))


draw_background = Background()


# noinspection GrazieInspection
class Scene(ABC):
    """
    The Scene class is an abstract class to be used as a base class for any scenes that you want to create.

    In the startup code for your  application, you create an instance of each of the
    scenes that you want to be available.  Then you build a dictionary like this

        |    {<sceneKey1>:<sceneObject1>, <sceneKey2>:<sceneObject2>, ...}

    Then you pass this dictionary when you instantiate the Scene Manager.
    See the SceneMgr documentation for details.

    To create a scene, you must write a subclass that inherits from this class.
    Your class must implement these methods

        |   __init__(), update(), draw(), get_scene_key()

    Other methods can be overridden if you wish:

        | enter(), leave()

    You can add any additional methods that your class requires.
    Additionally, there are other methods to allow you to get or set info, or navigate to other scenes:

        | go_to_scene(), quit(), request(), respond() and more.

    In the __init__() method of your scene subclass, you will receive a window reference.
    You should copy this into an instance variable like this, and use it when drawing:

        |    def __init__(self, screen):
        |        self.screen = screen
        |        self.screen_rect = screen.get_rect()
        |        # Add any initialization you want to do here.


        You also need to write a get_scene_key() method that returns a string
        or constant that uniquely identifies the scene.  It is recommended that you
        build and import a Constants.py file that contains constants for each scene,
        and use the key associated with the current scene here.
        |    def get_scene_key(self):
        |        return <string or CONSTANT that identifies this scene>

    When your scene is active, the SceneManager calls a standard set of methods in the current scene.
    Therefore, all scenes must implement these methods (polymorphism):

        |    update()        # called in every frame
        |    draw()          # called in every frame

    The following methods can optionally be implemented in a scene.  If they are not
    implemented, then the null version in the Scene subclass will be used.
    (The Scene class' default versions only execute a pass statement):

        |    enter()          # called once whenever the scene is entered
        |    update()         # called in every frame
        |    leave()          # called once whenever the scene is left

    When you want to go to a new scene, call:

        |    self.go_to_scene() and pass in the sceneKey of the scene you want to go to,
        |    and optionally, pass any data you want the next scene to receive in its enter() method.

    If you want to quit the program from your scene, call:
        |    self.quit()
    """

    @abstractmethod
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_rect = screen.get_rect()

    @abstractmethod
    def get_scene_key(self):
        """This returns a unique identity string that represents the internal representation of the scene"""
        pass

    @abstractmethod
    def update(self, events: list[pygame.event.EventType], key_pressed_list: list[bool]) -> None:
        """
        This method is called in every frame of the scene to handle events and key presses

        Args:
            events: a list of events your method should handle.
            key_pressed_list: a list of keys that are pressed (a Boolean for each key).
        """
        pass

    def enter(self, data: Any = None):
        """
        This method is called whenever the user enters a scene.
        Should be overridden if you expect data when your scene is entered.
        Add any code you need to start or re-start the scene

        Args:
            data: can be of any type agreed to by the old and new scenes
        """
        pass

    def _set_ref_to_scene_mgr(self, scene_mgr):
        self.scene_mgr = scene_mgr

    @abstractmethod
    def draw(self) -> None:
        """
        This method is called in every frame of the scene to draw anything that needs to be drawn
        Your code MUST override this method.
        """
        pass

    def leave(self) -> None:
        """
        This method is called whenever the user leaves a scene
        Override this method, and add any code you need to clean up the scene before leaving
        """
        pass

    def quit(self) -> None:
        """Call this method if you want to quit, from inside a scene"""
        self.go_to_scene(None)

    def go_to_scene(self, next_scene_key: Optional[str], data=None) -> None:
        """
        Call this method whenever you want to go to a new scene

        Args:
            next_scene_key: the scene key (string) of the scene to go to
            data: any data you want sent to the next scene (defaults: None)
        """
        self.scene_mgr._go_to_scene(next_scene_key, data)

    def request(self, target_scene_key: str, request_id: Any) -> None:
        """
        Call this method to get information from another scene

        The target scene must implement a method named: respond,
        it can return any info in any way the two scenes agree upon

        Args:
            target_scene_key: the scene key (string) of the scene to ask for data
            request_id: the data you want from the target scene"""
        info = self.scene_mgr._request_respond(target_scene_key, request_id)
        return info

    def send(self, target_scene_key: str, send_id: Any, info: Any) -> None:
        """
        Call this method to send information to  another scene

        The other scene must implement a method named:  receive().
        You can pass any info the two scenes agree upon

        Args:
            target_scene_key: the scene key (string) of the scene to ask for data
            send_id: the type of data you are sending the target scene
            info: the actual data to send (can be any type)
        """
        self.scene_mgr._send_receive(target_scene_key, send_id, info)

    def send_all(self, send_id, info) -> None:
        """
        Call this method to send information to all other scenes

        The other scenes must implement a method named:  receive().
        You can pass any info that the sender and all other scenes agree upon

        Args:
            send_id: the type of data you are sending the target scene
            info: the actual data to send
        """
        self.scene_mgr._send_all_receive(self, send_id, info)  # pass in self to identify sender

    def respond(self, request_id: Any) -> None:
        """
        Respond to a request for information from some other scene

        You must override this method if your scene expects to handle
        requests for information from other scenes via calls to:  request()
        Args:
            request_id: identifier of what data to be sent back to the caller
        """
        raise NotImplementedError

    def receive(self, receive_id: Any, info: Any) -> None:
        """
        Receives information from another scene.

        You must override this method if your scene expects to receive information from
        other scenes sending information via calls to:  send()

        Args:
            receive_id - an identifier for what type of information is being received
            info - the information sent from another scene
        """
        raise NotImplementedError

    def add_scene(self, scene_key: str, scene) -> None:
        """
        Call this method whenever you want to add a new scene dynamically.
        For example, you could have a game with many levels (each implemented as a scene),
        but only have the current level loaded.  As the player completes a level, you
        could do a remove_scene on the current level and do an add_scene on the
        next level, then do a goToScene on the new level.

        Args:
            scene_key: a key to uniquely identify this scene
            scene: an instance of the new scene to be added
            (typically, you would instantiate the new scene, and pass in that reference to this call)
        """
        self.scene_mgr._add_scene(scene_key, scene)

    def remove_scene(self, scene_key: str) -> None:
        """
        Call this method whenever you want to remove an existing scene
        You can remove a scene to save memory - the scene object will be deleted.
        The SceneMgr delays removing the scene until the next time through the main loop.
        Therefore, it is safe to call to remove_scene from its own scene, if you immediately
        go to another scene.

        Args:
            scene_key: the scene key (string) of the scene to remove"""
        self.scene_mgr._remove_scene(scene_key)


class SceneMgr:
    """
    SceneMgr (Scene Manager)  allows you to build a program with multiple scenes.

    The SceneMgr manages any number of scenes built as subclasses of the "Scene" class.
    For more details, see the "Scene" class.

    Args:
        scenes: is a dictionary or list that consists of:
            {<sceneKey>: <sceneObject>, <sceneKey>: <sceneObject>, ...} or [<sceneObject>, <sceneObject>, ...]
              where each sceneObject is an object instantiated from a scene class
              (For details on Scenes, see the Scene class)
        fps - is the frames per second at which the program should run

    Based on the concept of a "Scene Manager" by Blake O'Hare of Nerd Paradise
    """

    def __init__(
        self,
        scenes: Union[list, dict],
        fps: int,
        frame_rate_display: "widgets.DisplayText | None" = None,
    ):
        if isinstance(scenes, dict):
            self.scenes_dict = scenes
            keys_list = list(self.scenes_dict)  # get all the keys
            starting_key = keys_list[0]  # first key is the starting scene ley
            self.current_scene = self.scenes_dict[starting_key]

        else:  # Older style, we start with a list of scenes
            # Build a dictionary, each _entry of which is a scene key : scene object
            # Then we call getSceneKey so each scene can identify itself
            self.scenes_dict = {}
            for scene in scenes:
                key = scene.get_scene_key()  # Each scene must return a unique key to identify itself
                self.scenes_dict[key] = scene
            # The first element in the list is the used as the starting scene
            self.current_scene = scenes[0]

        self.fps = fps
        self.frame_rate_display = frame_rate_display
        self.show_frame_rate = frame_rate_display is not None  # for fast checking in main loop
        self.scenes_to_remove_list = []

        # Give each scene a reference back to the SceneMgr.
        # This allows any scene to do a goToScene, request, send,
        # or send_all, which gets forwarded to the scene manager.
        for key, scene in self.scenes_dict.items():
            scene._set_ref_to_scene_mgr(self)

    def run(self) -> None:
        """
        This method implements the main pygame loop.
        It should typically be called as the last line of your main program.
        It is designed to call a standardized set of methods in the current scene.
        All scenes must implement the following methods (polymorphism):
        |   update()  # called in every frame
        |   draw()          # called in every frame

        The following methods can be implemented in a scene:
            |   enter()  # called once whenever the scene is entered
            |   leave()  # called once whenever the scene is left

        If any is not implemented, then the version in the Scene base class,
        which only performs a pass statement, will be used.
        """

        clock = pygame.time.Clock()

        # 6 - Loop forever
        while True:
            # If there are any scenes to be removed (keys added by remove_scene method)
            if not (self.scenes_to_remove_list is []):
                for key in self.scenes_to_remove_list:
                    del self.scenes_dict[key]
                self.scenes_to_remove_list = []  # reset

            keys_down_list = pygame.key.get_pressed()

            # 7 - Check for and handle events
            events_list = []
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
                    # Tell current scene we're leaving
                    self.current_scene.leave()
                    pygame.quit()
                    sys.exit()

                events_list.append(event)

            # Here, we let the current scene process all events by calling its handleInputs() method
            # do any "per frame" actions in its update() method,
            # and call its draw() method so it can draw everything that needs to be drawn.
            self.current_scene.update(events_list, keys_down_list)
            self.current_scene.draw()
            if self.show_frame_rate:
                fps = str(clock.get_fps())
                self.frame_rate_display.set_value("FPS: " + fps)
                self.frame_rate_display.draw()

            # 11 - Update the window
            pygame.display.update()

            # 12 - Slow things down a bit
            clock.tick(self.fps)

    def _go_to_scene(self, next_scene_key, data_for_next_scene):
        if next_scene_key is None:  # meaning, exit
            pygame.quit()
            sys.exit()

        # Call the leave method of the old scene to allow it to clean up.
        # Set the new scene (based on the key) and
        # call the enter method of the new scene.
        self.current_scene.leave()
        pygame.key.set_repeat(0)  # turn off repeating characters
        try:
            self.current_scene = self.scenes_dict[next_scene_key]
        except KeyError:
            raise KeyError(
                "Trying to go to scene '" + next_scene_key + "' but that key is not in the dictionary of scenes."
            )
        self.current_scene.enter(data_for_next_scene)

    def _request_respond(self, target_scene_key, request_id):
        target_scene = self.scenes_dict[target_scene_key]
        info = target_scene.respond(request_id)
        return info

    def _send_receive(self, target_scene_key, send_id, info):
        target_scene = self.scenes_dict[target_scene_key]
        target_scene.receive(send_id, info)

    def _send_all_receive(self, sender_scene, send_id, info):
        for scene_key in self.scenes_dict:
            target_scene = self.scenes_dict[scene_key]
            if target_scene != sender_scene:
                target_scene.receive(send_id, info)

    def _add_scene(self, new_scene):
        # Ask the new scene for its scene key, and add it to the scenes dictionary
        new_scene_key = new_scene.getSceneKey()
        if new_scene_key in self.scenes_dict:
            raise KeyError("Trying to add a scene with key" + new_scene_key + "but that scene key already exists")
        self.scenes_dict[new_scene_key] = new_scene
        # Send the new scene a reference to the SceneMgr
        new_scene._set_ref_to_scene_mgr(self)

    def _remove_scene(self, scene_key_to_remove):
        if not (scene_key_to_remove in self.scenes_dict):
            raise KeyError(
                "Attempting to remove scene with key "
                + scene_key_to_remove
                + " but no scene with that key currently exists (either never defined or removed)."
            )
        # Add the key to a list of keys to be removed
        # The scene(s) will be removed the next time around the main loop.from
        # This allows a scene to make a call to remove_scene to remove itself right before doing a goToScene
        #    (and the call will return successfully)
        self.scenes_to_remove_list.append(scene_key_to_remove)
