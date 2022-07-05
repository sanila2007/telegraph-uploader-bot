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

LANGUAGE_SELECT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Github", url="https://github.com/sanila2007/telegraph-uploader-bot"),
            InlineKeyboardButton("Report Bugs", url="https://t.me/sanilaassistant_bot")
        ]
    ]
)


@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    text = f"Hello {message.from_user.first_name}\n\nWelcome to the Telegraph uploader bot.\nYou can send me any " \
           f"image, video, animation and I will upload it to telegraph and send you a generated link. But the file must be LESS THAN 5MB!!\n\n" \
           f"To get project updates and new features <a href=https://github.com/sanila2007>FOLLOW ME ON GITHUB</a>\n" \
           f"Leave me a feedback about this bot <a href=https://t.me/sanilaassistant_bot>by clicking this...</a>"
    reply_markup = LANGUAGE_SELECT
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True)


@bot.on_message(filters.photo)
async def photo_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://github.com/sanila2007/telegraph-uploader-bot>learn from Github</a>",
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://github.com/sanila2007>FOLLOW ME on Github to get more bot updates</a>",
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


@bot.on_message(filters.video)
async def video_uploa(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="image/jetg")
    try:
        link = upload_file(download_path)
        generated_Link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://github.com/sanila2007/telegraph-uploader-bot>learn from Github</a>",
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_Link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://github.com/sanila2007>FOLLOW ME on Github to get more bot updates</a>",
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


@bot.on_message(filters.animation)
async def animation_uploa(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="image/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://github.com/sanila2007/telegraph-uploader-bot>learn from Github</a>",
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://github.com/sanila2007>FOLLOW ME on Github to get more bot updates</a>",
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


print("All good")

bot.run()
