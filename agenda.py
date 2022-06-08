from discord.ext import tasks, commands
from discord.utils import get
import asyncio
from datetime import datetime, date, time, timezone

class Agenda(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.agenda_post.start()

    @tasks.loop(minutes=60.0) # this task should run every hour and check the time and last message sent in the-gay-agenda
    async def agenda_post(self):
        d = datetime.now()
        lm = self.bot.get_channel(750111111092764874).last_message
        if(d.weekday == 6 and lm.author.id == 819220966022185011 and not lm.created_at.weekday == 6): #checks if it's sunday, if there's already a message from sharti, etc
            print('gay agenda time!')
            for i in range(1,8):
                day=''
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

                msg = await self.bot.get_channel(750111111092764874).send('Availability: ' + day + ' ' + '<t:' + str(int(d.replace(day=d.day + i, hour=20, minute=0, second=0, microsecond=0).timestamp())) + '>')
                await msg.add_reaction(u"\U0001F44D")
                await msg.add_reaction(u"\U0001F44E")
                await msg.add_reaction(get(msg.guild.emojis, name="idk")) # copied your code here lol
        else: 
            print('agenda time hit but conditions not met')