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

class Server(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Server info Cog is online")
    
    @commands.command()
    async def ping(self, client, ctx):
        embed = discord.Embed(color = (1542362), description=f'My ping is: {round(client.latency * 1000)}ms')
        await ctx.send(embed=embed)

    @commands.command()
    async def mc(self, ctx):
        name = str(ctx.guild.name)
    

        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title= name + " member Count!",
    
            color = (1542362)
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name="Bot Total Servers", value=f'{len(self.client.guilds)}', inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['info'])
    async def serverinfo(self, ctx):
        total_text_channels = len(ctx.guild.text_channels)
        total_voice_channels = len(ctx.guild.voice_channels)
        total_roles = len(ctx.guild.roles)
        embed = discord.Embed(title=f'``{ctx.guild.name}`` Info!')
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name='Server Name:', value=f'{ctx.guild.name}')
        embed.add_field(name='Owner:', value=f'{ctx.guild.owner}')
        embed.add_field(name='Member Count:', value=f'{ctx.guild.member_count}')
        embed.add_field(name='Role Count:', value=total_roles)
        embed.add_field(name='Total Channels:', value=total_text_channels)
        embed.add_field(name='Total Voice Channels:', value=total_voice_channels)
        embed.set_footer(text=f'Requested By {ctx.author}')
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Server(client))