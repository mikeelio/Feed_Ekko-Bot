import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import mysql.connector

class Moderator (commands.Cog):

    def __init__(self, client):
        self.client = client

    #Command to kick user
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kickuser(self, ctx, member : discord.Member = None,*,reason=None):

        if member is None:
            await ctx.send(f"{ctx.author.mention} \nSorry but this command needs a user in order to ban. (>Ban 'Username' 'reason')")
            time.sleep(3)
            await ctx.channel.purge(limit=2)
        else:
                await member.kick(reason=reason)
                await ctx.send(f"{member} has been kicked by {ctx.author.mention}")

def setup(client):
    client.add_cog(Moderator(client))
