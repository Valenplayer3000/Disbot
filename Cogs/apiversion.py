import discord
from discord.ext import commands


class VersionCog(commands.Cog, name="api-version command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="apiversion",
                      usage="",
                      description="See the version of API")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def version(self, ctx):
        await ctx.send("⚙ || Current API Version: " + discord.__version__)


def setup(bot: commands.Bot):
    bot.add_cog(VersionCog(bot))
