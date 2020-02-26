import discord
from discord.ext import commands
import youtube_dl
import os
from os import system
import shutil
from discord.utils import get
import mysql.connector
import json
import configparser
from imgurpython import ImgurClient

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

#Setting up token
config = configparser.ConfigParser()
config.read('../token.ini')
token = config.get('token', 'token')

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
        "The Feed_Ekko Bot was created cause the creator(mikeelio) got bored and hated that for some bots,",
        "you have to pay for in order to use the goddam volume command.",
        "So now after a month of learning the curse of python and discord.py, we got a 'functioning' bot.",
        "==About the Creator==",
        "The creator of this stupid bot is non other than mikeelio#3708. After graduating college, mans got",
        "bored and though well time to put some time into making a discord bot cause no one will hire me.",
        "Twitch: http://gestyy.com/w7Vu5z",
        "Youtube: http://gestyy.com/w7Viwx"
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
        f"⏺️ \u200b >skip\t        ➡️    \u200b  Not Rocket Science(Experimental for now).",
        f"⏺️ \u200b >queue\t       ➡️    \u200b  Displays Queue (Under Construction).",
        f"⏺️ \u200b >volume\t      ➡️    \u200b  Control the volume (Max 200% for safety reasons).",
        f"⏺️ \u200b >nowplaying\t  ➡️    \u200b  Show whats playing (Experimental for now).",
        "================"
    ]

    nsfw = [
        "==NSFW Section==",
        "Sorry but this is under Construction, please kindly fuck off!",
        "=============="
        # f"⏺️ \u200b >amateur\t          ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >anal\t             ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >asianporn\t        ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >ass\t              ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >bdsm\t             ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >boobs\t            ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >ecchi\t            ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >getnsfw\t          ➡️    \u200b  Role for Channel and Command.",
        # f"⏺️ \u200b >hentai\t           ➡️    \u200b  Its Art.",
        # f"⏺️ \u200b >porn\t             ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >pussy\t            ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >redhead\t          ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >rule34\t           ➡️    \u200b  Its Porn.",
        # f"⏺️ \u200b >yuri\t             ➡️    \u200b  Its Porn.",

    ]

    anime = [
        "==Anime Meme Section==",
        f"⏺️ \u200b >baka",
        f"⏺️ \u200b >bang",
        f"⏺️ \u200b >bite",
        f"⏺️ \u200b >blush",
        f"⏺️ \u200b >cuddle",
        f"⏺️ \u200b >dab",
        f"⏺️ \u200b >dance",
        f"⏺️ \u200b >getfucked",
        f"⏺️ \u200b >greet",
        f"⏺️ \u200b >headbang",
        f"⏺️ \u200b >highfive",
        f"⏺️ \u200b >hug",
        f"⏺️ \u200b >kiss",
        f"⏺️ \u200b >lewd",
        f"⏺️ \u200b >lick",
        f"⏺️ \u200b >megumin",
        f"⏺️ \u200b >nani",
        f"⏺️ \u200b >neko",
        f"⏺️ \u200b >nico",
        f"⏺️ \u200b >nom",
        f"⏺️ \u200b >owo",
        f"⏺️ \u200b >pat",
        f"⏺️ \u200b >poke",
        f"⏺️ \u200b >punch",
        f"⏺️ \u200b >rem",
        f"⏺️ \u200b >shrug",
        f"⏺️ \u200b >slap",
        f"⏺️ \u200b >sleepy",
        f"⏺️ \u200b >stare",
        f"⏺️ \u200b >thumbsup",
        f"⏺️ \u200b >tickle",
        "===================="

    ]

    embed = discord.Embed()
    embed.set_author(name='Feed_Ekko Bot - Help and Documentation',icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="\u200b",value=f"{general[0]}\n {general[1]}\n {general[2]}\n {general[3]}\n {general[4]}",inline=False)
    embed.add_field(name="\u200b",value=f"{level[0]}\n {level[1]}\n {level[2]}\n {level[3]}",inline=False)
    embed.add_field(name="\u200b",value=f"{music[0]}\n {music[1]}\n {music[2]}\n {music[3]}\n {music[4]}\n {music[5]}\n {music[6]}\n {music[7]}\n {music[8]}\n {music[9]}",inline=False)
    embed.add_field(name="\u200b", value=f"{nsfw[0]}\n {nsfw[1]}\n {nsfw[2]}",inline=False)
    embed.add_field(name="\u200b", value=f"{anime[0]}\n {anime[1]}\n {anime[2]}\n {anime[3]}\n {anime[4]}\n {anime[5]}\n {anime[6]}\n {anime[7]}\n {anime[8]}\n {anime[9]}\n {anime[10]}\n {anime[11]}\n {anime[12]}\n {anime[13]}\n {anime[14]}\n {anime[15]}\n {anime[16]}\n {anime[17]}\n {anime[18]}\n {anime[19]}\n {anime[20]}\n {anime[21]}\n {anime[22]}\n {anime[23]}\n {anime[24]}\n {anime[25]}\n {anime[26]}\n {anime[27]}\n {anime[28]}\n {anime[29]}\n {anime[30]}\n {anime[31]}\n {anime[32]}" ,inline=False)
    # try:
    #     role = discord.utils.get(ctx.guild.roles, name="NSFW")
    #     if role in member.roles:
    #         embed.add_field(name="\u200b", value=f"{nsfw[0]}\n {nsfw[1]}\n {nsfw[2]}\n {nsfw[3]}\n {nsfw[4]}\n {nsfw[5]}\n {nsfw[6]}\n {nsfw[7]}\n {nsfw[8]}\n {nsfw[9]}\n {nsfw[10]}\n {nsfw[11]}\n {nsfw[12]}\n {nsfw[13]}\n {nsfw[14]}\n {nsfw[15]}",inline=False)
    #     else:
    #         embed.add_field(name="\u200b", value=f"{nsfw[0]}\n {nsfw[8]}\n {nsfw[15]}",inline=False)
    # except:
    #     embed.add_field(name="\u200b", value=f"{nsfw[0]}\n Can ONLY be accessed in a SERVER\n {nsfw[15]},inline=False")
    await member.send(embed=embed)
    await ctx.send(f"📬 You got mail")

