import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN_ETH_PRICE')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)
