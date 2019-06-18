import discord
from discord.ext import commands
import wikipedia

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx, arg):
        page = ((wikipedia.page(arg)).summary)
        page2 = page[:1990] + '...'
        # await ctx.channel.send(page2)
        # await ctx.channel.send(page.images)
        embed = discord.Embed(title=f"Wikipedia search- {arg}",
                              description=page2,
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        print(">wiki")




def setup(bot):
    bot.add_cog(Wiki(bot))