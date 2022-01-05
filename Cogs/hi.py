import discord
from discord.ext import commands


class HiCog(commands.Cog, name="hi command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="hi", usage="", description="Say hi!")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def hi(self, ctx):
        await ctx.send("Hi! 👋")


def setup(bot: commands.Bot):
    bot.add_cog(HiCog(bot))
