import discord
from discord.ext import commands
import youtube_dl
import os
from os import system
import shutil
from discord.utils import get
import mysql.connector
import json

# generate random integer values
from random import seed
from random import randint

#MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    auth_plugin="mysql_native_password"
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
    print(mydb)


#-------------------------------------------------------------------#
#Learning Stuff
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#-----------------------------[Commands]----------------------------#
#-------------------------------------------------------------------#

#-------------------------------[About]-----------------------------#
@client.command(pass_context=True)
async def about(ctx):
    member=ctx.author
    embed = discord.Embed()
    embed.set_author(name='Feed_Ekko Bot - Help and Documentation',icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=client.user.avatar_url)
    about = [
        "==About the Bot==",
        "The Feed_Ekko Bot was created cause the creator(mikeelio) got bored and hated that some bots",
        "you had to pay for in order to use the goddam volume command.",
        "So now after a month of learning the curse of python and discord.py, we got a 'functioning' bot.",
        "==About the Creator==",
        "The creator of this stupid bot is non other than mikeelio#3708. After graduating college, mans got",
        "bored and though well time to put some time into making a discord bot cause no one will hire me."
    ]
    embed.add_field(name="\u200b",value=f"{about[0]}\n {about[1]}\n {about[2]}\n {about[3]}\n {about[4]}\n {about[5]}\n {about[6]}",inline=False)
    await member.send(embed=embed)
    await ctx.send(f"📬 You got mail")

#-------------------------------------------------------------------#

#-------------------------------[Help]------------------------------#
@client.command(pass_context=True)
async def help(ctx):

    member = ctx.author

    general = [
        "==General Commands==",
        f"⏺️ \u200b >about\t➡️  \u200b  About the bot and the creator (My dumbass did this somehow).",
        f"⏺️ \u200b >help\t ➡️  \u200b  This is the command you just used.",
        f"⏺️ \u200b >ping\t ➡️  \u200b  Test speed",
        "=================="
    ]

    level = [
        "==Level Commands==",
        f"⏺️ \u200b >top3\t        ➡️    \u200b  See the top 3 members on your server.",
        f"⏺️ \u200b >level\t       ➡️    \u200b  Stops the music.",
        "================"
    ]

    music = [
        "==Music Commands==",
        f"⏺️ \u200b >play\t        ➡️    \u200b  Play Music and adds to the queue as well.",
        f"⏺️ \u200b >stop\t        ➡️    \u200b  Stops the music.",
        f"⏺️ \u200b >pause\t       ➡️    \u200b  Pauses the music.",
        f"⏺️ \u200b >resume\t      ➡️    \u200b  Resumes the... I think you get it.",
        f"⏺️ \u200b >queue\t       ➡️    \u200b  Displays Queue (Under Construction).",
        f"⏺️ \u200b >volume\t      ➡️    \u200b  Control the volume (Max 200% for safety reasons).",
        f"⏺️ \u200b >nowplaying\t  ➡️    \u200b  Show whats playing (Experimental for now).",
        "================"
    ]

    nsfw = [
        "==NSFW Section==",
        f"⏺️ \u200b >amateur\t          ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >anal\t             ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >asianporn\t        ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >ass\t              ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >bdsm\t             ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >boobs\t            ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >ecchi\t            ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >getnsfw\t          ➡️    \u200b  Role for Channel and Command.",
        f"⏺️ \u200b >hentai\t           ➡️    \u200b  Its Art.",
        f"⏺️ \u200b >porn\t             ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >pussy\t            ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >redhead\t          ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >rule34\t           ➡️    \u200b  Its Porn.",
        f"⏺️ \u200b >yuri\t             ➡️    \u200b  Its Porn.",
        "=============="
    ]

    embed = discord.Embed()
    embed.set_author(name='Feed_Ekko Bot - Help and Documentation',icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="\u200b",value=f"{general[0]}\n {general[1]}\n {general[2]}\n {general[3]}\n {general[4]}",inline=False)
    embed.add_field(name="\u200b",value=f"{level[0]}\n {level[1]}\n {level[2]}\n {level[3]}",inline=False)
    embed.add_field(name="\u200b",value=f"{music[0]}\n {music[1]}\n {music[2]}\n {music[3]}\n {music[4]}\n {music[5]}\n {music[6]}\n {music[7]}\n {music[8]}",inline=False)
    try:
        role = discord.utils.get(ctx.guild.roles, name="NSFW")
        if role in member.roles:
            embed.add_field(name="\u200b", value=f"{nsfw[0]}\n {nsfw[1]}\n {nsfw[2]}\n {nsfw[3]}\n {nsfw[4]}\n {nsfw[5]}\n {nsfw[6]}\n {nsfw[7]}\n {nsfw[8]}\n {nsfw[9]}\n {nsfw[10]}\n {nsfw[11]}\n {nsfw[12]}\n {nsfw[13]}\n {nsfw[14]}\n {nsfw[15]}")
        else:
            embed.add_field(name="\u200b", value=f"{nsfw[0]}\n {nsfw[8]}\n {nsfw[15]}")
    except:
        embed.add_field(name="\u200b", value=f"{nsfw[0]}\n Can ONLY be accessed in a SERVER\n {nsfw[15]}")
    await member.send(embed=embed)
    await ctx.send(f"📬 You got mail")

