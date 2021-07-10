"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
┏━━━━━━━━━━━━━━━━━━━━━━━━░🔥░━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┣➤                                ✨ 𝑩𝑬𝑹𝑪𝑬𝑺𝑻𝑬 ✨
┣➤ 🥇 Thank you TeamDerUntergang who contributed to the file. <github.com/TeamDerUntergang> 🥇
┗━━━━━━━━━━━━━━━━━━━━━━━━░🔥░━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

from os import getpid, system
from subprocess import PIPE, Popen
from sys import exc_info
from time import gmtime, strftime
from traceback import format_exc

from pyrogram import ContinuePropagation, StopPropagation, filters
from pyrogram.errors import MessageNotModified
from pyrogram.handlers import MessageHandler
from athena import TEMP, BOTLOG, PREFIXES, bot as app



def muinrobot(**args):
    pattern = args.get('pattern', None)
    outgoing = args.get('outgoing', True)
    incoming = args.get('incoming', False)
    noedit = args.get('noedit', False)
    notifyoff = args.get('notifyoff', False)
    compat = args.get('compat', True)
    brain = args.get('brain', False)
    private = args.get('private', True)
    group = args.get('group', True)
    bots = args.get('bots', False)
    service = args.get('service', False) 

#    if pattern and '.' in pattern[:2]:
#        args['pattern'] = pattern = pattern.replace('.', PREFIX)

    if pattern and pattern[-1:] != '$':
        args['pattern'] = pattern = f'{pattern}(?: |$)'

    def msg_decorator(func):
        async def wrap(client, message):
            if message.empty or not message.from_user:
                return

            try:
                if 'ME' not in TEMP:
                    me = await app.get_me()
                    TEMP['ME'] = me

                if not private and message.chat.type in ['private', 'bot']:
                    if not notifyoff:
                        pass # şimdilik
                    message.continue_propagation()

                if not group and 'group' in message.chat.type:
                    if not notifyoff:
                        pass # şimdilik
                    message.continue_propagation()

                if not compat:
                    func(client, message)
                else:
                    func(message)
            except (ContinuePropagation, StopPropagation) as c:
                raise c
            except MessageNotModified:
                return
            except Exception as e:
                try:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    try:
                        eventtext = message.text or message.caption
                    except:
                        eventtext = 'Probably service message'
                    gusername = str(message.chat.username) if message.chat.username else 'None'
                    text = "<b>==ATHENA HATA RAPORU==</b>\n"
                    text += f"\n<b>⌚ Tarih:</b> {date}\n"
                    text += f"<b>🗒️ Şu yüzden:</b> {eventtext}"

                    ftext = "<b>" + "--------ATHENA ERROR LOG--------\n" + "</b>"
                    ftext += "\n<b>📆 Tarih:</b> " + f"<i>{date}</i>"
                    ftext += "\n🇫🇲 <b>Grup ID:</b> " + f"<i>{str(message.chat.id)}</i>"
                    if message.chat.title:
                        ftext += "\n🏷️ <b>Sohbet İsmi</b>: " + f"<i>{str(message.chat.title)}</i>"
                    ftext += "\n🧠 <b>Grup Username:</b> " + f"{str(gusername)}"
                    ftext += "\n🐟 <b>Gönderen kişinin ismi:</b>" + f"<i>{str(message.from_user.first_name)}</i>"
                    ftext += "\n🐟 <b>Gönderen kişinin ID: </b>" + f"<i>{str(message.from_user.id)}</i>"
                    ftext += "\n\n📃 <b>Olay Tetikleyici:</b>\n"
                    ftext += "<i>" + str(message.text) + "</i>"
                    ftext += "\n\n🔸 <b>Hata metni:</b>\n"
                    ftext += "<i>" + str(exc_info()[1]) + "</i>"
                    ftext += "\n\n\n🔧 <b>Geri izleme bilgisi:</b>\n"
                    ftext += "<i>" + str(format_exc()) + "</i>"
                    ftext += "\n\n<b>--------ATHENA ERROR LOG--------" + "</b>"
                    try:
                        with open("error.log", "w+") as errorfile:
                            errorfile.write(ftext)
                        await app.send_document(BOTLOG,'error.log',caption=text)
                        remove('error.log')
                    except:
                        print(ftext)
                except Exception as x:
                    raise x

        filter = ~filters.channel
        if pattern:
            filter &= filters.regex(pattern)
            if outgoing and not incoming:
                filter &= filters.me
            elif incoming and not outgoing:
                filter &= filters.incoming & ~filters.me
                bot = False
        elif command:
            filter &= filters.command(commands=command,prefixes=PREFIXES,case_sensitive=True)
            if outgoing and not incoming:
                filter &= filters.me
            elif incoming and not outgoing:
                filter &= filters.incoming & ~filters.me
                bot = False
        else:
            if outgoing and not incoming:
                filter &= filters.me
            elif incoming and not outgoing:
                filter &= filters.incoming & ~filters.me
                bot = False
            else:
                filter &= (filters.me | filters.incoming)



        ####     Extras    ####

#        if brain:
#            filter &= filters.user(BRAIN)

        if not bots:
            filter &= ~filters.bot

        if noedit:
            filter &= ~filters.edited

        app.add_handler(MessageHandler(wrap, filter))

    return msg_decorator


