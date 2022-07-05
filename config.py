# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [telegraph-uploader-bot] (https://github.com/sanila2007/telegraph-uploader-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/telegraph-uploader-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star, fork, enjoy!


import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345678))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