#-------------------------------------------------------------------#

#--------------------------[Discord  Link]--------------------------#
@client.command()
async def joindiscord(ctx):
    member = ctx.author
    await member.send("Personal Streaming Server\n http://gestyy.com/w7ViEY")
    await ctx.send(f"📬 You got mail")
#-------------------------------------------------------------------#

#-------------------------[Discord  Invite]-------------------------#
@client.command()
async def invite(ctx):
    member = ctx.author
    await member.send("http://gestyy.com/w7ViTe")
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
                global nname
                nname = name.rsplit("-", 1)


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
        await ctx.send(f"Song Skipped")

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
    if ctx.voice_client is None:
        await ctx.send("Sir I am not in a channel")
    else:
        await ctx.send(f"Now Playing: {nname[0]}")

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
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
    count = (len([iq for iq in os.scandir('Google Drive Images/Images/General/Hello')]))
    max_num = count - 1
    num = randint(0,12)
    num = randint(0,max_num)

    sendimage = f'Google Drive Images\Images\General\Hello\hello({num}).gif'
    print(sendimage)
    member = ctx.author
    await ctx.send(f"{member.mention}",file=discord.File(sendimage))
#-------------------------------------------------------------------#

#-------------------------------[Anime]-----------------------------#

#To get link for image/gif from Imgur
def getLink(data):
    image_link = []

    config = configparser.ConfigParser()
    config.read('../auth.ini')

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    clienta = ImgurClient(client_id, client_secret)

    albums = configparser.ConfigParser()
    albums.read('./Imgur/Anime/' + data + '.ini')

    albums_dark = albums.get('anime','albums').split("\n")

    album_len = len(albums_dark)-1
    num = randint(0,5)
    num = randint(0,album_len)
    images = clienta.get_album_images(str(albums_dark[num]))
    for image in images:
        image_link.append(image.link)
    i = 0
    link_len = len(image_link)-1
    num = randint(0,link_len)

    return(image_link[num])

#Command for baka
@client.command(pass_context = True)
async def baka (ctx, member : discord.Member=None):
    image_link = getLink("baka")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Baka", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} is a baka (idiot for the uncultured swines that don't want anime).",embed=embed)

