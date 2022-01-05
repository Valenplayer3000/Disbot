import discord
from discord.ext import commands


class AboutCog(commands.Cog, name="about command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="about", usage="", description="About the bot.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def about(self, ctx):
        await ctx.send("📝 || This bot was made with Python.")
        await ctx.send("🔨 || Created by Bloom#9014")


def setup(bot: commands.Bot):
    bot.add_cog(AboutCog(bot))
