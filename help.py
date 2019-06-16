import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        user = ctx.message.author

        embed = discord.Embed(color=discord.Color.gold(), timestamp=ctx.message.created_at)

        embed.set_author(name="Help", icon_url=ctx.author.avatar_url)

        embed.add_field(name="cogs", value="Checks if cogs are functioning.", inline=False)
        embed.add_field(name="level", value="Shows your level and EXP.", inline=False)
        embed.add_field(name="ban @user", value="Bans a pinged user. Mods only.", inline=False)
        embed.add_field(name="bug (bug report here)", value="Sends your bug report to the developer. Possible rewards.", inline=False)
        embed.add_field(name="color (hex color here)", value="Custom color role with your username. Google hex color, and paste it in after cmd.", inline=False)
        embed.add_field(name="help @user", value="This command. Shows all commands + description.", inline=False)
        embed.add_field(name="kick @user", value="Kicks a pinged member. Mods only.", inline=False)
        embed.add_field(name="members", value="Shows the amount of members in your current server.", inline=False)
        embed.add_field(name="ping", value="Responds with 'Pong!' and your ping. ", inline=False)
        embed.add_field(name="purge (number)", value="Deleted a specified amount of messages.", inline=False)
        embed.add_field(name="say (message here)", value="Repeats what you said, and deletes your message.", inline=False)
        embed.add_field(name="server", value="Sends a link to the official support server.", inline=False)
        embed.add_field(name="suggest (suggestion here)", value="Sends your suggestion to the developer. Possible large rewards.", inline=False)
        embed.add_field(name="user @user", value="Shows detailed information about the pinged user.", inline=False)

        await user.send(embed=embed)

        embed = discord.Embed(title="Sent!", description=f"I have DM'ed a list of all commands to you, {ctx.message.author.display_name}!",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        print('>help')


def setup(bot):
    bot.add_cog(Help(bot))