import discord
from discord.ext import commands


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def lvl_up(self, user):
        cur_exp = user['xp']
        cur_lvl = user['lvl']

        if cur_exp >= round((15 + 3 * (cur_lvl ** 3)) / 5):
            await self.bot.pg_con.execute("UPDATE users SET lvl = $1 WHERE user_id = $2 AND guild_id = $3", cur_lvl + 1, user['user_id'], user['guild_id'])
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)
        guild_id = str(message.guild.id)

        user = await self.bot.pg_con.fetchrow(
            """
                SELECT *
                FROM users
                WHERE user_id = $1 AND guild_id = $2;
            """,
            author_id, guild_id
        )

        if not user:
            await self.bot.pg_con.execute("INSERT INTO users (user_id, guild_id, lvl, xp) VALUES ($1, $2, 1, 0)", author_id, guild_id)

        user = await self.bot.pg_con.fetchrow(
            """
                SELECT *
                FROM users
                WHERE user_id = $1 AND guild_id = $2;
            """,
            author_id, guild_id
        )

        await self.bot.pg_con.execute("UPDATE users SET xp = $1 WHERE user_id = $2 AND guild_id = $3", user['xp'] + 2.5, author_id, guild_id)

        if await self.lvl_up(user):
            embed = discord.Embed(title="Level up!", description=f"{message.author.mention} is now level {user['lvl'] + 1}!",
                                  color=discord.Color.gold())
            await message.channel.send(embed=embed)

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        guild_id = str(ctx.guild.id)
        author_id = str(ctx.message.author.id)

        user = await self.bot.pg_con.fetch(
            """
                SELECT *
                FROM users
                WHERE user_id = $1 AND guild_id = $2;
            """,
            author_id, guild_id
        )

        if not user:
            embed = discord.Embed(title="EXP", description=f"You don't seem to have any EXP at all, {ctx.message.author.mention}.",
                                  color=discord.Color.gold())
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"Level - {member}", icon_url=self.bot.user.avatar_url)

            embed.add_field(name="Level", value=user[0]['lvl'])
            embed.add_field(name="Experience", value=user[0]['xp'])

            await ctx.send(embed=embed)


    @commands.command()
    async def cogs(self, ctx):
        embed = discord.Embed(title="Cog state", description="/ᐠ.ᆽ.ᐟ \ Toast cogs are operational.",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)


    # @commands.command()
    # async def credit(self, user, message):
    #
    #     credit = user['Credits']
    #
    #     await self.bot.pg_con.execute("UPDATE users SET Credits = $1 WHERE user_id = $2", credit + 1,
    #                                   user[0])
    #     embed = discord.Embed(title="You found 1 credit!", description=" /ᐠ.ᆽ.ᐟ \ You found a credit in the ground.",
    #                           color=discord.Color.gold())
    #     await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Levels(bot))
