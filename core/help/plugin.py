from athena import bot as app
import os

def tg_userbotinstaller():
    for message in app.search_messages("me", filter="document"):
        file_name = message.document.file_name

        try:
            pymi = file_name.split('.')[-1]
        except:
            continue

        if pymi == 'py':
            if not os.path.exists("./athena/plugins/extra/" + file_name):
                plugin = app.download_media(message,f"./athena/plugins/extra/{file_name}")
                print(f'{file_name} yüklendi!')
            else:
                print(f'{file_name} atlandı!')
#                pass # Şimdilik
