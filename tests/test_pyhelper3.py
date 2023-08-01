import pygame
from pyhelper.pghelper import *
from pyhelper.pgwidgets import *

SCENE_A = 0
SCENE_B = 1
SCENE_C = 2


class SceneA(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        button_config = TextButtonConfig(screen)
        button_config.width = 100
        button_config.text = 'Go to Scene A'
        self.gotoAbuttom = TextButton(button_config)
        self.gotoAbuttom.rect.left = self.screen_rect.left + 15
        self.gotoAbuttom.rect.bottom = self.screen_rect.bottom - 30
        self.gotoAbuttom.lock = True

        button_config.text = 'Go to Scene B'
        button_config.command = lambda: self.go_to_scene(SCENE_B)
        self.gotoBbuttom = TextButton(button_config)
        self.gotoBbuttom.rect.center = self.screen_rect.center

        button_config.text = 'Go to Screen C'
        button_config.command = lambda: self.go_to_scene(SCENE_C)
        self.gotoCbuttom = TextButton(button_config)
        self.gotoCbuttom.rect.right = self.screen_rect.right - 30

    def get_scenen_key(self):
        return SCENE_A

    def update(self, events, key_pressed_list):
        for event in events:
            self.gotoAbuttom.update(event)
            self.gotoBbuttom.update(event)
            self.gotoCbuttom.update(event)
            # if self.gotoBbuttom.is_chick(event):
            #     self.gotoBbuttom.command()
            # if self.gotoCbuttom.is_chick(event):
            #     self.gotoCbuttom.command()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.gotoAbuttom.draw()
        self.gotoBbuttom.draw()
        self.gotoCbuttom.draw()


class SceneB(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        button_config = TextButtonConfig(screen)
        button_config.command = lambda: self.go_to_scene(SCENE_A)
        button_config.width = 100
        button_config.text = 'Go to Scene A'
        self.gotoAbuttom = TextButton(button_config)
        self.gotoAbuttom.rect.left = self.screen_rect.left + 15
        self.gotoAbuttom.rect.bottom = self.screen_rect.bottom - 30

        button_config.text = 'Go to Scene B'
        self.gotoBbuttom = TextButton(button_config)
        self.gotoBbuttom.rect.center = self.screen_rect.center
        self.gotoBbuttom.lock = True

        button_config.text = 'Go to Screen C'
        button_config.command = lambda: self.go_to_scene(SCENE_C)
        self.gotoCbuttom = TextButton(button_config)
        self.gotoCbuttom.rect.right = self.screen_rect.right - 30

    def get_scenen_key(self):
        return SCENE_B

    def update(self, events, key_pressed_list):
        for event in events:
            self.gotoAbuttom.update(event)
            self.gotoBbuttom.update(event)
            self.gotoCbuttom.update(event)
            # if self.gotoBbuttom.is_chick(event):
            #     self.gotoBbuttom.command()
            # if self.gotoCbuttom.is_chick(event):
            #     self.gotoCbuttom.command()

    def draw(self):
        self.screen.fill((150, 0, 0))
        self.gotoAbuttom.draw()
        self.gotoBbuttom.draw()
        self.gotoCbuttom.draw()


class SceneC(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        button_config = TextButtonConfig(screen)
        button_config.width = 100
        button_config.text = 'Go to Scene A'
        button_config.command = lambda: self.go_to_scene(SCENE_A)
        self.gotoAbuttom = TextButton(button_config)
        self.gotoAbuttom.rect.left = self.screen_rect.left + 15
        self.gotoAbuttom.rect.bottom = self.screen_rect.bottom -30

        button_config.text = 'Go to Scene B'
        button_config.command = lambda: self.go_to_scene(SCENE_B)
        self.gotoBbuttom = TextButton(button_config)
        self.gotoBbuttom.rect.center = self.screen_rect.center

        button_config.text = 'Go to Screen C'
        self.gotoCbuttom = TextButton(button_config)
        self.gotoCbuttom.rect.right = self.screen_rect.right - 30
        self.gotoCbuttom.lock = True

    def get_scenen_key(self):
        return SCENE_C

    def update(self, events, key_pressed_list):
        for event in events:
            self.gotoAbuttom.update(event)
            self.gotoBbuttom.update(event)
            self.gotoCbuttom.update(event)
            # if self.gotoBbuttom.is_chick(event):
            #     self.gotoBbuttom.command()
            # if self.gotoCbuttom.is_chick(event):
            #     self.gotoCbuttom.command()

    def draw(self):
        self.screen.fill((0, 200, 0))
        self.gotoAbuttom.draw()
        self.gotoBbuttom.draw()
        self.gotoCbuttom.draw()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    scene_list = [SceneA(screen),
                  SceneB(screen),
                  SceneC(screen)]

    scene_mgr = SceneMgr(scene_list, 29)

    scene_mgr.run()
