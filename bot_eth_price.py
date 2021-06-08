import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN_ETH_PRICE')
PRICE_REFRESH_TIMER = os.getenv('PRICE_REFRESH_TIMER')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    refresh_price.start()

@tasks.loop(seconds=float(PRICE_REFRESH_TIMER))
async def refresh_price():
    cg = CoinGeckoAPI()
    res = cg.get_price(ids='ethereum', vs_currencies='usd')
    price = f"${res['ethereum']['usd']}"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=price))

client.run(TOKEN)
