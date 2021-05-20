
from discord.ext import commands
import subprocess
import threading
import aiofiles
import discord
import asyncio
import aiohttp
import random
import ctypes
import re
import os


ctypes.windll.kernel32.SetConsoleTitleW('Server Security')
intents = discord.Intents().all()
client = commands.Bot(command_prefix='/', case_insensitive=False, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Servers: {len(client.guilds)}')
    for guild in client.guilds:
        print(guild.name)
    print()
    while True:
        activity = discord.Activity(type=discord.ActivityType.watching, name=f" {len(client.guilds)} servers! /help")
        await client.change_presence(activity=activity)

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


client.run("")
