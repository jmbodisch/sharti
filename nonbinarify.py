from discord.ext import tasks, commands
import discord

class Nonbinarify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    vowels = ["a", "e", "i", "o", "u"]

    def nonbinarify(str):
        result = ""
        if str is not None:
            words = str.split()
            for word in words:
                newWord = word
                if len(word) > 1:
                    rest = word[1:]
                    newWord = "th" + rest
                for vowel in vowels:
                    newWord = newWord.replace(vowel, "x")
                result += newWord
                result += " "
        return result

    @commands.command()
    async def nb(ctx, *, message: str):
        await ctx.send(nonbinarify(message))