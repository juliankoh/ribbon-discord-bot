import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN_TVL')
VAULT_REFRESH_TIMER = os.getenv('VAULT_REFRESH_TIMER')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    refresh_tvl.start()

@tasks.loop(seconds=float(VAULT_REFRESH_TIMER))
async def refresh_tvl():
    r = requests.get("https://api.llama.fi/tvl/ribbon-finance")
    tvl = round(float(r.text) / 1000000, 1)
    tvlstring = (f"${tvl}m TVL")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=tvlstring))
        
client.run(TOKEN)
