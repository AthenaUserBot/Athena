from athena import bot as app
import os

def tg_userbotinstaller():
    for message in app.iter_history("me"):
        if message.document:
            ret_msg = message.document
        else:
            continue
        file_name = ret_msg.file_name
        if (len(file_name.split('.')) > 1) \
            and plugin.file.name.split('.')[-1] == 'py':

            if not os.path.exists("./athena/plugins/extra/" + file_name):
                plugin = message.download()
            else:
                pass # Şimdilik
