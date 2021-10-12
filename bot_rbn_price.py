import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI

load_dotenv()

try:
    TOKEN = os.getenv('DISCORD_TOKEN_RBN')
    PRICE_REFRESH_TIMER = os.getenv('PRICE_REFRESH_TIMER')
except:
    TOKEN = os.environ('DISCORD_TOKEN_RBN')
    PRICE_REFRESH_TIMER = os.environ('PRICE_REFRESH_TIMER')

cg = CoinGeckoAPI()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    refresh_price.start()

@tasks.loop(seconds=float(PRICE_REFRESH_TIMER))
async def refresh_price():

    token = "ribbon-finance"
    res = cg.get_price(ids=token, vs_currencies='usd', include_24hr_change='true')
    
    price = f"${res[token]['usd']} USD"
    change = f"{res[token]['usd_24h_change']:+.2f}%"
    print("Price: {} Change {}".format(price, change))
    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=change))
    for guild in client.guilds:
        await guild.me.edit(nick=price)

client.run(TOKEN)