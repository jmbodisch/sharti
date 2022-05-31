# bot.py
import os
import discord
import random
import re
import logging
from discord.utils import get
from dotenv import load_dotenv

# <-- damp suggestions -->
import asyncio
from datetime import datetime, date, time, timezone
from discord.ext import tasks, commands
# <-- damp suggestions -->

load_dotenv()
logging.info('loading DISCORD_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
logging.info('loading DISCORD_GUILD')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
print('Client initiated')

@client.event
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

# <-- damp suggestions -->
@client.event #idk if this needs to be typed again but just want sharti to start running agenda_post whenever they're booted up
async def on_ready():
    print("starting...")
    agenda_post.start()

@tasks.loop(minutes=60.0) # this task should run every hour and check the time and last message sent in the-gay-agenda
async def agenda_post():
    d = datetime.now()
    lm = client.get_channel(750111111092764874).last_message
    if(d.weekday == 6 and lm.author.id == 819220966022185011 and not lm.created_at.weekday == 6): #checks if it's sunday, if there's already a message from sharti, etc
        logging.info('gay agenda time!')
        for i in range(1,8):
            day=''
            # i uhhhh couldnt think of any way to shorten this so yea
            if i == 1:
                day = 'Monday'
            if i == 2:
                day = 'Tuesday'
            if i == 3:
                day = 'Wednesday'
            if i == 4:
                day = 'Thursday'
            if i == 5:
                day = 'Friday'
            if i == 6:
                day = 'Saturday'
            if i == 7:
                day = 'Sunday'

            msg = await client.get_channel(750111111092764874).send('Availability: ' + day + ' ' + '<t:' + str(int(d.replace(day=d.day + i, hour=20, minute=0, second=0, microsecond=0).timestamp())) + '>')
            await msg.add_reaction(u"\U0001F44D")
            await msg.add_reaction(u"\U0001F44E")
            await msg.add_reaction(get(msg.guild.emojis, name="idk")) # copied your code here lol
# <-- damp suggestions -->

client.run(TOKEN)
