from os import getpid, system
from subprocess import PIPE, Popen
from sys import exc_info
from time import gmtime, strftime
from traceback import format_exc
from athena.func import to_be_sent

from pyrogram import ContinuePropagation, StopPropagation, filters
from pyrogram.errors import MessageNotModified
from pyrogram.handlers import MessageHandler
from athena import TEMP, BOTLOG, PREFIXES, bot as app



def athena(**args):
    pattern = args.get('pattern', None)
    command = args.get('command', None)
    outgoing = args.get('outgoing', True)
    incoming = args.get('incoming', False)
    noedit = args.get('noedit', False)
    notifyoff = args.get('notifyoff', False)
    compat = args.get('compat', True)
    brain = args.get('brain', False)
    private = args.get('private', True)
    ubot = args.get('bot', True)
    group = args.get('group', True)
    service = args.get('service', False) 

#    if pattern and '.' in pattern[:2]:
#        args['pattern'] = pattern = pattern.replace('.', PREFIX)

    if pattern and pattern[-1:] != '$':
        args['pattern'] = pattern = f'{pattern}(?: |$)(.*)'

    if incoming != False:
        outgoing = False

    def msg_decorator(func):
        global bot
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
                    await message.continue_propagation()

                if not group and 'group' in message.chat.type:
                    if not notifyoff:
                        pass # şimdilik
                    await message.continue_propagation()

                if not compat:
                    await func(client, message)
                else:
                    await func(message)
            except (ContinuePropagation, StopPropagation) as c:
                raise c
            except MessageNotModified:
                return
            except Exception as e:
                gonderilecek = await to_be_sent(message.chat)
                try:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    try:
                        eventtext = message.text or message.caption
                    except:
                        eventtext = 'Probably service message'
                    gusername = str(message.chat.username) if message.chat.username else 'None'
                    text = "==ATHENA HATA RAPORU==\n"
                    text += f"\n⌚ Tarih: {date}\n"
                    text += f"🗒️ Şu yüzden: {eventtext}"

                    ftext = "--------ATHENA ERROR LOG--------\n"
                    ftext += "\n📆 Tarih: " + date
                    ftext += "\n🇫🇲 Grup ID: " + str(message.chat.id)
                    if message.chat.title:
                        ftext += "\n🏷️ Sohbet İsmi: " + str(message.chat.title)
                    ftext += "\n🧠 Grup Username: " + str(gusername)
                    ftext += "\n🐟 Gönderen kişinin ismi:" + str(message.from_user.first_name)
                    ftext += "\n🐟 Gönderen kişinin ID: " + str(message.from_user.id)
                    ftext += "\n\n📃 Olay Tetikleyici:\n"
                    ftext += str(message.text) 
                    ftext += "\n\n🔸 Hata metni:\n"
                    ftext += str(exc_info()[1])
                    ftext += "\n\n\n🔧 Geri izleme bilgisi:\n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------ATHENA ERROR LOG--------"
                    try:
                        with open("error.log", "w+") as errorfile:
                            errorfile.write(ftext)
                        await app.send_document(gonderilecek,'error.log',caption=text)
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

        try:
            if not ubot:
                filter &= ~filters.bot
        except Exception as e:
            print('Error: ',str(e))

        if noedit:
            filter &= ~filters.edited

        app.add_handler(MessageHandler(wrap, filter))

    return msg_decorator


