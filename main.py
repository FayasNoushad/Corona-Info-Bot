import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Corona-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.text)
async def covid_info(bot, update):
    try:
        country = update.text.replace(" ", "+")
        r = requests.get(API + country)
        info = r.json()
        country = info['country']
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""
--**Covid 19 Information**--

Country : {country}
Actived : {active}
Confirmed : {confirmed}
Deaths : {deaths}
Id : {info_id}
Last Update : {last_update}
Latitude : {latitude}
Longitude : {longitude}
Recovered : {recovered}

Made by @FayasNoushad
"""
        await update.reply_text(
            text=covid_info,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )

FayasNoushad.run()
