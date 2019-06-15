import chalk
import discord
from discord.ext import commands
import datetime
import random
import asyncio


bot = commands.Bot(command_prefix=">", status=discord.Status.do_not_disturb,
                   activity=discord.Game(name="Booting up..."))


@bot.event
async def on_ready():
    print(chalk.green("Logged in as"))
    print(chalk.green(bot.user.name))
    print(chalk.green("Bot is online!"))
    print(chalk.green("----------------"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))


@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(title="Pong!", description=f"Your ping is {ping} milliseconds.", color=discord.Color.blurple())
    await ctx.channel.send(embed=embed)


@bot.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.User = None, reason=None):
    name = f"{member.name}#{member.discriminator}"
    name.replace(" ", "").rstrip(name[-5:]).upper()
    if member == None or member == ctx.message.author:
        await ctx.channel.send(f"You can't kick yourself, {name}.")
        return
    if reason is None:
        reason = "an unspecified reason."
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member} has been kicked!")


@bot.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.User = None, reason=None):
    name = f"{member.name}#{member.discriminator}"
    name.replace(" ", "").rstrip(name[-5:]).upper()
    if member == None or member == ctx.message.author:
        await ctx.channel.send(f"You can't ban yourself, {name}.")
        return
    if reason is None:
        reason = "an unspecified reason."
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} has been banned!")


@bot.command()
async def purge(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=99)
    await ctx.channel.send(f"Deleted {len(deleted)} messages.")


@bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@bot.command()
async def server(ctx, member: discord.User = None):
    await ctx.send("https://discord.gg/9FRghE3")
    await ctx.send(f"Join the official Toast server here, {member.display.name}!")


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def suggest(ctx, *, arg):
    user_id_list = [321092781676298240]  # IDs here
    for user_id in user_id_list:
        user = bot.get_user(user_id)
        embed = discord.Embed(title=f"Suggestion by {ctx.message.author}", description=f"{arg}", color=discord.Color.blue())
        embed.set_footer(text=datetime.datetime.utcnow(), icon_url=ctx.author.avatar_url)
        await user.send(embed=embed)
        embed = discord.Embed(title=f"Thank you for your suggestion!", description=f"It has been DM'ed to the bot developer.", color=discord.Color.green())
        embed.set_footer(text=datetime.datetime.utcnow(), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def bug(ctx, *, report):
    user_id_list = [321092781676298240]  # IDs here
    for user_id in user_id_list:
        user = bot.get_user(user_id)
        embed = discord.Embed(title=f"**BUG REPORT BY {ctx.message.author}**", description=f"{report}", color=discord.Color.dark_red())
        embed.set_footer(text=datetime.datetime.utcnow(), icon_url=ctx.author.avatar_url)
        await user.send(embed=embed)
        embed = discord.Embed(title=f"Thank you for the bug report!", description=f"It has been DM'ed to the bot developer. You may receive rewards if the bug is valid.", color=discord.Color.green())
        embed.set_footer(text=datetime.datetime.utcnow(), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


@bot.command()
async def user(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color, timstamp=ctx.message.created_at)

    embed.set_author(name=f"User Information - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Guild name", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)
    await ctx.send(embed=embed)

async def chng_pr():
    await bot.wait_until_ready()

    statuses = ["with yarn o~  ฅ/ᐠ｡ᆽ｡ᐟ \ ", "with users [^._.^]ﾉ彡", "use >help for commands!", ">suggest stuff to add!", "report bugs with >bug!"]

    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(status))

        await asyncio.sleep(10)


@bot.command()
async def color(ctx, *, arg: discord.Colour):
    guild = ctx.guild
    await guild.create_role(name=ctx.message.author.display_name, colour=arg)
    role = discord.utils.get(ctx.guild.roles, name=ctx.message.author.display_name)
    user = ctx.message.author
    await user.add_roles(role)
    embed = discord.Embed(title="Success!",
                          description=f"Your role color has sucessfully been changed to {arg} (The color of this embed).",
                          color=arg)
    await ctx.channel.send(embed=embed)


bot.loop.create_task(chng_pr())
bot.run("NTcxMDA4MDI1NTE5OTgwNTY2.XQPFwA.5MWbEmEP1HBeSEg_dNTIKxz7gsU", bot=True, reconnect=True)
