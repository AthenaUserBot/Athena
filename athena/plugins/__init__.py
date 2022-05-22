from os import path
from athena import LOGS, bot

def yükle():
    global ALL_MODULES
    for message in bot.search_messages("me", filter="document"):
        file_name = message.document.file_name

        try:
            pymi = file_name.split('.')[-1]
        except:
            continue
        dizin = "./athena/plugins/" + file_name
        if pymi == 'py':
            if not path.exists(dizin):
                plugin = bot.download_media(message,file_name=dizin)
                ALL_MODULES.append(file_name.replace(".py",""))
            else:
                LOGS.warning(f'{file_name} atlandı!')
#                pass # Şimdilik


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules

bot.start()

ALL_MODULES = sorted(__list_all_modules())

yükle()

LOGS.info("Modüller: " + str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]



