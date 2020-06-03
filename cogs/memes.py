import discord
import os
import configparser
from discord.ext import commands
from imgurpython import ImgurClient

# generate random integer values
from random import seed
from random import randint


class Memes (commands.Cog):

    def __init__(self, client):
        self.client = client


    #Command for meme
    @commands.command(pass_context = True)
    async def meme (self, ctx):
        image_link = []

        config = configparser.ConfigParser()
        config.read('../auth.ini')

        client_id = config.get('credentials', 'client_id')
        client_secret = config.get('credentials', 'client_secret')

        clienta = ImgurClient(client_id, client_secret)

        albums = configparser.ConfigParser()

        albums.read('./Imgur/Memes/meme.ini')
        albums_dark = albums.get('meme','albums').split("\n")

        album_len = len(albums_dark)-1
        num = randint(0,5)
        num = randint(0,album_len)
        images = clienta.get_album_images(str(albums_dark[num]))
        for image in images:
            image_link.append(image.link)
        i = 0
        link_len = len(image_link)-1
        num = randint(0,link_len)

        embed = discord.Embed()
        embed.set_author(name = "Feed_Ekko - Meme", icon_url = self.client.user.avatar_url)
        embed.set_image(url=image_link[num])
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Memes(client))
