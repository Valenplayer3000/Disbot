import discord 
from discord.ext import commands

class NyanCog(commands.Cog, name="nyan command"):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @commands.command( name = "nyan",
                    usage = "",
                    description = "Say nyan! ^W^")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def nyan(self, ctx):
        await ctx.send("🐱 || Nyan!")


def setup(bot:commands.Bot):
    bot.add_cog(NyanCog(bot))
