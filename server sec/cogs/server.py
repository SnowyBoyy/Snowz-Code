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
    async def ping(self, ctx):
        embed = discord.Embed(color = (16711680), description=f'My ping is: {round(self.client.latency * 1000)}ms')
        await ctx.send(embed=embed)

    @commands.command()
    async def mc(self, ctx):
        name = str(ctx.guild.name)
    

        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title= name + " member Count!",
    
            color = (16711680)
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
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=16711680, title='Server Name:', description=f'{ctx.guild.name}',inline=False)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name='Owner:', value=f'{ctx.guild.owner}',inline=False)
        embed.add_field(name='Creation Date', value=ctx.guild.created_at.strftime(date_format),inline=False)
        embed.add_field(name='Member Count:', value=f'{ctx.guild.member_count}',inline=False)
        embed.add_field(name='Role Count:', value=total_roles,inline=False)
        embed.add_field(name='Total Channels:', value=total_text_channels,inline=False)
        embed.add_field(name='Total Voice Channels:', value=total_voice_channels,inline=False)
        embed.set_footer(text=f'Requested By {ctx.author}')
        await ctx.send(embed=embed)
    @commands.command(aliases=['bot'])
    async def botinfo(self,ctx):
        servers = len(self.client.guilds)
        embed = discord.Embed(color=16711680, Title='Bot Info!')
        embed.add_field(name="Bot name:", value='Server Security#8952',inline=False)
        embed.add_field(name='Created By:', value='Stupid Snowz™#1337',inline=False)
        embed.add_field(name="Created on:", value='Made In Python, Created 5/5/2021',inline=False)
        embed.add_field(name='Servers:', value=servers,inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def servers(self,ctx):
        for guild in self.client.guilds:
            embed = discord.Embed(color=16711680, title='Server Names That I am in!')
            embed.add_field(name='Servers:',value=guild.name)
            await ctx.send(embed=embed)
            

    @commands.command(aliases=['userinfo','user','member','ui'])
    async def memberinfo(self, ctx,user: discord.User = None): 
            user = ctx.author
            roles = [role for role in user.roles]
            roles2 = (user.roles)
            avatar = (user.avatar_url)
             
            date_format = "%a, %d %b %Y %I:%M %p"
            embed = discord.Embed(color=16711680, title=f'User Info Below',inline=False)
            embed.set_author(name=f"{user}", url=avatar, icon_url=avatar)
            embed.add_field(name='Member:',value=f'{user}',inline=False)
            embed.add_field(name='Status:', value=user.status,inline=False)
            embed.add_field(name='Bot:', value=user.bot,inline=False)
            embed.set_thumbnail(url=avatar)
            embed.add_field(name='Roles:', value='->'.join([role.mention for role in roles]) ,inline=False)
            embed.add_field(name='Creation Date', value=user.created_at.strftime(date_format),inline=False)
            embed.add_field(name="Join Date:", value=user.joined_at.strftime(date_format),inline=False)
            embed.set_footer(text=f'ID ->{user.id}')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Server(client))