#-------------------------------------------------------------------#

#--------------------------[Discord  Link]--------------------------#
@client.command()
async def joindiscord(ctx):
    member = ctx.author
    await member.send("Personal Streaming Server\n https://discord.gg/kdQFwyn")
    await ctx.send(f"📬 You got mail")
#-------------------------------------------------------------------#

#-------------------------[Discord  Invite]-------------------------#
@client.command()
async def invite(ctx):
    member = ctx.author
    await member.send("https://discordapp.com/api/oauth2/authorize?client_id=666071024407674891&permissions=1345834183&scope=bot")
    await ctx.send(f"📬 You got mail")
#-------------------------------------------------------------------#

#-------------------------------[Clear]-----------------------------#
@client.command()
async def clear (ctx, amount=10):
    await ctx.channel.purge(limit=amount)
#-------------------------------------------------------------------#

#----------------------------[Ping/ Pong]---------------------------#
@client.command()
async def ping(ctx):
    member = ctx.author
    await ctx.send(f'{member.mention} Pong! ```That Ping took: {round(client.latency * 1000)}ms```')
#-------------------------------------------------------------------#

#--------------------------[Kick/Ban/Unban]-------------------------#
#Command to kick user
@client.command()
async def kickuser(ctx, member : discord.Member = None, *, reason=None):
    if member is None:
        await ctx.send(ctx.author, "Sorry but this command needs a user in order to ban. (>Ban 'Username' 'reason')")
    else:
        await member.kick(reason=reason)
#Command to ban user
@client.command()
async def banuser(ctx, member : discord.Member = None, *, reason=None):
    await member.ban(reason=reason)
