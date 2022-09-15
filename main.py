from config import SUDO_USERS
SUDO_USERS = SUDO_USERS
import asyncio
from pytgcalls import idle

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
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from Zaid.main import bot, call_py, Test

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d"
TOKEN = "5107223907:AAFWGA62pxbFNA-jxk982P2QNnNu2j3yo_M"

users = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


PHONE_NUMBER_TEXT = (
    "Hey!\n\nThis Is Zaid Music Cloner, I Can Host Your Bot On My Server And Vars..\n\nNow Send /clone {Bot token} from @botfather"
)



@users.on_message(filters.private & filters.command("start"))
async def hello(client: users, message: Message):
    await message.reply(PHONE_NUMBER_TEXT)


@users.on_message(filters.private & filters.command("clone"))
async def gnsStr(bot: users, msg: Message):
    chat = msg.chat
    zaid = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await zaid.edit("Booting Your Client")
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Zaid.Player"})
        await client.start()
        idle()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started! ✅\n\nName: {user.first_name}\nBot Username: @{user.username}\nBot id: {user.id}\nAssistant: @ClonedXyz\n\n\nThanks for cloning, Now you can add your bot and Assistant to your chat.")
        await bot.send_message(-1001503451387, f"New Clients Started As @{user.username}")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

bot.start()
call_py.start()
users.start()
idle()
bot.stop()
