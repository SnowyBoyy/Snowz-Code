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
logs_channel = 841867523590586379
administrators = [821120781714063390]
class Logs(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Log Cog Is Online")
        channel = await self.client.fetch_channel(logs_channel)
        embed = discord.Embed(color=16711680,title= ":heavy_check_mark:Bot Awake And Ready For Use!")
        await channel.send(embed=embed)
    @commands.command()
    async def reload(self, ctx):
        if ctx.author.id in administrators:
            try:
                channel = await self.client.fetch_channel(logs_channel)
                embed = discord.Embed(color=16711680,description= ':heart:Bot Restarting!')
                await channel.send(embed=embed)
                await self.client.close()
            except:
                    embed = discord.Embed(description='An error has occurred while attempting to run this command!')
                    await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Logs(client))