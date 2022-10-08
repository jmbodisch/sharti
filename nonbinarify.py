from discord.ext import tasks, commands
import discord

class Nonbinarify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nb(self, ctx, *, message: str):
        vowels = ["a", "e", "i", "o", "u"]
        result = ""
        if message is not None:
            words = message.split()
            for word in words:
                newWord = word
                if len(word) > 1:
                    rest = word[1:]
                    newWord = "th" + rest
                for vowel in vowels:
                    newWord = newWord.replace(vowel, "x")
                result += newWord
                result += " "
        await ctx.send(result)