#Command for bang
@client.command(pass_context = True)
async def bang (ctx, member : discord.Member=None):
    image_link = getLink("bang")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Bang", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} is now dead. (Sorry couldnt come up with something good.)",embed=embed)
#Command for bite
@client.command(pass_context = True)
async def bite (ctx, member : discord.Member=None):
    image_link = getLink("bite")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Bite", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} has been bitten.",embed=embed)
#Command for blush
@client.command(pass_context = True)
async def blush (ctx, member : discord.Member=None):
    image_link = getLink("blush")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Blush", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Yo {member.mention}, {ctx.author.mention} be blushing.",embed=embed)
#Command for cuddle
@client.command(pass_context = True)
async def cuddle (ctx, member : discord.Member=None):
    image_link = getLink("cuddle")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Cuddle", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} better be ready to cuddle.",embed=embed)
#Command for dab
@client.command(pass_context = True)
async def dab (ctx, member : discord.Member=None):
    image_link = getLink("dab")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Dab", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} got dabbed on like a bitch (Im sorry for putting this as a description i hate my life)",embed=embed)
#Command for dance
@client.command(pass_context = True)
async def dance (ctx, member : discord.Member=None):
    image_link = getLink("dance")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Dance", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention}\n You have been challenged bitch!",embed=embed)
#Command for getfucked
@client.command(pass_context = True)
async def getfucked (ctx, member : discord.Member=None):
    image_link = getLink("getfucked")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Get Fucked", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} got fucked up!",embed=embed)
#Command for greet
@client.command(pass_context = True)
async def greet (ctx, member : discord.Member=None):
    image_link = getLink("greet")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Greet", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Hello {member.mention}-san!",embed=embed)
#Command for headbang
@client.command(pass_context = True)
async def headbang (ctx, member : discord.Member=None):
    image_link = getLink("headbang")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Headbang", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Dodge this {member.mention}-san!",embed=embed)
#Command for highfive
@client.command(pass_context = True)
async def highfive (ctx, member : discord.Member=None):
    image_link = getLink("highfive")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - High Five", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"High five {member.mention}!",embed=embed)
#Command for hug
@client.command(pass_context = True)
async def hug (ctx, member : discord.Member=None):
    image_link = getLink("hug")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Hug", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} better be prepared for this hug!",embed=embed)
#Command for kiss
@client.command(pass_context = True)
async def kiss (ctx, member : discord.Member=None):
    image_link = getLink("kiss")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Kiss", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"So {ctx.author.mention} kissed {member.mention}...",embed=embed)
#Command for lewd
@client.command(pass_context = True)
async def lewd (ctx, member : discord.Member=None):
    image_link = getLink("lewd")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Lewd", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"I dont know how to explain this {member.mention}...",embed=embed)
#Command for lick
@client.command(pass_context = True)
async def lick (ctx, member : discord.Member=None):
    image_link = getLink("lick")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Lick", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Um you got licked {member.mention}... I suggest you run!",embed=embed)
#Command for megumin
@client.command(pass_context = True)
async def megumin (ctx, member : discord.Member=None):
    image_link = getLink("megumin")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Megumin", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"EXPLOSIAN {member.mention}!",embed=embed)
#Command for nani
@client.command(pass_context = True)
async def nani (ctx, member : discord.Member=None):
    image_link = getLink("nani")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Nani", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} got hit with the NANI!",embed=embed)
#Command for neko
@client.command(pass_context = True)
async def neko (ctx, member : discord.Member=None):
    image_link = getLink("neko")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Neko...", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} I can't say shit",embed=embed)
#Command for nico
@client.command(pass_context = True)
async def nico(ctx, member : discord.Member=None):
    image_link = getLink("nico")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Nico", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention}, just accept it.",embed=embed)
#Command for nom
@client.command(pass_context = True)
async def nom (ctx, member : discord.Member=None):
    image_link = getLink("nom")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Nom", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} NOM",embed=embed)
#Command for owo
@client.command(pass_context = True)
async def owo (ctx, member : discord.Member=None):
    image_link = getLink("owo")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - OWO", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention}",embed=embed)
#Command for pat
@client.command(pass_context = True)
async def pat (ctx, member : discord.Member=None):
    image_link = getLink("pat")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Pat", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} has been patted by {ctx.author.mention}",embed=embed)
