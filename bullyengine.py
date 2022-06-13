import random
from discord.ext import commands
from discord.utils import get

class BullyEngine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 309881856898367489: #bully damp
            if message.channel.id != 750594840647172096 and message.channel.id != 828495394194980875:
                if random.randrange(0, 300) == 182:
                    print('bullying damp with a lil react')
                    await message.add_reaction(u"\U0001F44E")

        if message.author.id == 103637471115382784: #me
            if random.randrange(0, 100) == 50:
                print('plooding for daddy')
                await message.add_reaction(get(message.guild.emojis, name="plooding"))

        if message.content=='hi sharti':
            if message.author.id == 309881856898367489: #bully damp
                print('damp said hi')
                await message.add_reaction(u"\U0001F595")
            else:
                print('someone said hi')
                await message.channel.send('<:babydamp:866167423055691786>')
            if message.author.id == 96284227053551616: #hi knick
                print('knick said hi')
                await message.add_reaction(get(message.guild.emojis, name="goodjob"))

        if message.content=='bye sharti':
            print('someone said bye')
            await message.add_reaction(u"\U0001F44B")