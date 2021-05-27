from discord.ext import commands
import threading
import aiofiles
import discord
import asyncio
import aiohttp
import random
import ctypes
import re
import os
import json
import requests

class Servers(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Server setup Is Online")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setup(self, ctx):
        guild = ctx.guild
        message1= 'Server Setup Canclled, PUSSYYY'
        message2= 'Server Setup Canclled'
        message3= 'You Didnt See That'
        message4= 'Server Setup Canclled'
        msg1='Server Setting up.'
        msg2='Server Setting up..'
        msg3='Server Setting up...'
        msg4='Server Setting up.'
        msg5='Server Setting up..'
        msg6='Server Setting up...'
        await ctx.send('Make Sure All channels But **One** Are deleted,This Will make brand new ones, do you want to Continue (**Yes**/**No**) *Case Sensitive*')
        msg= await self.client.wait_for('message', check=lambda message:message.author == ctx.author and message.channel.id == ctx.channel.id)
        if msg.content in ("Y", "Yes"):
            msgg=await ctx.send('Server Setting Up')
            await msgg.edit(content=msg1)
            await asyncio.sleep(.1)
            await msgg.edit(content=msg2)
            await asyncio.sleep(.1)
            await msgg.edit(content=msg3)
            await asyncio.sleep(.1)
            await msgg.edit(content=msg4)
            await asyncio.sleep(.1)
            await msgg.edit(content=msg5)
            await asyncio.sleep(.1)
            await msgg.edit(content=msg6)
            info_channel = await ctx.guild.create_category("Important")
            await ctx.guild.create_text_channel("announcements")
            await ctx.guild.create_text_channel("Staff")
            await ctx.guild.create_text_channel("rules")
            await ctx.guild.create_text_channel("verify")
            await ctx.guild.create_text_channel("welcome-leave")
            await ctx.guild.create_text_channel("general")
            await ctx.guild.create_text_channel("bot-cmds")
            await ctx.guild.create_text_channel("counting")
            await ctx.guild.create_category("Chatting")
            await ctx.guild.create_category("Fun")
            await ctx.guild.create_category("VCS")
            await ctx.guild.create_voice_channel("Chatting")
            await ctx.guild.create_voice_channel("Gaming")
            await ctx.guild.create_voice_channel("Music")
            await ctx.guild.create_voice_channel("Staff VC")
            admin_channel = await ctx.guild.create_category("Staff")
            await ctx.guild.create_role(name="Mod")
            await ctx.guild.create_role(name="Admin")
            await ctx.guild.create_role(name="Member")
            await ctx.guild.create_role(name="Verified") 
            await ctx.guild.create_role(name="Vip")
            await ctx.guild.create_role(name="Owner")
            await ctx.send("Now you Must Rearange Channels, Make Role Permission and colors!")
            await admin_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), view_channel=False, send_messages=False, read_messages=False)
            await info_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), view_channel=True, send_messages=False, read_messages=True)
                        
        elif msg.content in ("N", "No"):
            message = await ctx.send(message1)
            await asyncio.sleep(1)
            await message.edit(content=message2)
            await asyncio.sleep(1)
            await message.edit(content=message3)
            await asyncio.sleep(2)
            await message.edit(content=message4)


def setup(client):
    client.add_cog(Servers(client))

