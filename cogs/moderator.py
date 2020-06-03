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
    async def kick(self, ctx, member : discord.Member = None,*,reason=None):
        if member is None:
            await ctx.send(f"{ctx.author.mention} \nSorry but this command needs a user in order to kick. (>kick 'Username' 'reason')")
            time.sleep(3)
            await ctx.channel.purge(limit=2)
        else:
                await member.kick(reason=reason)
                await ctx.send(f"{member} has been kicked by {ctx.author.mention}")

    #Command to ban user
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member = None,*,reason=None):
        if member is None:
            await ctx.send(f"{ctx.author.mention} \nSorry but this command needs a user in order to ban. (>ban 'Username' 'reason')")
            time.sleep(3)
            await ctx.channel.purge(limit=2)
        else:
                await member.ban(reason=reason)
                await ctx.send(f"{member} has been banned by {ctx.author.mention}")

    #Command to unban user
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member : discord.Member = None):
        if member is None:
            await ctx.send(f"{ctx.author.mention} \nSorry but this command needs a user in order to unban. (>unban 'Username')")
            time.sleep(3)
            await ctx.channel.purge(limit=2)
        else:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send (f'Unbanned{user.mention}')
                    return


def setup(client):
    client.add_cog(Moderator(client))
