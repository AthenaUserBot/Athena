async def extract_text(message):
    text = message.text.markdown or message.caption.markdown
    if not text:
        return ''
    return text.split()[1] if len(text.split()) > 1 else None
