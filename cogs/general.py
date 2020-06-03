import discord
import os
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Ping
    @commands.command(pass_context = True)
    async def ping (self, ctx, member : discord.Member=None):
        if member is None:
            member = ctx.author
            await ctx.send(f'{member.mention} Pong! ```That Ping took: {round(self.client.latency * 1000)}ms```')
        else:
            await ctx.send(f'{member.mention} Pong! ```That Ping took: {round(self.client.latency * 1000)}ms```')

    #Discord link
    # @commands.command()
    # async def joindiscord(self, ctx):
    #     member = ctx.author
    #     await member.send("Personal Streaming Server\n http://gestyy.com/w7ViEY")
    #     await ctx.send(f"📬 You got mail")

    # @commands.command()
    # async def invite(self, ctx):
    #     member = ctx.author
    #     await member.send("http://gestyy.com/w7ViTe")
    #     await ctx.send(f"📬 You got mail")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear (self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(General(client))
