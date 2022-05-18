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


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
)
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
from Zaid.main import bot, call_py, Test

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

API_TEXT = """Hi, {}.
This Is A Spam Bot hoster

By @Timesisnotwaiting

JUST SEND YOUR SESSION TO START YOUR BOT 😄.

Get `APP_ID` from https://my.telegram.org or @UseTGzKBot."""
HASH_TEXT = "Now send your `API_HASH`.\n\nGet `API_HASH` from https://my.telegram.org Or @UseTGzKBot.\n\nPress /cancel to Cancel Task."
PHONE_NUMBER_TEXT = (
    "Hey!\n\nThis Is Zaid Music Cloner, I Can Host Your Bot On My Server And Vars..\n\nNow Send /clone {Bot token} from @botfather"
)
HASH = "4e984ea35f854762dcde906dce426c2d"
API_ID = 6435225 


import re
import sys
import subprocess
import traceback

from time import time
from io import StringIO
from inspect import getfullargspec

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@bot.on_message(filters.command(["eval"]) & ~filters.edited & filters.user(SUDO_USERS))
async def executor(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="» Give a command to execute")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    t1 = time()
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "SUCCESS"
    final_output = f"`OUTPUT:`\n\n```{evaluation.strip()}```"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳", callback_data=f"runtime {t2-t1} seconds"
                    )
                ]
            ]
        )
        await message.reply_document(
            document=filename,
            caption=f"`INPUT:`\n`{cmd[0:980]}`\n\n`OUTPUT:`\n`attached document`",
            quote=False,
            reply_markup=keyboard,
        )
        await message.delete()
        remove_if_exists(filename)
    else:
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"runtime {round(t2-t1, 3)} seconds",
                    )
                ]
            ]
        )
        await edit_or_reply(message, text=final_output, reply_markup=keyboard)


@bot.on_callback_query(filters.regex(r"runtime"))
async def runtime_func_cq(_, cq):
    runtime = cq.data.split(None, 1)[1]
    await cq.answer(runtime, show_alert=True)


@bot.on_message(filters.command(["sh"]) & ~filters.edited & filters.user(SUDO_USERS))
async def shellrunner(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="**usage:**\n\n» /sh echo hello world")
    text = message.text.split(None, 1)[1]
    if "\n" in text:
        code = text.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except Exception as err:
                print(err)
                await edit_or_reply(message, text=f"`ERROR:`\n\n```{err}```")
            output += f"**{code}**\n"
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", text)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as err:
            print(err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            return await edit_or_reply(
                message, text=f"`ERROR:`\n\n```{''.join(errors)}```"
            )
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await bot.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.message_id,
                caption="`OUTPUT`",
            )
            return remove_if_exists("output.txt")
        await edit_or_reply(message, text=f"`OUTPUT:`\n\n```{output}```")
    else:
        await edit_or_reply(message, text="`OUTPUT:`\n\n`no output`")


@users.on_message(filters.private & filters.command("start"))
async def hello(client: users, message: Message):
    await message.reply(PHONE_NUMBER_TEXT)


@users.on_message(filters.private & filters.command("bash"))
async def gnsStr(bot: users, msg: Message):
    chat = msg.chat
    zaid = await msg.reply("Usage:\n\n /bash (Pyrogram Session)")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await zaid.edit("Booting Your Client")
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Zaid.Player"})
        await client.start()
        idle()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @ZaidVcPlayer To Your Chat!\n\nThanks for Cloning.")
        await bot.send_message(-1001447540388, f"New Clients Started As @{user.username}")
        okie = await Test.get_chat(user.id)
        await Test.send_message(okie, "/start")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

bot.start()
call_py.start()
users.start()
idle()
bot.stop()
