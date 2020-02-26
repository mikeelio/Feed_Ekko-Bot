import discord
from discord.ext import commands

class Help (commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help (self, ctx):
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
        embed.set_author(name='Feed_Ekko Bot - Help and Documentation',icon_url=self.client.user.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url)
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

def setup(client):
    client.add_cog(Help(client))
