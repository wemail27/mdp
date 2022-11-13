# (©) AswanthVK 

import os
import asyncio
import requests
import math
import time
from pyrogram import Client, filters
from helper_funcs.helpers import humanbytes, convert
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton


TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5475320054:AAGnT6eMBInj7v5scpjfw1Sw9jF_rwcERj8")

APP_ID = int(os.environ.get("APP_ID", "9411723"))

API_HASH = os.environ.get("API_HASH", "30fa091455c0548d77dc254f0bb705b0")




app = Client("mdisk", bot_token=TG_BOT_TOKEN, api_hash=API_HASH, api_id=APP_ID)

 


@app.on_message(filters.command(['start']))
async def start(client, message):
   await message.reply_photo(
            photo="https://telegra.ph/file/29d3b17cdb209845ce4ef.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\nɪ ᴀᴍ ᴍᴅɪsᴋ ʙʏᴘᴀssᴇʀ ʙᴏᴛ\n\n>> ɪ ᴄᴀɴ ʙʏᴘᴀss ᴀɴʏ ᴍᴅɪsᴋ ʟɪɴᴋ ᴛᴏ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ.\n\n#ɴᴏᴛᴇ sᴇɴᴅ ʟɪɴᴋ ᴏɴᴇ ʙʏ ᴏɴᴇ \n\n ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ @redxtgbots**",reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("🌐 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs", url="https://t.me/redxtgbots")]]), reply_to_message_id=message.message_id)

@app.on_message(filters.command(['help']))
async def help(client, message):
    await message.reply_text(text=f"ʜᴇʏ,\n\nғᴏʟʟᴏᴡ ᴛʜᴇsᴇ sᴛᴇᴘs:  -\n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ 𝟷 ᴍᴅɪsᴋ ʟɪɴᴋ ᴀᴛ ᴀ ᴛɪᴍᴇ ᴀɴᴅ sᴇᴇ ᴍᴀɢɪᴄ ✨\n\nᴍᴀᴅᴇ ʙʏ @AmanReDX", reply_to_message_id=message.message_id)




@app.on_message(filters.private & filters.text)
async def link_extract(bot, message):
    urls = message.text
    
    if not message.text.startswith("https://mdisk.me"):
        await message.reply_text(
            f"**INVALID LINK**",
            reply_to_message_id=message.message_id
        )
        return
    a = await bot.send_message(
            chat_id=message.chat.id,
            text=f"Processing…",
            reply_to_message_id=message.message_id
        )
    inp = urls #input('Enter the Link: ')
    fxl = inp.split("/")
    cid = fxl[-1]
    URL=f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={cid}'
    header = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://mdisk.me/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    resp = requests.get(url=URL, headers=header).json()
    fn = resp['filename']
    dn = resp['display_name']
    dr = resp['duration']
    sz = resp['size']
    ht = resp['height']
    wt = resp['width']
    download = resp['download']
    source = resp['source']
    
    await a.edit_text("**ᴛɪᴛʟᴇ :** {}\n\n**sɪᴢᴇ :** {}\n\n**ᴅᴜʀᴀᴛɪᴏɴ :** {}\n\n**ʀᴇsᴏʟᴜᴛɪᴏɴ :** {}*{}\n\n**ᴜᴘʟᴏᴀᴅᴇʀ :** {}\n\n**💽 ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ (sᴜᴘᴘᴏʀᴛ ᴏɴʟʏ ᴍx ᴘʟᴀʏᴇʀ) :** {}\n\n**🖥️ sᴏᴜʀᴄᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴜʀʟ (ɪғ ᴍxᴠ ᴘʀᴇsᴇɴᴛ ɪɴ ʟɪɴᴋ ᴛʜᴇɴ ɪᴛ sᴜᴘᴘᴏʀᴛ ᴏɴʟʏ ᴍx ᴘʟᴀʏᴇʀ  ɪғ ᴅᴀsʜ, ᴍᴘᴅ, ᴍ𝟹ᴜ𝟾, ʜʟs ᴘʀᴇsᴇɴᴛ ɪɴ ʟɪɴᴋ ᴛʜᴇɴ ɪᴛ sᴜᴘᴘᴏʀᴛ ᴀʟʟ ᴘʟᴀʏᴇʀ) :** {}".format(fn, humanbytes(sz), convert(dr), wt, ht, dn, download, source), disable_web_page_preview=True)
    


app.run()
