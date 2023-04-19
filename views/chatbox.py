import flet as ft
import random
import string

from controllers import chat, new_chat

color = "#67dfe2"

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
    def __init__(self, content: str, role, msg_align, text_align, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.role = role
        self.msg_align = msg_align
        self.text_aling = text_align

    # @property
    # def border(self):
    #     return ft.Border(*[ft.BorderSide(1) for i in range(4)])

    def build(self):
        return ft.Container(
            content=ft.Text(self.content, text_align=self.text_aling),
            margin=10,
            padding=10,
            alignment=self.msg_align,
            # width=150,
            # height=150,
            border_radius=10,
            border=ft.border.all(1, color=ft.colors.OUTLINE),
        )


class ChatBox(ft.UserControl):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.open = False
        self.id = random_id()
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
                    **message, msg_align=ft.alignment.center_right,
                    text_align=ft.TextAlign.RIGHT)
            else:
                message = Message(
                    **message, msg_align=ft.alignment.center_left,
                    text_align=ft.TextAlign.LEFT)

            controls.append(message)
        self.message_column.controls = controls
        self.message_column.update()

    # controls

    @property
    def button(self):
        if not is_definied(self, '_button'):
            self._button = ft.TextButton("Ask Me", on_click=self.message)

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
                ft.Row([self.textbox, self.button],
                       alignment=ft.MainAxisAlignment.START),
            ])

        return self._columns

    @property
    def message_column(self):
        if not is_definied(self, '_message_column'):
            self._message_column = ft.ListView(expand=False, auto_scroll=True, spacing=10)

        return self._message_column

    @property
    def chat_container(self):
        if not is_definied(self, '_chat_container'):
            self._chat_container = ft.Container(
                content=self.message_column,
                # border=ft.border.all(0, color=ft.colors.OUTLINE),
                # border_radius=5,
                padding=10,
                expand=False,
            )

        return self._chat_container
