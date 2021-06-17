import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN_TVL')
VAULT_REFRESH_TIMER = os.getenv('VAULT_REFRESH_TIMER')

client = discord.Client()

def get_tvl():
    r = requests.get("https://api.llama.fi/tvl/ribbon-finance")
    tvl = round(float(r.text) / 1000000, 1)
    tvlstring = (f"${tvl}m TVL")
    return tvlstring

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    refresh_tvl.start()

@tasks.loop(seconds=float(VAULT_REFRESH_TIMER))
async def refresh_tvl():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=get_tvl()))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$tvl'):
        tvl = get_tvl()
        await message.channel.send(tvl)
        
client.run(TOKEN)
