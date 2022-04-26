import discord
from discord.ext import commands
import random



class RollCog(commands.Cog, name="roll command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="roll", usage="", description="Send a random number")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def roll(self, ctx):
        number = random.randint(1, 100)
        await ctx.send(number)
        if number == 100:
            ctx.send("You won. Literally...")
        elif number == 0:
            ctx.send("You have tried. What do you think?")


def setup(bot: commands.Bot):
    bot.add_cog(RollCog(bot))
