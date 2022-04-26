import discord
from discord.ext import commands


class TestCog(commands.Cog, name="test command"):
    def __int__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="test", usage="", description="Send a Test Message")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def test(self, ctx):
        await ctx.send("Hello World")
        await ctx.send("ABCDEF 1234567890")
        await ctx.send("!@#$%^&*()_+")


def setup(bot: commands.Bot):
    bot.add_cog(TestCog(bot))
