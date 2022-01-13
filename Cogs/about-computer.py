import discord
from discord.ext import commands
import platform


class AboutPCCog(commands.Cog, name="about computer command"):
    def __init(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="aboutpc", usage="", description="Display server (PC) information")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def aboutpc(self, ctx):  # Sends the pc information to the Server
        await ctx.send("==" + " System Information " + "==")
        uname = platform.uname()
        await ctx.send(f"System: {uname.system}")
        await ctx.send(f"Node Name: {uname.node}")
        await ctx.send(f"Release: {uname.release}")
        await ctx.send(f"Version: {uname.version}")
        await ctx.send(f"Machine: {uname.machine}")
        await ctx.send(f"Processor: {uname.processor}")


def setup(bot: commands.Bot):
    bot.add_cog(AboutPCCog(bot))
