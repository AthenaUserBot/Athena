async def extract_text(message):
    text = message.text.markdown or message.caption.markdown
    if not text:
        return ''
    return text.split()[1] if len(text.split()) > 1 else None

async def to_be_sent(chat):
    from athena import BOTLOG
    return BOTLOG if BOTLOG else chat.id
