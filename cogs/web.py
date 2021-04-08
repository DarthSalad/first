import discord
import json
import requests
import os
from discord.ext import commands
from googlesearch import search
from dotenv import load_dotenv

key = os.getenv('key')

class Web(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command(help="Lists the number of search results from the web as typed after gsearch")
    async def gsearch(self, ctx, n :int):
        await ctx.send("Type the search query")
        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await bot.wait_for("message", check=check)
        return_value=search(str(msg.content), tld='co.in', num=n, stop=n, pause=1)
        for j in return_value:
                await ctx.send(j)

    @commands.command(help='Type the YT search query and number fo results desired')
    async def yt(self, ctx, *, info):
        query = " ".join(info.split(" ")[0:-1]).replace(" ","+")
        num = int(info.split(" ")[-1])
        req = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={num}&q={query}&key={key}"
        response = requests.get(req)
        for item in response.json()["items"]:
            if item["id"]["kind"] == "youtube#playlist":
                await ctx.send("https://www.youtube.com/watch?v=temp&list="+item["id"]["playlistId"])
            elif item["id"]["kind"] == "youtube#video":
                await ctx.send("https://www.youtube.com/watch?v="+item["id"]["videoId"])

def setup(bot):
    bot.add_cog(Web(bot))