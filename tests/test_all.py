import os

import pygame

from pyhelper import chdir
from pyhelper.gamehelpers import *
from pyhelper.gamehelpers.pghelper import *
from pyhelper.gamehelpers.pghelper.widgets import *

if __name__ == "__main__":
    if not os.path.exists("pyhelper"):
        os.chdir("..")
    with chdir("./pyhelper"):
        os.system("python __init__.py")
        os.system("python mathhelper.py")
        os.system("python color.py")

    if not os.getcwd().endswith("pghelper"):
        if os.getcwd().endswith("pyhelper\\pyhelper"):
            os.chdir(r".\gamehelpers\pghelper")
        else:
            os.chdir(os.path.abspath(r".\pyhelper\gamehelpers\pghelper"))

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    config = TextButtonConfig(screen)
    config.command = print
    config.args = ("Hello, TextButton!",)
    config.text = "Hello, TextButton"

    text_button = TextButton(config)
    text_button.rect.center = screen.get_rect().center
    text_button.rect.top = screen.get_rect().top + 10

    config = CheckBoxConfig(screen)
    config.text = "RadioButton 1"
    config.image_paths = (
        r"..\images\checkBoxOnUp.png",
        r"..\images\checkBoxOnDown.png",
        r"..\images\checkBoxOffUp.png",
        r"..\images\checkBoxOffDown.png",
    )
    radio_buttons = []

    checkbox = CheckBox(config)
    checkbox.rect.center = screen.get_rect().center
    checkbox.rect.top -= 30
    radio_buttons.append(checkbox)

    config.text = "RadioButton 2"
    checkbox = CheckBox(config)
    checkbox.rect.center = screen.get_rect().center
    radio_buttons.append(checkbox)

    config.text = "RadioButton 3"
    checkbox = CheckBox(config)
    checkbox.rect.center = screen.get_rect().center
    checkbox.rect.top += 30
    radio_buttons.append(checkbox)
    radio_button = RadioButtons(screen, radio_buttons)

    config = CustomButtonConfig(
        screen,
        [
            r"..\images\ButtonUp.png",
            r"..\images\ButtonDown.png",
            r"..\images\ButtonOver.png",
            r"..\images\ButtonLock.png",
        ],
    )
    config.text = "Get Radio Button"
    config.font_size = 20
    config.command = lambda: print(radio_button.get_focus())
    config.args = ()

    custom_button = CustomButton(config)
    custom_button.rect.center = screen.get_rect().center
    custom_button.rect.top = screen.get_rect().top + 60

    dragger = Dragger(
        screen,
        (
            r"..\images\dragMeUp.png",
            r"..\images\dragMeDown.png",
            r"..\images\dragMeOver.png",
            r"..\images\dragMeDisabled.png",
        ),
    )
    dragger.rect.bottomright = screen.get_rect().bottomright

    text = DisplayText(screen, text="", font=None)
    text.set_value("a")

    text2 = DisplayText(screen, text="", font=None)
    text2.set_value("b")
    text2.rect.topright = screen.get_rect().topright

    image = Image(screen, r"..\images\pythonIcon.png", loc=(0, 0))
    image.rect.bottomleft = (10, screen.get_height() - 10)

    config = InputTextConfig(screen)
    config.value = "652098gyh"
    config.loc = (300, 200)

    input_text = InputText(config)

    _ = (
        r"..\images\f1.gif",
        r"..\images\f2.gif",
        r"..\images\f3.gif",
        r"..\images\f4.gif",
        r"..\images\f5.gif",
        r"..\images\f6.gif",
        r"..\images\f7.gif",
        r"..\images\f8.gif",
        r"..\images\f9.gif",
        r"..\images\f10.gif",
    )
    images = load_images(_)
    config = AnimateConfig(screen, images)
    config.loop = True

    animate = Animate(config)

    count_up = CountUpTimer()
    count_down = CountDownTimer("1:30:20.5", command=lambda: print("OK!"))
    count_up.start()
    count_down.start()

    is_running = True
    while is_running:
        animate.update()
        count_down.update()
        text.set_value(f"Count Up Timer: {count_down.get_time(mode='HHMMSS')}")
        text2.set_value(f"Count Down Timer: {count_up.get_time(mode='HHMMSS')}")
        text2.rect.topright = screen.get_rect().topright
        for event in pygame.event.get():
            text_button.update(event)
            custom_button.update(event)
            radio_button.update(event)
            dragger.update(event)
            input_text.update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                is_running = False
                break
            elif event.type == pygame.KEYDOWN:
                animate.play()
            elif event.type == pygame.KEYUP:
                animate.pause()
        if not is_running:
            break
        draw_background(screen, "..\\images\\background.jpg")
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
    pygame.init()
    SCENE_A = "scene A"
    SCENE_B = "scene B"
    SCENE_C = "scene C"

    class SceneA(Scene):
        def __init__(self, screen):
            self.screen = screen
            self.screen_rect = screen.get_rect()

            button_config = TextButtonConfig(screen)
            button_config.width = 100
            button_config.text = "Go to Scene A"
            self.goto_a_button = TextButton(button_config)
            self.goto_a_button.rect.left = self.screen_rect.left + 15
            self.goto_a_button.rect.bottom = self.screen_rect.bottom - 30
            self.goto_a_button.lock = True

            button_config.text = "Go to Scene B"
            button_config.command = lambda: self.go_to_scene(SCENE_B)
            self.goto_b_button = TextButton(button_config)
            self.goto_b_button.rect.center = self.screen_rect.center

            button_config.text = "Go to Screen C"
            button_config.command = lambda: self.go_to_scene(SCENE_C)
            self.goto_c_button = TextButton(button_config)
            self.goto_c_button.rect.right = self.screen_rect.right - 30

        def get_scene_key(self):
            return SCENE_A

        def update(self, events, key_pressed_list):
            for event in events:
                self.goto_a_button.update(event)
                self.goto_b_button.update(event)
                self.goto_c_button.update(event)

        def draw(self):
            self.screen.fill((0, 0, 0))
            self.goto_a_button.draw()
            self.goto_b_button.draw()
            self.goto_c_button.draw()

    class SceneB(Scene):
        def __init__(self, screen):
            self.screen = screen
            self.screen_rect = screen.get_rect()

            button_config = TextButtonConfig(screen)
            button_config.command = lambda: self.go_to_scene(SCENE_A)
            button_config.width = 100
            button_config.text = "Go to Scene A"
            self.goto_a_button = TextButton(button_config)
            self.goto_a_button.rect.left = self.screen_rect.left + 15
            self.goto_a_button.rect.bottom = self.screen_rect.bottom - 30

            button_config.text = "Go to Scene B"
            self.goto_b_button = TextButton(button_config)
            self.goto_b_button.rect.center = self.screen_rect.center
            self.goto_b_button.lock = True

            button_config.text = "Go to Screen C"
            button_config.command = lambda: self.go_to_scene(SCENE_C)
            self.goto_c_button = TextButton(button_config)
            self.goto_c_button.rect.right = self.screen_rect.right - 30

        def get_scene_key(self):
            return SCENE_B

        def update(self, events, key_pressed_list):
            for event in events:
                self.goto_a_button.update(event)
                self.goto_b_button.update(event)
                self.goto_c_button.update(event)

        def draw(self):
            self.screen.fill((150, 0, 0))
            self.goto_a_button.draw()
            self.goto_b_button.draw()
            self.goto_c_button.draw()

    class SceneC(Scene):
        def __init__(self, screen):
            self.screen = screen
            self.screen_rect = screen.get_rect()

            button_config = TextButtonConfig(screen)
            button_config.width = 100
            button_config.text = "Go to Scene A"
            button_config.command = lambda: self.go_to_scene(SCENE_A)
            self.goto_a_button = TextButton(button_config)
            self.goto_a_button.rect.left = self.screen_rect.left + 15
            self.goto_a_button.rect.bottom = self.screen_rect.bottom - 30

            button_config.text = "Go to Scene B"
            button_config.command = lambda: self.go_to_scene(SCENE_B)
            self.goto_b_button = TextButton(button_config)
            self.goto_b_button.rect.center = self.screen_rect.center

            button_config.text = "Go to Screen C"
            self.goto_c_button = TextButton(button_config)
            self.goto_c_button.rect.right = self.screen_rect.right - 30
            self.goto_c_button.lock = True

        def get_scene_key(self):
            return SCENE_C

        def update(self, events, key_pressed_list):
            for event in events:
                self.goto_a_button.update(event)
                self.goto_b_button.update(event)
                self.goto_c_button.update(event)

        def draw(self):
            self.screen.fill((0, 200, 0))
            self.goto_a_button.draw()
            self.goto_b_button.draw()
            self.goto_c_button.draw()

    screen = pygame.display.set_mode((900, 600))

    scene_list = [SceneA(screen), SceneB(screen), SceneC(screen)]

    scene_mgr = SceneMgr(scene_list, 29)

    scene_mgr.run()
