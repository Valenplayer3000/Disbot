import discord
from discord.ext import commands


class BanCog(commands.Cog, name="ban command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="ban", usage="", description="Ban a User")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ban(self, ctx):
        await ctx.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")


def setup(self: commands.Bot):
    self.add_cog(BanCog(self))
