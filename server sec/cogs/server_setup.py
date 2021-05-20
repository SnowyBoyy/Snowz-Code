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


def setup(client):
    client.add_cog(Servers(client))