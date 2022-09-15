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

from helpers import is_session_in_db, add_session, get_all_session

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
        if await is_session_in_db(phone):
           return await zaid.edit("This Client Is already present in my Database!!\n\nExiting..")
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Zaid.Player"})
        await client.start()
        idle()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started! ✅\n\nName: {user.first_name}\nBot Username: @{user.username}\nBot id: {user.id}\nAssistant: @ClonedXyz\n\n\nThanks for cloning, Now you can add your bot and Assistant to your chat.")
        await bot.send_message(-1001503451387, f"New Clients Started As @{user.username}")
        await add_session(user.id, phone)
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")



async def start_bot():
    print("[INFO]: LOADING ASSISTANT DETAILS")
    await bot.start()
    await users.start()
    await call_py.start()
    string = await get_all_session()
    for i in string:
        try:
            pyroman = Client(session_name=f"{i['string']}", api_id=6435225, api_hash="4e984ea35f854762dcde906dce426c2d", plugins=dict(root=f"Zaid.Player"))
            await pyroman.start()
            user = await pyroman.get_me()
            print(f"[INFO]: Started {user.first_name}")
        except BaseException as eb:
            print(eb)
    print(f"Total Client = {len(string)} User")
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

