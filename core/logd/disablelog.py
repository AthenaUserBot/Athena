from logging import CRITICAL, DEBUG, INFO, basicConfig, getLogger


def disablelogs(): #thx to teamderuntergang
    pyrogram_syncer = getLogger('pyrogram.syncer')
    pyrogram_syncer.setLevel(CRITICAL)
    pyrogram_session = getLogger('pyrogram.session.session')
    pyrogram_session.setLevel(CRITICAL)
    pyrogram_auth = getLogger('pyrogram.session.auth')
    pyrogram_auth.setLevel(CRITICAL)




