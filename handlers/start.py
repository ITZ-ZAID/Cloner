#Copyright By Itz-Zaid
# @Timesnotwaiting on Telegram!

from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters



@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply("Hey! It's Just a Cloner Bot example source Code")

