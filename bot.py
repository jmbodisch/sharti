# bot.py
import os
import discord
import random
import re
import logging
from agenda import Agenda
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import tasks, commands

load_dotenv()
logging.info('loading DISCORD_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
logging.info('loading DISCORD_GUILD')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')
print('Client initiated')

@bot.event
async def on_message(message):

    if message.channel.id == 750111111092764874:
        if not re.match("\*{0,2}\(", message.content):
            logging.info('Agenda message found: %s' % message.content )
            await message.add_reaction(u"\U0001F44D")
            await message.add_reaction(u"\U0001F44E")
            await message.add_reaction(get(message.guild.emojis, name="idk"))

    if message.author.id == 309881856898367489: #bully damp
        if message.channel.id != 750594840647172096 and message.channel.id != 828495394194980875:
            if random.randrange(0, 300) == 182:
                logging.info('bullying damp with a lil react')
                await message.add_reaction(u"\U0001F44E")

    if message.author.id == 103637471115382784: #me
        if random.randrange(0, 100) == 50:
            logging.info('plooding for daddy')
            await message.add_reaction(get(message.guild.emojis, name="plooding"))

    if message.content=='hi sharti':
        if message.author.id == 309881856898367489: #bully damp
            logging.info('damp said hi')
            await message.add_reaction(u"\U0001F595")
        else:
            logging.info('someone said hi')
            await message.channel.send('<:babydamp:866167423055691786>')
        if message.author.id == 96284227053551616: #hi knick
            logging.info('knick said hi')
            await message.add_reaction(get(message.guild.emojis, name="goodjob"))

    if message.content=='bye sharti':
        logging.info('someone said bye')
        await message.add_reaction(u"\U0001F44B")

    if message.content=='!furrypoll':
        with open('content/furrypoll.png', 'rb') as f:
            logging.info('furry poll...')
            msg = await message.channel.send(file=discord.File(f))
            await msg.add_reaction(u"\U0001F44D")
            await msg.add_reaction(u"\U00002665")
            await msg.add_reaction(u"\U0001F62E")
            await msg.add_reaction(u"\U0001F622")

@bot.event #idk if this needs to be typed again but just want sharti to start running agenda_post whenever they're booted up
async def on_ready():
    print("starting...")
    bot.add_cog(Agenda(bot))
    
bot.run(TOKEN)
