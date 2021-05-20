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

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog Online")

    @commands.command()
    async def penis(self, ctx):
        responses = ["8========================D, to big man",
    "*nothing lmao*",
    "8=====D, pretty normal",
    "8=D, hahaha small ass",
    "**it's a girl**",
    "**snowz size small**"]
        await ctx.send(f'Your pp size is \n lmaooo -> {random.choice(responses)}')
      

    @commands.command()
    async def topic(self, ctx):
        responses = ["Do You Like The Server?",
    "Are You Dating Anyone?",
    "Who is the fastest typer in the discord?",
    "How's quarantine going for you?",
    "Is life going good?",
    "Can you code?",
    "whats your favorite sport?",
    "do you play any sports?",
    "How did you come up with your discord name?",
    "Whats your favorite food?",
    "Have you had sex before?",
    "Is fortnite gay?",
    "What is the best game ever?",
    "What is the best streaming service?",
    "Will **Spotted** Hit 5k?",
    "Do you like the bot(s)?",
    "Do you Wanna learn To code?",
    "How was Your Day today?",
    "What Did you have for lunch/dinner today?",
    "how Old Are You?",]
        await ctx.send(f'Your Topic is \n  -> {random.choice(responses)}')
       


    @commands.command(pass_context = True)
    async def number(self, ctx):
        embed = discord.Embed(title = "Random number", description = (random.randint(1,1001)), color =1542362) 
        await ctx.send(embed = embed)
       

    @commands.command(aliases=['8ball'])
    async def eightball(ctx, *, question):
        responses = ["Yes",
    "No",
    "Maybe",
    "Only Time Will Tell",
    "Most Likely",
    "The Outlook Is Good.... *or is it*",
    "Don't Count On It...",
    "My Guess Is No",
    "You will Fail",
    "Succes is in the future \n \n \n \n SIKE I LIED YOUR FUTURE IS FRIED",
    "Asked My Buddys.. \n Its gonna be a no",]
        await ctx.send(f'{ctx.author}\n{random.choice(responses)}')
       

    @commands.command(pass_context=True)
    async def meme(self,ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
                
    @commands.command()
    async def hug(self,ctx, member : discord.Member):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/hug')
            hugjson = await request.json()
            
        embed = discord.Embed(title=f"{ctx.author} Is giving A Hug To {member}", color=16711680)
        embed.set_image(url=hugjson['link'])
        await ctx.send(embed=embed)
        

    @commands.command()
    async def pat(self,ctx, member : discord.Member):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/pat')
            hugjson = await request.json()

        embed = discord.Embed(title=f"Pat Pat Pat ->{member}", color=16711680)
        embed.set_image(url=hugjson['link'])
        await ctx.send(embed=embed)
        

    @commands.command(aliases=['av'])
    async def avatar(self,ctx, user: discord.Member = None) :
        if not user :
            user = ctx.author
        emb = discord.Embed(
            color=16711680,

            title=None,
            description=f"[Avatar Link]({user.avatar_url})")
        emb.set_image(url=f"{user.avatar_url}")
        await ctx.send(embed=emb)
       


    @commands.command()
    async def cat(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            dogjson = await request.json()

        embed = discord.Embed(title="Kitty Pic!", color=16711680)
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)
      





    @commands.command(aliases=['fp'])
    async def foodporn(self,ctx):
        embed = discord.Embed(title="Food!", description="Yummy!")
        embed.set_footer(text= f'Requested by {ctx.author}')

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/foodporn/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
                

    @commands.command(pass_context=True)
    async def pfp(self,ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/aesthetic/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def pfp1(self,ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/ProfilePics/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
               

    @commands.command(pass_context=True)
    async def anime(self,ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/AnimePFP/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
              


    @commands.command()
    async def dog(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()

        embed = discord.Embed(title="Doggo Pic!", color=16711680)
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def catfact(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request.json()

        embed = discord.Embed(title="Kitty Fact", text= factjson['fact'], color=16711680) 
        embed.add_field(name= "Here is a Cat Fact for ya", value= factjson['fact'])
        await ctx.send(embed=embed)
        


    @commands.command()
    async def dogfact(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request.json()

        embed = discord.Embed(title="Doggo Fact", text= factjson['fact'], color=16711680)
        embed.add_field(name= "Here is a Dog Fact for ya", value= factjson['fact'])
        await ctx.send(embed=embed)
       

    @commands.command()
    async def embed(self,ctx,*,message):
        embed = discord.Embed(color=16711680,description=f"{message}")
        msg=await ctx.channel.send(embed = embed)
        

    @commands.command()
    async def twitch(self, ctx,*,message):
        await ctx.send(f'https://www.twitch.tv/{message}')
       

    @commands.command()
    async def poll(ctx,*,message):
        embed = discord.Embed(color=16711680,description=f"{message}")
        msg=await ctx.channel.send(embed = embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
       

def setup(client):
    client.add_cog(Fun(client))