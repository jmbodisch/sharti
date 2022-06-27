# bot.py
import os
from agenda import Agenda
from dotenv import load_dotenv
from discord.ext import commands
import discord
from bullyengine import BullyEngine
from furrypoll import FurryPoll
from asuka import ItsWednesday

#Environment variables
load_dotenv()
print('loading DISCORD_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
print('loading DISCORD_GUILD')
GUILD = os.getenv('DISCORD_GUILD')
print('loading AGENDA_CHANNEL')
AGENDA_CHANNEL = os.getenv('AGENDA_CHANNEL')
print('loading ANNOUNCE_CHANNEL')
ANNOUNCE_CHANNEL = os.getenv('ANNOUNCE_CHANNEL')

intents = discord.Intents.default()

intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
print('Client initiated')

@bot.event #idk if this needs to be typed again but just want sharti to start running agenda_post whenever they're booted up
async def on_ready():
    print("starting...")
    await bot.add_cog(Agenda(bot, AGENDA_CHANNEL))
    await bot.add_cog(FurryPoll(bot))
    await bot.add_cog(BullyEngine(bot))
    await bot.add_cog(ItsWednesday(bot, ANNOUNCE_CHANNEL))
    
@bot.command(name='hi')
async def greeting(self, ctx):
    print('hit')
    await ctx.channel.send('hello')

bot.run(TOKEN)
