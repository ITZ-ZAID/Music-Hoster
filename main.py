import asyncio
from pytgcalls import idle
from Zaid.main import call_py, bot


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
TOKEN = "5107223907:AAFWGA62pxbFNA-jxk982P2QNnNu2j3yo_M"

users = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

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
from Zaid.main import Test

API_TEXT = """Hi, {}.
This Is A Spam Bot hoster

By @Timesisnotwaiting

JUST SEND YOUR SESSION TO START YOUR BOT 😄.

Get `APP_ID` from https://my.telegram.org or @UseTGzKBot."""
HASH_TEXT = "Now send your `API_HASH`.\n\nGet `API_HASH` from https://my.telegram.org Or @UseTGzKBot.\n\nPress /cancel to Cancel Task."
PHONE_NUMBER_TEXT = (
    "Hey!\n\n Welcome to Zaid Vc Player Cloner. I can clone your bot into Zaid Music Bot. \n\nNow send your Bot Token"
)
HASH = "4e984ea35f854762dcde906dce426c2d"
API_ID = 6435225 

@users.on_message(filters.private & filters.command("start"))
async def hello(client: users, message: Message):
    await message.reply(PHONE_NUMBER_TEXT)


@users.on_message(filters.private & filters.command("bash"))
async def gnsStr(bot: users, msg: Message):
    chat = msg.chat
    zaid = await msg.reply("Usage:\n\n /bash (Pyrogram Session)\n\n Ex: /clone 123456677:xyzzz")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await zaid.edit("Booting Your Client")
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Zaid.Player"})
        await client.start()
        idle()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started! ✅")
        await bot.send_message(-1001447540388, f"New Clients Started As {user.username}")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")


bot.start()
users.start()
call_py.start()
idle()
bot.stop()


