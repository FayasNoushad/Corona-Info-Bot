import os
import requests
from pyrogram import Client, filters

FayasNoushad = Client(
    "Corona-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://api.sumanjay.cf/covid/covid/?country="

@FayasNoushad.on_message(filters.private & filters.text)
async def covid_info(bot, update):
    country = update.text.replace(" ", "+")
    info = requests.get(API + country).json()
    covid_info = f"""
--**Covid 19 Information**--

Country : {info['country']}
Actived : {info['active']}
Confirmed : {info['confirmed']}
Deaths : {info['deaths']}
Id : {info['id']}
Last Update : {info['last_update']}
Latitude : {info['latitude']}
Longitude : {info['longitude']}
Recovered : {info['recovered']}

Made by @FayasNoushad
"""
    await update.reply_text(covid_info)

FayasNoushad.run()
