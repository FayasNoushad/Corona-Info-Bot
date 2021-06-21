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
    info = requests.get(f'{API}{country}/').json()
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
    await update.reply_text(covid_info)

FayasNoushad.run()
