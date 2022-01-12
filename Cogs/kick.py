import discord
from discord.ext import commands


class KickCog(commands.Cog, name="kick command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="kick", usage="", description="Kick a User")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ban(self, ctx):
        await ctx.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        await ctx.send("Get **Rickrolled!**")


def setup(self: commands.Bot):
    self.add_cog(KickCog(self))
