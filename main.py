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

users = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins={"root": "Zaid.Bot"},
)

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STOPPING BOT & USERBOT")
    await users.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: Starting Cloner")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
