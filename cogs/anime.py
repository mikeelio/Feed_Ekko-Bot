import discord
import os
import configparser
from discord.ext import commands
from imgurpython import ImgurClient

# generate random integer values
from random import seed
from random import randint

class Anime (commands.Cog):

    def __init__(self, client):
        self.client = client

    #Command for baka
    @commands.command(pass_context = True)
    async def baka (self, ctx, member : discord.Member=None):
        image_link = getLink("baka")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Baka", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            try:
                await ctx.send(f"{member.mention} is a baka (idiot for the uncultured swines that don't want anime).",embed=embed)
            except:
                await ctx.send("That person does not exit. (Learn to spell)")

    #Command for bang
    @commands.command(pass_context = True)
    async def bang (self, ctx, member : discord.Member=None):
        image_link = getLink("bang")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Bang", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} is now dead. (Sorry couldnt come up with something good.)",embed=embed)
    #Command for bite
    @commands.command(pass_context = True)
    async def bite (self, ctx, member : discord.Member=None):
        image_link = getLink("bite")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Bite", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} has been bitten.",embed=embed)
    #Command for blush
    @commands.command(pass_context = True)
    async def blush (self, ctx, member : discord.Member=None):
        image_link = getLink("blush")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Blush", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Yo {member.mention}, {ctx.author.mention} be blushing.",embed=embed)
    #Command for cuddle
    @commands.command(pass_context = True)
    async def cuddle (self, ctx, member : discord.Member=None):
        image_link = getLink("cuddle")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Cuddle", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} better be ready to cuddle.",embed=embed)
    #Command for dab
    @commands.command(pass_context = True)
    async def dab (self, ctx, member : discord.Member=None):
        image_link = getLink("dab")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Dab", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} got dabbed on like a bitch (Im sorry for putting this as a description i hate my life)",embed=embed)
    #Command for dance
    @commands.command(pass_context = True)
    async def dance (self, ctx, member : discord.Member=None):
        image_link = getLink("dance")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Dance", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention}\n You have been challenged bitch!",embed=embed)
    #Command for getfucked
    @commands.command(pass_context = True)
    async def getfucked (self, ctx, member : discord.Member=None):
        image_link = getLink("getfucked")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Get Fucked", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} got fucked up!",embed=embed)
    #Command for greet
    @commands.command(pass_context = True)
    async def greet (self, ctx, member : discord.Member=None):
        image_link = getLink("greet")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Greet", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Hello {member.mention}-san!",embed=embed)
    #Command for headbang
    @commands.command(pass_context = True)
    async def headbang (self, ctx, member : discord.Member=None):
        image_link = getLink("headbang")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Headbang", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Dodge this {member.mention}-san!",embed=embed)
    #Command for highfive
    @commands.command(pass_context = True)
    async def highfive (self, ctx, member : discord.Member=None):
        image_link = getLink("highfive")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - High Five", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"High five {member.mention}!",embed=embed)
    #Command for hug
    @commands.command(pass_context = True)
    async def hug (self, ctx, member : discord.Member=None):
        image_link = getLink("hug")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Hug", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} better be prepared for this hug!",embed=embed)
    #Command for kiss
    @commands.command(pass_context = True)
    async def kiss (self, ctx, member : discord.Member=None):
        image_link = getLink("kiss")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Kiss", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"So {ctx.author.mention} kissed {member.mention}...",embed=embed)
    #Command for lewd
    @commands.command(pass_context = True)
    async def lewd (self, ctx, member : discord.Member=None):
        image_link = getLink("lewd")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Lewd", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"I dont know how to explain this {member.mention}...",embed=embed)
    #Command for lick
    @commands.command(pass_context = True)
    async def lick (self, ctx, member : discord.Member=None):
        image_link = getLink("lick")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Lick", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Um you got licked {member.mention}... I suggest you run!",embed=embed)
    #Command for megumin
    @commands.command(pass_context = True)
    async def megumin (self, ctx, member : discord.Member=None):
        image_link = getLink("megumin")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Megumin", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"EXPLOSIAN {member.mention}!",embed=embed)
    #Command for nani
    @commands.command(pass_context = True)
    async def nani (self, ctx, member : discord.Member=None):
        image_link = getLink("nani")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Nani", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} got hit with the NANI!",embed=embed)
    #Command for neko
    @commands.command(pass_context = True)
    async def neko (self, ctx, member : discord.Member=None):
        image_link = getLink("neko")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Neko...", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} I can't say shit",embed=embed)
    #Command for nico
    @commands.command(pass_context = True)
    async def nico(self, ctx, member : discord.Member=None):
        image_link = getLink("nico")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Nico", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention}, just accept it.",embed=embed)
    #Command for nom
    @commands.command(pass_context = True)
    async def nom (self, ctx, member : discord.Member=None):
        image_link = getLink("nom")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Nom", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} NOM",embed=embed)
    #Command for owo
    @commands.command(pass_context = True)
    async def owo (self, ctx, member : discord.Member=None):
        image_link = getLink("owo")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - OWO", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention}",embed=embed)
    #Command for pat
    @commands.command(pass_context = True)
    async def pat (self, ctx, member : discord.Member=None):
        image_link = getLink("pat")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Pat", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} has been patted by {ctx.author.mention}",embed=embed)
    #Command for poke
    @commands.command(pass_context = True)
    async def poke (self, ctx, member : discord.Member=None):
        image_link = getLink("poke")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Poke", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} has been poked! We can't say with what...",embed=embed)
    #Command for punch
    @commands.command(pass_context = True)
    async def punch (self, ctx, member : discord.Member=None):
        image_link = getLink("punch")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Punch", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} got punched..... LIKE A BITCH!",embed=embed)
    #Command for rem
    @commands.command(pass_context = True)
    async def rem (self, ctx, member : discord.Member=None):
        image_link = getLink("rem")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Rem", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} you have been remmmmmmmmmmed!",embed=embed)
    #Command for slap
    @commands.command(pass_context = True)
    async def slap (self, ctx, member : discord.Member=None):
        image_link = getLink("slap")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Slap", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.mention} has slapped {member.mention} like a bitch",embed=embed)
    #Command for shrug
    @commands.command(pass_context = True)
    async def shrug (self, ctx, member : discord.Member=None):
        image_link = getLink("shrug")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Slug", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention}",embed=embed)
    #Command for sleepy
    @commands.command(pass_context = True)
    async def sleepy (self, ctx, member : discord.Member=None):
        image_link = getLink("sleepy")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Sleepy", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} better be sleppy!",embed=embed)
    #Command for stare
    @commands.command(pass_context = True)
    async def stare (self, ctx, member : discord.Member=None):
        image_link = getLink("stare")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Stare", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.mention} is staring at {member.mention} (seriously idk what to put here)",embed=embed)
    #Command for thumbsup
    @commands.command(pass_context = True)
    async def thumbsup (self, ctx, member : discord.Member=None):
        image_link = getLink("thumbsup")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Thumbsup", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention}",embed=embed)
    #Command for tickle
    @commands.command(pass_context = True)
    async def tickle (self, ctx, member : discord.Member=None):
        image_link = getLink("tickle")
        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Tickle", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link)

        if member is None:
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{member.mention} like a bitch",embed=embed)

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

def setup(client):
    client.add_cog(Anime(client))
