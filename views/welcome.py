import flet as ft

from .logo import Logo

color = "#67dfe2"


class Welcome(ft.UserControl):
    welcome_header = "Welcome to ShopAI"
    welcome_Text = "ShopAI is powered by OpenAI and trained by \nShopcek to enhance your experience and provide \nquick responses to any inquiries you may have. \nFeel free to utilize ShopAI whenever you need \nassistance or have any questions about our services. \nWe are always here to help!"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(ft.Row([self.text,self.logo],
                                   alignment=ft.MainAxisAlignment.CENTER,
                                   vertical_alignment=ft.CrossAxisAlignment.END))

    @property
    def text(self):
        if not hasattr(self, '_text'):
            self._text = ft.Column([
                ft.Text(self.welcome_header,
                        color=color,
                        size=25,
                        weight=ft.FontWeight.W_900,
                        selectable=True,
                        text_align=ft.alignment.center_right),
                ft.Text(self.welcome_Text, selectable=True, text_align=ft.alignment.center_right)
            ])

        return self._text

    @property
    def logo(self):
        if not hasattr(self, '_logo'):
            self._logo = Logo()

        return self._logo
