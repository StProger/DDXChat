from app.chats.models import Chats

def choose_dialogs_user(user_id: int, dialogs: list[Chats]):

    output_dialogs = []
    for dialog in dialogs:

        if dialog.first_user_id == user_id:

            output_dialogs.append(dialog.second_user_id)
        else:

            output_dialogs.append(dialog.first_user_id)

    return output_dialogs
