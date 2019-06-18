import discord
from discord.ext import commands
import praw
import pandas as pd
import datetime as dt


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        # subreddit = reddit.subreddit(arg)
        submission = reddit.subreddit('kittens').random()
        embed = discord.Embed(title=f"{submission.title}",
                              description=f"{submission.score} updoots",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(submission.url)
        print('>reddit')

    @commands.command()
    async def dog(self, ctx):
        # subreddit = reddit.subreddit(arg)
        submission = reddit.subreddit('puppies').random()
        embed = discord.Embed(title=f"{submission.title}",
                              description=f"{submission.score} updoots",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(submission.url)
        print('>reddit')

    @commands.command()
    async def meme(self, ctx):
        # subreddit = reddit.subreddit(arg)
        submission = reddit.subreddit('memes').random()
        embed = discord.Embed(title=f"{submission.title}",
                              description=f"{submission.score} updoots",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(submission.url)
        print('>reddit')

    @commands.command()
    async def surreal(self, ctx):
        # subreddit = reddit.subreddit(arg)
        submission = reddit.subreddit('surrealmemes').random()
        embed = discord.Embed(title=f"{submission.title}",
                              description=f"{submission.score} updoots",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(submission.url)
        print('>reddit')

    @commands.command()
    async def reddit(self, ctx, arg):
        # subreddit = reddit.subreddit(arg)
        submission = reddit.subreddit(arg).random()
        embed = discord.Embed(title=f"{submission.title}",
                              description=f"{submission.score} updoots",
                              color=discord.Color.gold())
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(submission.url)
        print('>reddit')


reddit = praw.Reddit(client_id='BQ_oFJS42glTrg',
                     client_secret='KjwBpYQ5zMheHx3thsbiFDpRWWA',
                     user_agent='Toast',
                     username='PepMeow',
                     password='Mz6275001')


def setup(bot):
    bot.add_cog(Reddit(bot))