#Command for poke
@client.command(pass_context = True)
async def poke (ctx, member : discord.Member=None):
    image_link = getLink("poke")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Poke", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} has been poked! We can't say with what...",embed=embed)
#Command for punch
@client.command(pass_context = True)
async def punch (ctx, member : discord.Member=None):
    image_link = getLink("punch")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Punch", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} got punched..... LIKE A BITCH!",embed=embed)
#Command for rem
@client.command(pass_context = True)
async def rem (ctx, member : discord.Member=None):
    image_link = getLink("rem")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Rem", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} you have been remmmmmmmmmmed!",embed=embed)
#Command for slap
@client.command(pass_context = True)
async def slap (ctx, member : discord.Member=None):
    image_link = getLink("slap")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Slap", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{ctx.author.mention} has slapped {member.mention} like a bitch",embed=embed)
#Command for shrug
@client.command(pass_context = True)
async def shrug (ctx, member : discord.Member=None):
    image_link = getLink("shrug")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Slug", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention}",embed=embed)
#Command for sleepy
@client.command(pass_context = True)
async def sleepy (ctx, member : discord.Member=None):
    image_link = getLink("sleepy")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Sleepy", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} better be sleppy!",embed=embed)
#Command for stare
@client.command(pass_context = True)
async def stare (ctx, member : discord.Member=None):
    image_link = getLink("stare")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Stare", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{ctx.author.mention} is staring at {member.mention} (seriously idk what to put here)",embed=embed)
#Command for thumbsup
@client.command(pass_context = True)
async def thumbsup (ctx, member : discord.Member=None):
    image_link = getLink("thumbsup")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Thumbsup", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention}",embed=embed)
#Command for tickle
@client.command(pass_context = True)
async def tickle (ctx, member : discord.Member=None):
    image_link = getLink("tickle")
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Tickle", icon_url = client.user.avatar_url)
    embed.set_image(url=image_link)

    if member is None:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} like a bitch",embed=embed)
#-------------------------------------------------------------------#

#--------------------------------[NS-FW]----------------------------#
#Command for amateur
#Command for anal
#Command for asianporn
# @client.command(pass_context = True)
# async def asianporn (ctx):
#     role = discord.utils.get(ctx.guild.roles, name="NSFW")
#     member = ctx.author
#     if role in member.roles:
#         if ctx.channel.is_nsfw():
#             count = (len([iq for iq in os.scandir('Google Drive Images/Images/NSFW/asianporn')]))
#             max_num = count - 1
#             num = randint(0,12)
#             num = randint(0,max_num)
#
#             sendimage = f"Google Drive Images/Images/NSFW/asianporn/asianporn({num}).png"
#             await ctx.send(file=discord.File(sendimage, spoiler=True))
#         else:
#             member = ctx.author
#             await ctx.send(f"{member.mention} This command can only be used in NSFW chat.")
#     else:
#             await ctx.send(f"{member.mention} You need the NSFW Role sir")

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
    sendimage = "https://i.imgur.com/dwv4cP1.gif"
    print(sendimage)
    embed = discord.Embed()
    embed.set_author(name = "Feed_Ekko - Darkmeme", icon_url = client.user.avatar_url)
    embed.set_image(url="https://i.imgur.com/dwv4cP1.gif")
    await ctx.send(embed=embed)

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
    mycursor.execute("CREATE TABLE `"+ guild_id +"`.`twitch` ( `userid` VARCHAR(50) NOT NULL , `username` VARCHAR(50) NOT NULL , `twitch` VARCHAR(50) NOT NULL , PRIMARY KEY (`userid`))")
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

#-------------------------------------------------------------------#
#--------------------------[Twitch Commands]------------------------#
#-------------------------------------------------------------------#

#------------------------[Add User's Twitch]------------------------#
@client.command(pass_content=True)
async def addstreamer (ctx, member: discord.Member=None):
    guild_id = str(ctx.guild_id)
    author = ctx.author
    if member is None:
        return await ctx.send(f"{author.mention} The command is >addstreamer 'Twitch Username' ")
    else:
        mycursor = mydb.cursor()

        mydb.commit()
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#


#Assigns the bot to the token

client.run(token)
