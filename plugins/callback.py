from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from modules.config import BOT_USERNAME

HELP_TEXT = """
Hanglo [{}](tg://user?id={})
Saya adalah bot bernama Kiana88 dari generasi terbaru dan tercepat dengan kecanggihan 4.0
My Owner[ðð¦ð±â`ã¡Ï»oÍ¥Î®oÍ£kÍ«roÏ»](https://t.me/depapancake)...
âââââââââââââââââââ**"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("â Tambahkan Saya Ke Group Anda â", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("ð« sá´á´á´á´Êá´", url="https://t.me/troubsnout"),
            InlineKeyboardButton("ð£ á´á´á´á´á´á´s", url="https://t.me/+rktVBMYSOLM4ZmE1")
        ],
        [
            InlineKeyboardButton("ð§° á´á´¡É´á´Ê", url="https://t.me/depadidaw"),
            InlineKeyboardButton("âï¸ á´á´Êá´ ÉªÉ´Òá´", callback_data="moreinfo")
        ]
   
     ]
  ),
)






@Client.on_callback_query(filters.regex("moreinfo"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Êá´Êá´ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Dim Musik untuk Telegram :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¯ï¸ ê±á´á´á´á´Êá´", url=f"https://t.me/troubsnout"),
                    InlineKeyboardButton(
                        "ð á´á´á´á´á´á´ê±", url=f"https://t.me/depadidaw")
                ],
                [
                    InlineKeyboardButton(
                        "ð á´á´ÉªÉ´á´á´ÉªÉ´á´Ê", url="https://t.me/depadidaw"),
                    InlineKeyboardButton(
                        "ð á´á´Êá´Ê ÉªÉ´Òá´", url="https://t.me/depadidaw")
                ],
                [
                    InlineKeyboardButton("â² Êá´á´á´ â³", callback_data="home")
                ]
           ]
        ),
    )



@Client.on_callback_query(filters.regex("cls"))
async def reinfo(_, query: CallbackQuery):
    try:
        await query.message.delete()
        await query.message.reply_to_message.delete()
    except Exception:
        pass


@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Selengkapnya Tentang Saya : 
Saya hanya gabut gaada info lebih lanjut karna Kiana88 sibuk dengan Slot nya WD tiap hari!
.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð É¢á´", url=f"https://t.me/+rktVBMYSOLM4ZmE1"),
                    InlineKeyboardButton(
                        "ð á´Ê", url=f"https://t.me/troubsnout")
                ],
                [
                    InlineKeyboardButton(
                        "ð¾ á´á´¡É´", url="https://t.me/depadidaw"),
                    InlineKeyboardButton(
                        "ð¤¤ á´á´ á´á´¡É´", url="https://t.me/kiana88re")
                ],
                [
                    InlineKeyboardButton("â² Êá´á´á´ â³", callback_data="moreinfo")
                ]
           ]
        ),
     )
    
        
