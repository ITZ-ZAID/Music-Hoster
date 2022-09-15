## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC_mO0iEEwi6LYmVh9O2CyI0SsxV2yYwjNVo-PinFiSk9G8OkV0r4h3TxUk6O1X0NFOnfEF7dtS6g8JIRrU7oAcDcgnwwwsLWgWuBpSxCCwDisLDulFDlMKTeYK2xAuoeRrkOmGfQH6EAz-AMkiVk4gYuTF4SXESv1Un2bHtUiaHWPZ23ulBwCjzCbQKFYUVG88-8t7Ji_Dxian_BZTdaTmTwHpDipxIxTjwxW0-_71NmN3Nce1XjlOjpWyFh8d-zZpKP6vYUI0zFawMQegeJs3a3WP8qZUDRoHUOT9-cRcDpWXgUbUGUn9Ce-vh5W2L8X4ec4dPlcgWJFPwyiThfIBAAAAATNByrMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5305247875:AAEtmpmCAizvAA2n2ZsXP6DnEKWd47uV11k")
BOT_NAME = getenv("BOT_NAME", "ZaidXHoster")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "Zaid2_Robot")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ZaidVcPlayer")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
