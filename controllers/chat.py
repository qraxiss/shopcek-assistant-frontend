from .helpers import api


def validate_message(message: str):
    if message is None:
        message = ""
    
    return {
        "role": "user",
        "content": message
    }


def new_chat(id: str, message: str ):    
    return api("chat", {
        "id": id,
        "message": validate_message(message)
    }, "post").json()


def get_chat(id: str):
    return api("chat", {
        "id": id
    }, method="get").json()


def chat(id: str, message: str):
    return api("chat/chat", {
        "id": id,
        "message": validate_message(message)
    }, "post").json()
