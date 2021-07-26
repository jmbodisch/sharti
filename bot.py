# bot.py
import os
import discord
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.name=='the-gay-agenda':
        if not (message.content.startswith('(')):
            await message.add_reaction(u"\U0001F44D")
            await message.add_reaction(u"\U0001F44E")
            await message.add_reaction(get(message.guild.emojis, name="idk"))

client.run(TOKEN)
