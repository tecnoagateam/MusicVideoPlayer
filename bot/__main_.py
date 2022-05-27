# ===========
# running bot
# ===========

import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from bot.videoplayer import app
from player.videoplayer import call_py

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot"),
)

bot.start()
print("[INFO]: BOT BAŞLADI")
app.start()
print("[INFO]: ASSİSTANT BAŞLADI")
call_py.start()
print("[INFO]: PY-TGCALLS BAŞLADI")
idle()
print("[INFO]: BOT STOP EDİLDİ")
