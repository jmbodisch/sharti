import datetime
import asyncio
from discord.ext import commands, tasks
import discord
from  random import randint

ihop_frequency = 12
#^^ 1/ihop_frequency chance to put the ihop asuka dies
#instead of the normal feliz jueves 

class ItsWednesday(commands.Cog):
    def __init__(self, bot, AnnounceChannel):
        self.bot = bot
        self.channelPlace = int(AnnounceChannel)
        self.LikeToCall.start()

    def cog_unload(self):
        self.LikeToCall.cancel()

    @tasks.loop(minutes = 1)
    async def LikeToCall(self):
        t = datetime.datetime.now()
        wkd = datetime.datetime.weekday(t)
        #monday is zero apparently!

        if(wkd == 4):
            if(t.hour == 9 and t.minute == 0):
                await self.bot.get_channel(self.channelPlace).send("https://va.media.tumblr.com/tumblr_qep9sc7Ukp1wwpg7e.mp4")
                print("Sent flatworm friday")

        if(wkd == 2):
            if(t.hour == 23 and t.minute == 58):
                await self.bot.get_channel(self.channelPlace).send("It's Wednesday")
            elif(t.hour == 23 and t.minute == 59):
                await self.bot.get_channel(self.channelPlace).send("or as I like to call it,")
        elif(wkd == 3):
            if(t.hour == 0 and t.minute == 0):
                await self.bot.get_channel(self.channelPlace).send("Thursday")
                if(randint(1,ihop_frequency) == 1):
                    await self.bot.get_channel(self.channelPlace).send("https://cdn.discordapp.com/attachments/730266935912300634/990141376266121256/87_degrees_results_meme.mp4")
                else:
                    await self.bot.get_channel(self.channelPlace).send("https://cdn.discordapp.com/attachments/787188953539280906/989609455538831430/Feliz_Jueves.mp4")
                print("jueves felizd")
