import discord
from discord.ext import commands
import os
from os import system
import time
import configparser
import shutil
import configparser
import mysql.connector
from discord.utils import get
import datetime
from discord.ext import tasks


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
async def load(ctx, file=None):
    author = str(ctx.author.id)
    if author == owner_id:
        if file is None:
            await ctx.send("Hold up you forgot something")
        else:
            client.load_extension(f'cogs.{file}')
            await ctx.send(f"{file} has been loaded.")
            time.sleep(2)
            await ctx.channel.purge(limit=2)
    else:
        await ctx.send("Sorry but only mikeelio (THE OWNER) can run this command")

#Unload single command
@client.command()
async def unload(ctx, file=None):
    author = str(ctx.author.id)
    if author == owner_id:
        if file is None:
            await ctx.send("Hold up you forgot something")
        else:
            client.unload_extension(f'cogs.{file}')
            await ctx.send(f"{file} has been unloaded.")
            time.sleep(2)
            await ctx.channel.purge(limit=2)
    else:
        await ctx.send("Sorry but only mikeelio (THE OWNER) can run this command")

#Reload single command
@client.command()
async def reload(ctx, file=None):
    author = str(ctx.author.id)
    if author == owner_id:
        if file is None:
            await ctx.send("Hold up you forgot something")
            time.sleep(2)
            await ctx.channel.purge(limit=2)

        elif file == "all":
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    client.unload_extension(f'cogs.{filename[:-3]}')
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    client.load_extension(f'cogs.{filename[:-3]}')

            await ctx.send("All Cogs have been reloaded")
            time.sleep(2)
            await ctx.channel.purge(limit=2)
        else:
            client.unload_extension(f'cogs.{file}')
            await ctx.send(f"{file} has been unloaded.")
            time.sleep(2)
            client.load_extension(f'cogs.{file}')
            await ctx.send(f"{file} has been loaded.")
            time.sleep(2)
            await ctx.channel.purge(limit=4)
    else:
        await ctx.send("Sorry but only mikeelio (THE OWNER) can run this command")


#loads all cogs at startup
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(minutes=30)
async def refresh():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.reload_extension(f'cogs.{filename[:-3]}')
    e = datetime.datetime.now()
    e = e.strftime("%Y-%m-%d %I:%M:%S %p")

    print(f"Bot has refreshed at: {e} ")

refresh.start()
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