#Command to unban user
@client.command()
async def unbanuser(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send (f'Unbanned{user.mention}')
            return
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#--------------------------[Voice Commands]-------------------------#
#-------------------------------------------------------------------#

#--------------------------[Join/Disconnect]------------------------#
#Command to join voice channel
@client.command(pass_context=True)
async def summon(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

#Command to disconnect from voice channel
@client.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        member = ctx.author
        await ctx.send (f"{member.mention} Sir I am not in a channel.")
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#--------------------------[Player Commands]------------------------#
#-------------------------------------------------------------------#
#Command to play music with title
@client.command(pass_context=True)
async def play (ctx, *url: str):

    if not url:
        return await ctx.send(f"{ctx.author.mention} No Selected Music (>play 'name of song')")
    global voice
    try:
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            print()
        else:
            voice = await channel.connect()
    except:
        return await ctx.send(f"{ctx.author.mention} Your not in a voice channel. Are you trying to kill me?")

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_queue = length - 1

            try:
                first_file = os.listdir(DIR)[0]
            except:
                queues.clear()
                return

            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)

            if length != 0:
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)

                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        name = file
                        os.rename(file, "song.mp3")
                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return
        else:
            queues.clear()


    song_exist = os.path.isfile("song.mp3")
    try:
        if song_exist:
            os.remove("song.mp3")
            queues.clear()
    except PermissionError:
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is False:
            os.mkdir("Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        q_num = len(os.listdir(DIR))
        q_num += 1
        add_queue = True
        while add_queue:
            if q_num in queues:
                q_num += 1
            else:
                add_queue = False
                queues[q_num] = q_num
        queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        song_search = " ".join(url)

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("downloading audio")
                ydl.download([f"ytsearch1:{song_search}"])
                print("downloading complete")

        except:
            c_path = os.path.dirname(os.path.realpath(__file__))
            system("spotdl -ff song -f " + '"' + c_path + '"' + " -s " + song_search)


        await ctx.send("Added song to the queue")

        return

    Queue_infile = os.path.isdir("./Queue")

    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            shutil.rmtree(Queue_folder)
    except:
        print("No Old Queue Folder")


    await ctx.send("Preparing: Wait im going as fast as i can")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    song_search = " ".join(url)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading audio")
            ydl.download([f"ytsearch1:{song_search}"])
            print("downloading complete")

    except:
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -ff song -f " + '"' + c_path + '"' + " -s " + song_search)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    global nname
    nname = name.rsplit("-", 1)
    await ctx.send(f"Playing: {nname[0]}")

#Command to pause music
@client.command(pass_context=True)
async def pause (ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
        await ctx.send("Music Paused")
    else:
        member = ctx.author
        await ctx.send (f"{member.mention} Music not playing")

#Command to resume music
@client.command(pass_context=True)
async def resume (ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        voice.resume()
        await ctx.send(f"Music Resumed: {nname[0]}")
    else:
        member = ctx.author
        await ctx.send (f"{member.mention} Music not paused")

#Command to stop music
@client.command(pass_context=True)
async def stop (ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send("Music Stopped")
    else:
        member = ctx.author
        await ctx.send (f"{member.mention} Music not playing")


queues = {}

#Command for queue
@client.command(pass_context=True)
async def queue (ctx):
    print()
#Command for skipping music
@client.command(pass_context=True)
async def skip (ctx):
    voice = get (client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send(f"Now Playing: {nname[0]}")

    else:
        member = ctx.author
        await ctx.send(f"{member.mention} Music not playing")

#Command for volume control
@client.command(pass_context=True)
async def volume (ctx, volume: int):

    if ctx.voice_client is None:
        await ctx.send("Sir I am not in a channel")
    else:

        if volume > 200:
            member = ctx.author
            return await ctx.send(f"{member.mention} Thats too loud")

        ctx.voice_client.source.volume = volume / 1000
        await ctx.send(f"Volume is now {volume}%")

#Command for nowplaying
@client.command(pass_context=True)
async def nowplaying (ctx):

    await ctx.send(f"Now Playing: {nname[0]}")

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#--------------------------[Twitch Commands]------------------------#
#-------------------------------------------------------------------#

#------------------------[Add User's Twitch]------------------------#
@client.command(pass_content=True)
async def addstreamer (ctx, member: discord.Member=None):
    author = ctx.author
    if member is None:
        return await ctx.send(f"{author.mention} The command is >addstreamer 'Twitch Username' ")
    else:
        with open('Twitch.json','w') as f:
            json.dump(member,f)
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#--------------------------[Images Commands]------------------------#
#-------------------------------------------------------------------#

#------------------------------[General]----------------------------#
#Command for Hi
@client.command(pass_context = True)
async def hello (ctx):
    max_num = 5
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f'Google Drive Images\Images\General\Hello\hello({num}).gif'
    print(sendimage)
    member = ctx.author
    await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#-------------------------------------------------------------------#

#-------------------------------[Anime]-----------------------------#
#Command for baka
@client.command(pass_context = True)
async def baka (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/Baka')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/Baka/baka({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for bang
@client.command(pass_context = True)
async def bang (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/bang')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/bang/bang({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for bite
@client.command(pass_context = True)
async def bite (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/bite')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/bite/bite({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for blush
@client.command(pass_context = True)
async def blush (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/blush')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/blush/blush({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for cuddle
@client.command(pass_context = True)
async def cuddle (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/cuddle')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/cuddle/cuddle({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for dab
@client.command(pass_context = True)
async def dab (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/dab')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/dab/dab({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for dance
@client.command(pass_context = True)
async def dance (ctx, member : discord.Member=None):
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/Anime/dance')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/dance/dance({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for getfucked
@client.command(pass_context = True)
async def getfucked (ctx, member : discord.Member=None):
    max_num = 2
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f"Google Drive Images/Images/Anime/fucked/fucked({num}).gif"
    print(sendimage)

    if member is None:
            await ctx.send(file=discord.File(sendimage))
    else:
        await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#Command for greet
#Command for headbang
#Command for highfive
#Command for hug
#Command for kiss
#Command for lewd
#Command for lick
#Command for megumin
#Command for nani
#Command for neko
#Command for nom
#Command for owo
#Command for pat
#Command for poke
#Command for punch
#Command for rem
#Command for slap
#Command for shrug
#Command for sleepy
#Command for stare
#Command for thumbsup
#Command for tickle
#-------------------------------------------------------------------#

#--------------------------------[NS-FW]----------------------------#
#Command for amateur
#Command for anal
#Command for asianporn
@client.command(pass_context = True)
async def asianporn (ctx):
    role = discord.utils.get(ctx.guild.roles, name="NSFW")
    member = ctx.author
    if role in member.roles:
        if ctx.channel.is_nsfw():
            count = (len([iq for iq in os.scandir('Google Drive Images/Images/NSFW/asianporn')]))
            max_num = count - 1
            num = randint(0,12)
            num = randint(0,max_num)

            sendimage = f"Google Drive Images/Images/NSFW/asianporn/asianporn({num}).png"
            await ctx.send(file=discord.File(sendimage, spoiler=True))
        else:
            member = ctx.author
            await ctx.send(f"{member.mention} This command can only be used in NSFW chat.")
    else:
            await ctx.send(f"{member.mention} You need the NSFW Role sir")

#Command for ass
#Command for bdsm
#Command for boobs
#Command for ecchi
#Command for hentai
#Command for porn
#Command for pussy
#Command for redhead
#Command for rule34
#Command for tentacle
#Command for yuri

#Command for getting NSFW role
@client.command(pass_context = True)
async def getnsfw (ctx, member : discord.Member = None):

    user = ctx.author
    if member is None:
        return await ctx.send(f"{user.mention} The correct command is >getnsfw 'Your Username'")

    if member is user:
        nsfwrole = discord.utils.get(user.guild.roles, name="NSFW")
        if nsfwrole is None:
            await ctx.send(f"{user.mention}Oh looks like theres no nsfw role... Well I think I should create one...\n Please use the command again to get the role.")
            await ctx.guild.create_role(name="NSFW")
        else:
            await user.add_roles(nsfwrole)
            await user.send("NSFW Role has been added, Remember doing this means you are saying you are 18 years of age!!!")



#-------------------------------------------------------------------#

#-----------------------------[Dark Meme]---------------------------#
#Command for darkmeme
@client.command(pass_context = True)
async def darkmeme (ctx):
    max_num = 76
    num = randint(0,5)
    num = randint(0,max_num)

    sendimage = f'Google Drive Images/Images/Memes/Dark Memes/dark_meme({num}).png'
    print(sendimage)
    await ctx.send(file=discord.File(sendimage))

#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#--------------------------[Leveling System]------------------------#
#-------------------------------------------------------------------#

#--------------------------[Event  Handlers]------------------------#

@client.event
async def on_guild_join(guild):
    guild_id = str(guild.id)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE `" + guild_id + "`")
    mycursor.execute("CREATE TABLE `"+ guild_id +"`.`level_system` ( `userid` VARCHAR(50) NOT NULL , `experience` BIGINT NOT NULL , `level` BIGINT NOT NULL , `username` VARCHAR(50) NOT NULL , `avatarurl` VARCHAR(2083) NOT NULL , PRIMARY KEY (`userid`))")
    mydb.commit()

@client.event
async def on_guild_remove(guild):
    guild_id = str(guild.id)
    mycursor = mydb.cursor()
    mycursor.execute("USE " + guild_id)
    mycursor.execute("DROP DATABASE `" + guild_id + "`")

async def update_data(member, guild, message = None):
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
            embed.set_author(name = "Feed_Ekko - Level Up", icon_url = client.user.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            embed.description = f"{member.mention} has leveled up to Level {newlevel}"
            await message.channel.send(embed=embed)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        pass
    elif message.author.bot == True:
        pass

    else:
        guild_id = message.guild.id
        member = message.author
        if member.id == 666071024407674891:
            pass
        else:
            await update_data(member, guild_id, message)
    if isinstance(message.channel, discord.DMChannel):
        pass
    else:
        await client.process_commands(message)
#-------------------------------------------------------------------#

#--------------------------[Level Commands]-----------------------#
#show top3 levels
@client.command()
async def top3(ctx):

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

    print(top1)
    print(top2)
    print(top3)

    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - 1st Place", icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=top1[3])
    embed.description = f"Username: {top1[0]}"
    embed.add_field(name="\u200b", value= f"Level: {top1[2]}\n Experience: {top1[1]}")
    await ctx.send(embed=embed)

    embed.set_author(name = "Feed_Ekko - 2st Place", icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=top2[3])
    embed.description = f"Username: {top2[0]}"
    embed.add_field(name="\u200b", value= f"Level: {top2[2]}\n Experience: {top2[1]}")
    await ctx.send(embed=embed)

    embed.set_author(name = "Feed_Ekko - 3st Place", icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=top3[3])
    embed.description = f"Username: {top3[0]}"
    embed.add_field(name="\u200b", value= f"Level: {top3[2]}\n Experience: {top3[1]}")
    await ctx.send(embed=embed)

#show user level
@client.command()
async def level(ctx):

    guild_id = str(ctx.guild.id)
    member = ctx.author
    mycursor = mydb.cursor()
    mycursor.execute("USE `" + guild_id + "`")

    mycursor.execute("SELECT `username`,`experience`,`level` FROM `level_system` WHERE userid = " + str(member.id))
    global result
    result = mycursor.fetchall()

    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - User Level", icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.description = f"Username: {result[0][0]}"
    embed.add_field(name="\u200b", value= f"Level: {result[0][2]}\n Experience: {result[0][1]}")
    await ctx.send(embed=embed)
#-------------------------------------------------------------------#




#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#Assigns the bot to the token
token = "SURE"
client.run(token)
