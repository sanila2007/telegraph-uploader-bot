# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [telegraph-uploader-bot] (https://github.com/sanila2007/telegraph-uploader-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/telegraph-uploader-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star, fork, enjoy!

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from config import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

INLINE_SELECT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007/telegraph-uploader-bot"),
            InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
        ],
        [
            InlineKeyboardButton("Join Channel🌐", url="https://t.me/telsabots")
        ]
    ]
)

ERROR_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot"),
            InlineKeyboardButton("Learn Bot🙂", url="https://t.me/sanilaassistant_bot")
        ]
    ]
)


@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    text = f"Hello {message.from_user.first_name}!\n\nWelcome to the Telegraph uploader bot.\nYou can send me any " \
           f"image, video, animation and I will upload it to telegraph and send you a generated link. But the file must be LESS THAN 5MB!!\n\n" \
           f"<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>"
    reply_markup = INLINE_SELECT
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True)


## UPLOAD PHOTOS

@bot.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)

        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD VIDEOS

@bot.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="image/jetg")
    try:
        link = upload_file(download_path)
        generated_Link = "https://telegra.ph" + "".join(link)

        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_Link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_Link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD GIF

@bot.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)

        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


##UPLOAD ANIMATIONS TO THE TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.animation)
async def animation_upload_groups(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD PHOTOS TO TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.photo)
async def photo_upload_groups(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## VIDEO UPLOAD TO THE TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.video)
async def video_upload_group(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## STICKER UPLOAD


@bot.on_message(filters.sticker)
async def sticker_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD STICKERS TO TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.sticker)
async def sticker_upload_group(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


print("All good")

bot.run()
