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
administrators = [821120781714063390]
class Logs(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Log Cog Is Online")
    @commands.command()
    async def reload(self, ctx):
        if ctx.author.id in administrators:
                await ctx.send('Restarting Bot!')
                await self.client.close()

def setup(client):
    client.add_cog(Logs(client))