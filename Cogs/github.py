import discord
from discord.ext import commands


class GithubCog(commands.Cog, name="github command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="github", usage="", description="Display Github Repository")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def github(self, ctx):
        await ctx.send("Github Repository 🔽")
        await ctx.send("https://github.com/Valenplayer3000/Disbot")
        await ctx.send("Github (Web) Repository 🔽")
        await ctx.send("https://github.com/Valenplayer3000/Disbot-Nuxt")


def setup(bot: commands.Bot):
    bot.add_cog(GithubCog(bot))
