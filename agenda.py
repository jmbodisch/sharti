import re
from discord.ext import tasks, commands
from discord.utils import get
from datetime import datetime, date, time, timezone

class Agenda(commands.Cog):
    def __init__(self, bot, agendaChannel):
        self.lastAgenda = None
        self.agendaChannel = int(agendaChannel)
        self.bot = bot
        self.agenda_post.start()

    @tasks.loop(minutes=60.0) # this task should run every hour and check the time and last message sent in the-gay-agenda
    async def agenda_post(self):
        d = datetime.now()
        print('Agenda task running at ', d.isoformat())
        
        if((self.lastAgenda is None or(d-self.lastAgenda).days > 6) and d.weekday() == 6 ): 
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

                msg = await self.bot.get_channel(self.agendaChannel).send('Availability: ' + day + ' ' + '<t:' + str(int(d.replace(day=d.day + i, hour=20, minute=0, second=0, microsecond=0).timestamp())) + '>')

                self.lastAgenda = datetime.now()
        else: 
            print('agenda time hit but conditions not met')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == self.agendaChannel:
            if not re.match("\*{0,2}\(", message.content):
                print('Agenda message found: %s' % message.content )
                await message.add_reaction(u"\U0001F44D")
                await message.add_reaction(u"\U0001F44E")
                await message.add_reaction(get(message.guild.emojis, name="idk"))