import discord
import os
from os import system
from discord.ext import commands
import configparser
import mysql.connector
import shutil
from discord.utils import get

# generate random integer values
from random import seed
from random import randint




class Level (commands.Cog):

    def __init__(self, client):
        self.client = client

    # Database global Information
    global host
    global user
    global passwd
    global auth_plugin
    config = configparser.ConfigParser()
    config.read('../sql.ini')
    host = str(config.get('info','host'))
    user = str(config.get('info','user'))
    passwd = str(config.get('info','passwd'))
    auth_plugin = str(config.get('info','auth_plugin'))

    #MySQL
    global mydb
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        auth_plugin=auth_plugin
    )


    #--------------------------[Event  Handlers]------------------------#
    @commands.Cog.listener()
    async def on_message(self, message):
        #print("got message")
        def update_data(self, member, guild, message = None):
            guild_id = str(guild)
            mycursor = mydb.cursor()
            mycursor.execute("USE `" + guild_id + "`")
            mycursor.execute("SELECT `experience` FROM `level_system` WHERE userid = " + str(member.id))
            global result
            result = mycursor.fetchall()

            if(len(result) == 0):
                mycursor.execute("USE `" + guild_id+"`")
                mycursor.execute("INSERT INTO `level_system` VALUES("+ str(member.id) +",'0','0','"+ str(member) +"','" + str(member.avatar_url) + "')")
                mydb.commit()
            else:
                xp = int(result[0][0]) + 1
                #print("XP from database for user: " + str(result[0][0]))
                #print("New XP to be loaded: " + str(xp))

                mycursor.execute("USE `" + guild_id+"`")
                mycursor.execute("SELECT `level` FROM `level_system` WHERE userid = " + str(member.id))
                currentLevel = mycursor.fetchall()
                mycursor.execute("UPDATE `level_system` SET experience = "+str(xp)+" WHERE userid = " + str(member.id))
                #print("XP SHOULD BE " + str(xp))
                mydb.commit()

                i=2
                levels = [0,2,20]
                while i < 1000:
                    this = i * 20
                    levels.append(this)
                    i+=1

                i = 0
                exp = xp
                newlevel=0

                while i <= len(levels) - 1:
                    if exp >= levels[i]:
                        if exp <= levels[i+1]:
                            newlevel = i
                            break
                    i+=1

                if int(currentLevel[0][0]) < newlevel:
                    mycursor.execute("UPDATE `level_system` SET level = "+str(newlevel)+" WHERE userid = " + str(member.id))
                    mydb.commit()

                    embed = discord.Embed()
                    embed.set_author(name = "Feed_Ekko - Level Up", icon_url = self.client.user.avatar_url)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.description = f"{member.mention} has leveled up to Level {newlevel}"
                    return(embed)
                    # await message.channel.send(embed=embed)


        num = randint(0,20)
        num = randint(1,3)

        if num == 2:
            if isinstance(message.channel, discord.DMChannel):
                pass
            elif message.author.bot == True:
                pass
            else:
                guild_id = message.guild.id
                member = message.author
                check = str(message)
                check = check[0]
                if member.id == bot_id:
                    pass
                elif check == '>':
                    pass
                else:
                    embed = discord.Embed()
                    embed = update_data(self, member, guild_id, message)
                    if embed is None:
                        pass
                    else:
                        await message.channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guild_id = str(guild.id)
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE `" + guild_id + "`")
        mycursor.execute("CREATE TABLE `"+ guild_id +"`.`level_system` ( `userid` VARCHAR(50) NOT NULL , `experience` BIGINT NOT NULL , `level` BIGINT NOT NULL , `username` VARCHAR(50) NOT NULL , `avatarurl` VARCHAR(2083) NOT NULL , PRIMARY KEY (`userid`))")
        mycursor.execute("CREATE TABLE `"+ guild_id +"`.`twitch` ( `userid` VARCHAR(50) NOT NULL , `username` VARCHAR(50) NOT NULL , `twitch` VARCHAR(50) NOT NULL , PRIMARY KEY (`userid`))")
        mydb.commit()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guild_id = str(guild.id)
        mycursor = mydb.cursor()
        mycursor.execute("USE " + guild_id)
        mycursor.execute("DROP DATABASE `" + guild_id + "`")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild_id = str(member.guild.id)
        mycursor = mydb.cursor()
        mycursor.execute("USE `" + guild_id + "`")
        mycursor.execute("DELETE FROM `level_system` WHERE userid = " + str(member.id))


    #-------------------------------------------------------------------#
    #--------------------------[Level Commands]-----------------------#
    #show top3 levels
    @commands.command()
    async def top3(self, ctx):

        guild_id = str(ctx.guild.id)
        mycursor = mydb.cursor()
        mycursor.execute("USE `" + guild_id + "`")

        mycursor.execute("SELECT `username`,`experience`,`level`,`avatarurl` FROM `level_system`")
        global result
        result = mycursor.fetchall()

        top1 = ['Name',0,0,'avatar']
        top2 = ['Name',0,0,'avatar']
        top3 = ['Name',0,0,'avatar']

        i = 0
        end = int(len(result))
        if end == 0:
            await ctx.send(f"Im sorry but looks like we cant create a leaderboard yet, please try again later!")

        else:
            for i in range(end):
                num = result[i][1]
                if num >= top1[1]:
                    top1[0] = result[i][0]
                    top1[1] = result[i][1]
                    top1[2] = result[i][2]
                    top1[3] = result[i][3]
            for i in range(end):
                num = result[i][1]
                if num >= top2[1]:
                    if result[i][0] == top1[0]:
                        pass
                    else:
                        top2[0] = result[i][0]
                        top2[1] = result[i][1]
                        top2[2] = result[i][2]
                        top2[3] = result[i][3]
            for i in range(end):
                num = result[i][1]
                if num >= top3[1]:
                    if result[i][0] == top1[0] or result[i][0] == top2[0]:
                        pass
                    else:
                        top3[0] = result[i][0]
                        top3[1] = result[i][1]
                        top3[2] = result[i][2]
                        top3[3] = result[i][3]

            # print(top1)
            # print(top2)
            # print(top3)

            if top1[0] != "Name":
                embed = discord.Embed()
                embed.set_author(name = "Feed_Ekko - 1st Place", icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=top1[3])
                embed.description = f"Username: {top1[0][:-5]}"
                embed.add_field(name="\u200b", value= f"Level: {top1[2]}\n Experience: {top1[1]}")
                await ctx.send(embed=embed)

            if top2[0] != "Name":
                embed = discord.Embed()
                embed.set_author(name = "Feed_Ekko - 2st Place", icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=top2[3])
                embed.description = f"Username: {top2[0][:-5]}"
                embed.add_field(name="\u200b", value= f"Level: {top2[2]}\n Experience: {top2[1]}")
                await ctx.send(embed=embed)

            if top3[0] != "Name":
                embed = discord.Embed()
                embed.set_author(name = "Feed_Ekko - 3st Place", icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=top3[3])
                embed.description = f"Username: {top3[0][:-5]}"
                embed.add_field(name="\u200b", value= f"Level: {top3[2]}\n Experience: {top3[1]}")
                await ctx.send(embed=embed)

    #show user level
    @commands.command()
    async def level(self, ctx):

        guild_id = str(ctx.guild.id)
        member = ctx.author
        mycursor = mydb.cursor()
        mycursor.execute("USE `" + guild_id + "`")

        mycursor.execute("SELECT `username`,`experience`,`level` FROM `level_system` WHERE userid = " + str(member.id))
        global result
        result = mycursor.fetchall()

        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - User Level", icon_url=self.client.user.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.description = f"Username: {result[0][0][:-5]}"
        embed.add_field(name="\u200b", value= f"Level: {result[0][2]}\n Experience: {result[0][1]}")
        await ctx.send(embed=embed)
    #-------------------------------------------------------------------#


def setup(client):
    client.add_cog(Level(client))
    global bot_id
    config = configparser.ConfigParser()
    config.read('../token.ini')
    token = config.get('token', 'token')
    bot_id = str(config.get('token','bot_id'))
