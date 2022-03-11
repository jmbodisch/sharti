# bot.py
import os
import discord
import random
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):

    if message.channel.id == 750111111092764874:
        if not (message.content.startswith('(')):
            await message.add_reaction(u"\U0001F44D")
            await message.add_reaction(u"\U0001F44E")
            await message.add_reaction(get(message.guild.emojis, name="idk"))

    if message.author.id == 309881856898367489: #bully damp
        if message.channel.id != 750594840647172096 and message.channel.id != 828495394194980875:
            if random.randrange(0, 300) == 182:
                await message.add_reaction(u"\U0001F44E")

    if message.author.id == 103637471115382784: #me
        if random.randrange(0, 100) == 50:
            await message.add_reaction(get(message.guild.emojis, name="plooding"))

    if message.content=='hi sharti':
        if message.author.id == 309881856898367489: #bully damp
            await message.add_reaction(u"\U0001F595")
        else:
            await message.channel.send('<:babydamp:866167423055691786>')
        if message.author.id == 96284227053551616: #hi knick
            await message.add_reaction(get(message.guild.emojis, name="goodjob"))

    if message.content=='bye sharti':
        await message.add_reaction(u"\U0001F44B")

    if message.content=='!furrypoll':
        with open('content/furrypoll.png', 'rb') as f:
            msg = await message.channel.send(file=discord.File(f))
            await msg.add_reaction(u"\U0001F44D")
            await msg.add_reaction(u"\U00002665")
            await msg.add_reaction(u"\U0001F62E")
            await msg.add_reaction(u"\U0001F622")

client.run(TOKEN)
