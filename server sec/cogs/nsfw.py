from discord.ext import commands
import threading
import aiofiles
import discord
import asyncio
import aiohttp
import random
import urllib
import ctypes
import re
import os
import json
import requests
from PIL import Image, ImageFont, ImageDraw

class Nsfw(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Nsfw Cog Online")

    @commands.command(pass_context=True)
    async def porn(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="Here ya Horny Freak", description="")
            embed.set_footer(text= f'Requested by {ctx.author}')

            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
                    res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title= f"Woah Woah There :smiling_imp:{ctx.author}:smiling_imp:\n This Command Is For **NSFW** Channels Only")
            await ctx.send(embed=embed)




    @commands.command(pass_context=True)
    async def feet(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="Here ya Horny Freak", description="")
            embed.set_footer(text= f'Requested by {ctx.author}')

            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/feetpics/new.json?sort=hot') as r:
                    res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title= f"Woah Woah There :smiling_imp:{ctx.author}:smiling_imp:\n This Command Is For **NSFW** Channels Only")
            await ctx.send(embed=embed)



    @commands.command(pass_context=True)
    async def ass(self,ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="Here ya Horny Freak", description="")
            embed.set_footer(text= f'Requested by {ctx.author}')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/ass/new.json?sort=hot') as r:
                    res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title= f"Woah Woah There :smiling_imp:{ctx.author}:smiling_imp:\n This Command Is For **NSFW** Channels Only")
            await ctx.send(embed=embed)



    @commands.command(pass_context=True)
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="Here ya Horny Freak", description="")
            embed.set_footer(text= f'Requested by {ctx.author}')

            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/hentai/new.json?sort=hot') as r:
                    res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title= f"Woah Woah There :smiling_imp:{ctx.author}:smiling_imp:\n This Command Is For **NSFW** Channels Only")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def boobs(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="Here ya Horny Freak", description="")
            embed.set_footer(text= f'Requested by {ctx.author}')

            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/boobs/new.json?sort=hot') as r:
                    res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title= f"Woah Woah There :smiling_imp:{ctx.author}:smiling_imp:\n This Command Is For **NSFW** Channels Only")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def pussy(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title="Here ya Horny Freak", description="")
            embed.set_footer(text= f'Requested by {ctx.author}')
                
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/pussy/new.json?sort=hot') as r:
                    res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title= f"Woah Woah There :smiling_imp:{ctx.author}:smiling_imp:\n This Command Is For **NSFW** Channels Only")
            await ctx.send(embed=embed)


   

def setup(client):
    client.add_cog(Nsfw(client))