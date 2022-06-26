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
async def clone(bot: ZAID, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "handlers"})
        await client.start()
        idle()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @Amala_music_assistant_1 To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

ZAID.start()
idle()
