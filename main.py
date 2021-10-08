# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad) (@BXBotz)

import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Glitch-Art-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """
**Hai {}, 

Iam A Simple photo to glitch art telegram bot. Send me any photo I will convert photo to glitch art

Made With ❤ By @BX_Botz**
"""

SOURCE_TEXT = """<b>🎁 MY Source Code</b>"""

START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Updates Channel', url='https://telegram.me/BX_Botz'),
        InlineKeyboardButton('Support Group', url='https://telegram.me/BXSupport')
    ],
    [
        InlineKeyboardButton('Other Bots', url='https://telegram.me/BX_Botz/31')
    ]]
)


PATH = os.environ.get("PATH", "./DOWNLOADS")

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )




@Bot.on_message(filters.private & filters.photo)
async def glitch_art(bot, update):
    download_path = PATH + "/" + str(update.from_user.id) + "/"
    download_location = download_path + "photo.jpg"
    message = await update.reply_text(
        text="`Processing...`",
        quote=True
    )
    try:
        await update.download(
            file_name=download_location
        )
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\n\nContact My [Support Group](https://t.me/BXSupport) "
        )
        return 
    await message.edit_text(
        text="`🎨 Converting to glitch...`"
    )
    try:
        glitch_art = glitchart.jpeg(download_location)
        await update.reply_photo(photo=glitch_art, quote=True)
        os.remove(download_location)
        os.remove(glitch_art)
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\n\nContact My [Support Group](https://t.me/BXSupport)"
        )
        return
    await message.delete()


Bot.run()
