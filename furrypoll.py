from discord.ext import tasks, commands
import discord

class FurryPoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='furrypoll')
    async def furry_poll(self, message):
        with open('content/furrypoll.png', 'rb') as f:
            print('furry poll...')
            msg = await message.channel.send(file=discord.File(f))
            await msg.add_reaction(u"\U0001F44D")
            await msg.add_reaction(u"\U00002665")
            await msg.add_reaction(u"\U0001F62E")
            await msg.add_reaction(u"\U0001F622")