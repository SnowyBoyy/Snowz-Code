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

class Help(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog Is Online")
    
    @commands.command()
    async def link(self, ctx):
        embed = discord.Embed(color=16711680,description= 'Bot Invite link! invite this bot to your server for a cookie :)')
        embed.add_field(name= 'Server Security Bot Invite Link', value='https://discord.com/api/oauth2/authorize?client_id=839690922656792588&permissions=8&scope=bot')
        await ctx.send(embed=embed)
    

    @commands.command()
    async def credit(self, ctx):
        embed = discord.Embed(color=16711680,description= 'Credits!')
        embed.add_field(name= "Creator And Date",value='Credits to @$tupid $nowz#9999 For this Bot! It Was created On 5/5/2021!')
        embed.add_field(name= "Language + Commands",value= "This Bot Was Created In Python And has 30+ Commands!")
        embed.add_field(name= "Extra",value='The Bot Is Getting More Commands Added By The Day!')
        await ctx.send(embed=embed)
 

    
    @commands.command()
    async def help(self, ctx):
        if ctx.channel.type != discord.ChannelType.private:
            embed = discord.Embed(color=16711680, title="Server Security Commands")
            embed.add_field(name='Mod Commands', value='`/mod` - Shows **All** Mod Commands!', inline=False)
            embed.add_field(name='NSFWCommands', value='`/nsfw` - Shows **All** NSFW Commands!', inline=False)
            embed.add_field(name='Server commands', value='`/server` - Shows **All** Server Commands!', inline=False)
            embed.add_field(name='Fun Commands', value='`/fun` - Shows **All** Fun Commands!', inline=False)
            embed.set_footer(text="Coded By Stupid Snowz\n Note This Bot Is Basic And More Commands Will Be Added Later")
            await ctx.send(embed=embed)
            

    @commands.command()
    async def nsfw(self, ctx):
        embed = discord.Embed(color=16711680,description= "NSFW Commands")
        embed.add_field(name='Porn',value='`Usage /porn`')
        embed.add_field(name='Feet',value='`Usage /feet`')
        embed.add_field(name='Ass',value='`Usage /ass`')
        embed.add_field(name='Pussy',value='`Usage /pussy`')
        embed.add_field(name='Boobs',value='`Usage /boobs`')
        await ctx.send(embed=embed)
    


    @commands.command()
    async def mod(self, ctx):
        embed = discord.Embed(color=16711680,description= "Mod Commands")
        embed.add_field(name='Ban',value='`Usage /ban (member)(reason)`')
        embed.add_field(name='Kick',value='`Usage /kick (member)(reason)`')
        embed.add_field(name='Mute',value='`Usage /mute (member)(reason)`')
        embed.add_field(name='Purge',value='`Usage /purge (amount)`')
        embed.add_field(name='Slowmode',value='`Usage /slowmode (time in seconds)`')
        embed.add_field(name='Lock',value='`Usage /lock`')
        embed.add_field(name='Unban',value='`Usage /unban (member)`')
        embed.add_field(name='Unmute',value='`Usage /unmute (member)`')
        embed.add_field(name='Unlock',value='`Usage /unlock`')
        embed.set_footer(text="Coded By Stupid Snowz\n Note This Bot Is Basic And More Commands Will Be Added Later")
        await ctx.send(embed=embed)
     

    @commands.command()
    async def fun(self, ctx):
        embed = discord.Embed(color=16711680,description= 'Fun Commands')
        embed.add_field(name='Penis',value='`Usage /penis` \nShows PP Size')
        embed.add_field(name='Topic',value='`Usage /topic` \nGives A Random Topic To Talk About')
        embed.add_field(name='Poll',value='`Usage /poll (Poll/message)` \n sends Poll')
        embed.add_field(name='8ball',value='`Usage /8ball (question)` \n Gives A Response On Question')
        embed.add_field(name='Hug',value='`Usage /hug (member)`\n hugs member <3')
        embed.add_field(name='Embed',value='`Usage /embed (message)` \n Embeds Custom Message')
        embed.add_field(name='Dog',value='`Usage /dog` \n Doggo photos')
        embed.add_field(name='Dog Facts',value='`Usage /dogfact` \n Doggo facts')
        embed.add_field(name='Cat Photos',value='`Usage /cat` \n Kitty photos')
        embed.set_footer(text="Coded By Stupid Snowzn\n Note This Bot Is Basic And More Commands Will Be Added Later")
        await ctx.send(embed=embed)
       

    @commands.command()
    async def server(self, ctx):
        embed = discord.Embed(color=16711680,description= 'Server Info Commands')
        embed.add_field(name='Member Count',value='`Usage /mc` \nShows Server Member Count')
        embed.add_field(name='Credits',value='`Usage /credit` \nShows when Bot was Made And Who Made It')
        embed.add_field(name='Link',value='`Usage /link` \nSends Invite Link So Members Can Add Me To Their Server!')
        embed.set_footer(text="Coded By Stupid Snowz\n Note This Bot Is Basic And More Commands Will Be Added Later")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Help(client))