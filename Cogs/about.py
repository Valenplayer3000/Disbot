import discord
from discord.ext import commands
import json
import os

with open("configuration.json", "r") as config:
    data = json.load(config)
    branch = data["branch"]


class AboutCog(commands.Cog, name="about command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="about", usage="", description="Display about the bot.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def about(self, ctx):
        await ctx.send("📝 || This bot was made with Python.")
        await ctx.send("🔨 || Created by Bloom#9014")
        await ctx.send("💻 || Github repository: https://github.com/Valenplayer3000/Disbot")
        await ctx.send("📲 || Branch: " + branch)


def setup(bot: commands.Bot):
    bot.add_cog(AboutCog(bot))
