from json import load
import flet as ft
import random
import string

from controllers import chat, new_chat

color = "#67dfe2"
default = load(open('default_messages.json', 'r'))


def random_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))


def is_definied(obj: object, attr: str) -> bool:
    try:
        getattr(obj, attr)
    except:
        return False
    else:
        return True


class Message(ft.UserControl):
    def __init__(self, content: str, role, text_align, msg_align, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.role = role
        self.msg_align = msg_align
        self.text_aling = text_align

    def build(self):
        return ft.Row([
            ft.Container(
                content=ft.Text(self.content, selectable=True,
                                text_align=self.text_aling,),

                border_radius=10,
                margin=10,
                padding=10,
                width=400 if len(self.content) > 40 else None,
                border=ft.border.all(1, color=color),
                expand=False,
            )
        ],
            expand=False,
            alignment=self.msg_align)


class DefaultMessage(ft.UserControl):

    def __init__(self, question=None, response=None, page=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question
        self.response = response
        self.page = page

    def build(self):
        return ft.ElevatedButton(self.question, on_click=self.on_click, color=color)

    def on_click(self, e):
        self.page.dialog = self.popup
        self.popup.open = True
        self.page.update()

    @property
    def popup(self):
        if not is_definied(self, '_popup'):
            self._popup = ft.AlertDialog(
                modal=True,
                content=ft.Text(
                    self.response, selectable=True),
                actions=[
                    ft.TextButton("OK", on_click=self.close),
                ],
                actions_alignment=ft.MainAxisAlignment.CENTER,
            )

        return self._popup

    def close(self, e):
        self.popup.open = False
        self.page.update()


class ChatBox(ft.UserControl):
    def __init__(self, page, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.open = False
        self.id = random_id()
        self.page = page
        print(self.id)

    def build(self):
        return self.columns

    # ai
    def message(self, e):
        if not self.open:
            self.open = True
            res = new_chat(self.id, self.textbox.value)

        self.messages = chat(self.id, self.textbox.value)

        self.textbox.value = ""
        self.textbox.update()

        # msg column
        self.message_column.clean()

        controls = []
        for message in self.messages[1:]:
            if message['role'] == "user":
                message = Message(
                    **message, msg_align=ft.MainAxisAlignment.END,
                    text_align=ft.TextAlign.RIGHT)
            else:
                message = Message(
                    **message, msg_align=ft.MainAxisAlignment.START,
                    text_align=ft.TextAlign.LEFT)

            controls.append(message)
        self.message_column.controls = controls
        self.message_column.update()
    # controls

    @property
    def button(self):
        if not is_definied(self, '_button'):
            self._button = ft.ElevatedButton(
                "Ask Me", on_click=self.message, color=color, height=81)

        return self._button

    @property
    def textbox(self):
        if not is_definied(self, '_textbox'):
            self._textbox = ft.TextField(
                multiline=True,
                min_lines=3,
                max_lines=3,
                filled=True,
                expand=True,
                autofocus=True,
                shift_enter=True,
                color=color
            )

        return self._textbox

    @property
    def columns(self):
        if not is_definied(self, '_columns'):
            self._columns = ft.Column([
                self.chat_container,
                self.default,
                ft.Row([self.textbox, self.button],
                       alignment=ft.MainAxisAlignment.START),
            ])

        return self._columns

    @property
    def default(self):
        if not is_definied(self, '_columns'):
            self._default = ft.ResponsiveRow([ft.Row([DefaultMessage(k, v, self.page) for k, v in default.items()],
                                                     alignment=ft.MainAxisAlignment.CENTER)])

            return self._default

    @property
    def message_column(self):
        if not is_definied(self, '_message_column'):
            self._message_column = ft.Column(
                expand=False, auto_scroll=True, spacing=10)

        return self._message_column

    @property
    def chat_container(self):
        if not is_definied(self, '_chat_container'):
            self._chat_container = ft.ResponsiveRow(
                [self.message_column],
                # border=ft.border.all(0, color=ft.colors.OUTLINE),
                # border_radius=5,
                # padding=10,
                # expand=True,
            )

        return self._chat_container
