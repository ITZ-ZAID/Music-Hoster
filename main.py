import asyncio
from pytgcalls import idle
from Zaid.main import call_py, bot

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


import asyncio
import os
import time
from pyromod import listen
from asyncio.exceptions import TimeoutError
import logging
from pyrogram import *
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
)
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
TOKEN = "5258584227:AAHVgoO8bJj4QilPN8J7EWwp9Po83bEaDjM"

users = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

API_TEXT = """Hi, {}.
This Is A Spam Bot hoster 

By @Timesisnotwaiting

JUST SEND YOUR SESSION TO START YOUR BOT 😄.

Get `APP_ID` from https://my.telegram.org or @UseTGzKBot."""
HASH_TEXT = "Now send your `API_HASH`.\n\nGet `API_HASH` from https://my.telegram.org Or @UseTGzKBot.\n\nPress /cancel to Cancel Task."
PHONE_NUMBER_TEXT = (
    "Now send your PyroGram String Session"
)
HASH = "4e984ea35f854762dcde906dce426c2d"
API_ID = 6435225

@users.on_message(filters.private & filters.command("start"))
async def genStr(bot: users, msg: Message):
    chat = msg.chat
    while True:
        number = await bot.ask(chat.id, PHONE_NUMBER_TEXT)
        if not number.text:
            continue
        phone = number.text
        confirm = await bot.ask(chat.id, f'`Is "{phone}" correct? (y/n):` \n\nSend: `y` (If Yes)\nSend: `n` (If No)')
        if "y" in confirm.text:
            break
    try:
        Zaid = await bot.send_message(chat.id, f"Booting Your Client")
        client = Client(session_name= phone, api_id=API_ID, api_hash=HASH, plugins=dict(root="handlers"))
        await client.start()
        idle()
        await bot.send_message(chat.id, f"Your Client Has Been Successfully Started! ✅")
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
        pass

users.run()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
