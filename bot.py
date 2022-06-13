# bot.py
import os
from agenda import Agenda
from dotenv import load_dotenv
from discord.ext import commands
from bullyengine import BullyEngine
from furrypoll import FurryPoll

#Environment variables
load_dotenv()
print('loading DISCORD_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
print('loading DISCORD_GUILD')
GUILD = os.getenv('DISCORD_GUILD')
print('loading AGENDA_CHANNEL')
AGENDA_CHANNEL = os.getenv('AGENDA_CHANNEL')

bot = commands.Bot(command_prefix='$')
print('Client initiated')

@bot.event #idk if this needs to be typed again but just want sharti to start running agenda_post whenever they're booted up
async def on_ready():
    print("starting...")
    bot.add_cog(Agenda(bot))
    bot.add_cog(FurryPoll(bot))
    bot.add_cog(BullyEngine(bot))
    
bot.run(TOKEN)
