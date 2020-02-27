import discord
from discord.ext import commands
import os
from os import system
import time
import configparser
import shutil


#Setting up the prefix the bot will use
client = commands.Bot(command_prefix = '>')
client.remove_command('help')
#setting up the bots
@client.event
async def on_ready():
    activity = discord.Activity(name='how to become an AI', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print (client.user.name+' Bot is ready.')


#-------------------------------------------------------------------#
#-----------------------------[Commands]----------------------------#
#-------------------------------------------------------------------#

#Load single command
@client.command()
async def load(ctx, file):
    author = str(ctx.author.id)
    if author == owner_id:
        client.load_extension(f'cogs.{file}')
        await ctx.send(f"{file} has been loaded.")
        time.sleep(2)
        await ctx.channel.purge(limit=2)
    else:
        await ctx.send("Sorry but only mikeelio (THE OWNER) can run this command")

#Unload single command
@client.command()
async def unload(ctx, file):
    author = str(ctx.author.id)
    if author == owner_id:
        client.unload_extension(f'cogs.{file}')
        await ctx.send(f"{file} has been unloaded.")
        time.sleep(2)
        await ctx.channel.purge(limit=2)
    else:
        await ctx.send("Sorry but only mikeelio (THE OWNER) can run this command")

#Reload single command
@client.command()
async def reload(ctx, file):
    author = str(ctx.author.id)
    if author == owner_id:
        client.unload_extension(f'cogs.{file}')
        await ctx.send(f"{file} has been unloaded.")
        time.sleep(2)
        client.unload_extension(f'cogs.{file}')
        await ctx.send(f"{file} has been unloaded.")
        time.sleep(2)
        await ctx.channel.purge(limit=4)
    else:
        await ctx.send("Sorry but only mikeelio (THE OWNER) can run this command")



#loads all cogs at startup
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        pass
    elif message.author.bot == True:
        pass

    else:
        guild_id = message.guild.id
        member = message.author
        if member.id == bot_id:
            pass
        else:
            await update_data(member, guild_id, message)
    if isinstance(message.channel, discord.DMChannel):
        pass
    else:
        await client.process_commands(message)




#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#Assigns the bot to the token
config = configparser.ConfigParser()
config.read('../token.ini')
token = config.get('token', 'token')
owner_id = str(config.get('token','id'))
bot_id = str(config.get('token','bot_id'))
client.run(token)
