import asyncio
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
HOME_TEXT = "👋🏻 **Hi Dude [{}](tg://user?id={})** \n\n🤖 Im **Video Chat Bot**. \n**I Can Stream Lives, Radios, YouTube Videos & Telegram Video Files On Voice Chat Of Telegram Channels & Groups**"
HELP_TEXT = """
🏷️ **Setting Up** :

\u2022 Start a voice chat in your channel or group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Use /stream YouTube link or /stream live stream link or /stream as a reply to an video file.

🏷️ **Common Commands** :

\u2022 `/start` - start the bot
\u2022 `/help` - show help message

🏷️ **Admin Only Commands** :

\u2022 `/radio` - start streaming the radio
\u2022 `/stream` - start streaming the video
\u2022 `/nstream` - stop streaming the video
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("👮 Aᴅᴍɪɴꜱ", callback_data="admins"),
                InlineKeyboardButton("🗨️ Uꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🤬 Rᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton("🗨️ Sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("🤖 Cʟᴏɴᴇʀ", url="t.me/ZaidVcBot"),
            ],
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url=''),
            ],
            [
                InlineKeyboardButton("💌 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/Superior_Support"),
                InlineKeyboardButton("🏷️ Oꜰꜰɪᴄɪᴀʟ Cʜᴀɴɴᴇʟ", url="https://t.me/Superior_bots"),
            ],
            [
                InlineKeyboardButton("🤖 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/Itz-Zaid/Zaid-Vc-Player"),
            ],
            [
                InlineKeyboardButton("🤔 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url=''),
            ],
            [
                InlineKeyboardButton("💌 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/Superior_Support"),
                InlineKeyboardButton("🏷️ Oꜰꜰɪᴄɪᴀʟ Cʜᴀɴɴᴇʟ", url="https://t.me/Superior_bots"),
            ],
            [
                InlineKeyboardButton("🤖 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/Itz-Zaid/Zaid-Vc-Player"),
            ],
            [
                InlineKeyboardButton("🤔 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & filters.private)
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("👮 Aᴅᴍɪɴꜱ", callback_data="admins"),
                InlineKeyboardButton("🗨️ Uꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🤬 Rᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton("🗨️ Sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("🤖 Cʟᴏɴᴇʀ", url="t.me/ZaidVcBot"),
            ],
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
