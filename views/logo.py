import flet as ft

from config import IMG_PATH

class Logo(ft.UserControl):
    def __init__(self, img_name: str = "robot.png", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_path = f'{IMG_PATH}/{img_name}'

    def build(self):
        return ft.Image(src=self.img_path,
                        width=80,
                        height=80)
