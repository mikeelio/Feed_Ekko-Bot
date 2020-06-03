import discord
import os
from discord.ext import commands
import shutil
from discord.utils import get

class Assign (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = discord.utils.get(member.guild.roles, name="General")

        if role in member.roles:
            pass
        else:
            if payload.guild_id is None:
                return
            else:
                #print("Passed checkpoint 1")
                if payload.channel_id == 696011049433825306:
                    #print("Passed checkpoint 2")
                    if payload.emoji.name == '✅':
                        #print("Passed checkpoint 3")
                        await member.add_roles(role)
                        #print(f"Gave{member} The General Role")
                        embed = discord.Embed()
                        embed.set_author(name = "Feed_Ekko - New Member", icon_url = self.client.user.avatar_url)
                        embed.set_thumbnail(url=member.avatar_url)
                        embed.description = f"{member.mention} has joined the family."
                        channel = self.client.get_channel(701548839995310100)
                        await channel.send(embed=embed)
                        await member.send("You now have the role: General")

                        role = discord.utils.get(member.guild.roles, name="Read_Rules")
                        await member.remove_roles(role)
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name = "Read_Rules")
        await member.add_roles(role)


def setup(client):
    client.add_cog(Assign(client))
