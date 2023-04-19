import flet as ft

from views import Welcome, ChatBox

def app(page: ft.Page):
    page.scroll = "auto"
    page.add(Welcome(), ChatBox())
    page.update()



ft.app(target=app , view=ft.WEB_BROWSER, port=8502, assets_dir="assets")