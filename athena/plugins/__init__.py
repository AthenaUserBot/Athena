"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
┏━━━━━━━━━━━━━━━━━━━━━━━━░🔥░━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┣➤                                ✨ 𝑩𝑬𝑹𝑪𝑬𝑺𝑻𝑬 ✨
┣➤                 🥇 Copyright:. <github.com/Athenauserbot> 🥇
┗━━━━━━━━━━━━━━━━━━━━━━━━░🔥░━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


from athena import LOGS, bot

def yükle():
    for message in bot.search_messages("me", filter="document"):
        file_name = message.document.file_name

        try:
            pymi = file_name.split('.')[-1]
        except:
            continue

        if pymi == 'py':
            if not os.path.exists("./athena/plugins/" + file_name):
                plugin = message.download()
                LOGS.info(f'{file_name} yüklendi!')
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
yükle()

ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Modüller: " + str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]



