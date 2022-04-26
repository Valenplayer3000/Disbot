import discord
from discord.ext import commands
import sys


class VersionCog(commands.Cog, name="api-version command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="apiversion",
                      usage="",
                      description="See the version of API")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def version(self, ctx):
        await ctx.send("⚙ || Current Discord Version: " + discord.__version__)
        await ctx.send("🗂 || Current Python Version: " + sys.version)


def setup(bot: commands.Bot):
    bot.add_cog(VersionCog(bot))
