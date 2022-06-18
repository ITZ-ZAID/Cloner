import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *

os.system("apt install git curl python3-pip ffmpeg -y")


API_ID = ""
API_HASH = ""
TOKEN = ""

ZAID = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


@ZAID.on_message(filters.private & filters.command("start"))
async def hello(client: ZAID, message: Message):
    await message.reply("Hey! It's Just a Cloner Bot example source Code")


@ZAID.on_message(filters.private & filters.command("clone"))
async def gnsStr(bot: ZAID, msg: Message):
    """Command format will be /clone <repo> <clone as> <ccloned Directry> <start command>"""
    chat = msg.chat
    zaid = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    repo = msg.command[1]
    extract = msg.command[2]
    bash = msg.command[4]
    try:
        await zaid.edit("Cloning Your Codes")
        os.system(f"git clone {repo + extract}")
        os.system(f"cd {extract}")
        os.system(f"python3 {bash}")   
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

ZAID.start()
idle()
