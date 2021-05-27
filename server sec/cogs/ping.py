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

class Censor(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Censor Cog Is Online")
  
    
   

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith(f"<@!{self.client.user.id}>") and \
            len(message.content) == len(f"<@!{self.client.user.id}>"):
                embed = discord.Embed(color=discord.Color.red(), description=f"Hi! My prefix is `/`\nUse `/help` to get started.")
                await message.channel.send(embed=embed) 





def setup(client):
    client.add_cog(Censor(client))