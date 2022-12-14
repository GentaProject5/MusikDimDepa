from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from modules.config import BOT_USERNAME

HELP_TEXT = """
Hanglo [{}](tg://user?id={})
Saya adalah bot bernama Kiana88 dari generasi terbaru dan tercepat dengan kecanggihan 4.0
My Owner[𝘋𝘦𝘱⋏`メϻoͥήoͣkͫroϻ](https://t.me/depapancake)...
━━━━━━━━━━━━━━━━━━━**"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ Tambahkan Saya Ke Group Anda ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🫂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/troubsnout"),
            InlineKeyboardButton("📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/+rktVBMYSOLM4ZmE1")
        ],
        [
            InlineKeyboardButton("🧰 ᴏᴡɴᴇʀ", url="https://t.me/depadidaw"),
            InlineKeyboardButton("⚕️ ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo")
        ]
   
     ]
  ),
)






@Client.on_callback_query(filters.regex("moreinfo"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Dim Musik untuk Telegram :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/troubsnout"),
                    InlineKeyboardButton(
                        "🌐 ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/depadidaw")
                ],
                [
                    InlineKeyboardButton(
                        "🍄 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/depadidaw"),
                    InlineKeyboardButton(
                        "🍀 ᴏᴛʜᴇʀ ɪɴғᴏ", url="https://t.me/depadidaw")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
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
                        "🔗 ɢᴄ", url=f"https://t.me/+rktVBMYSOLM4ZmE1"),
                    InlineKeyboardButton(
                        "💌 ᴄʜ", url=f"https://t.me/troubsnout")
                ],
                [
                    InlineKeyboardButton(
                        "👾 ᴏᴡɴ", url="https://t.me/depadidaw"),
                    InlineKeyboardButton(
                        "🤤 ᴄᴏ ᴏᴡɴ", url="https://t.me/kiana88re")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="moreinfo")
                ]
           ]
        ),
     )
    
        
