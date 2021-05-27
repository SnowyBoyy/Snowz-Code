from discord.ext import tasks
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
client = commands.Bot(command_prefix='/',case_insensitive=True, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Servers: {len(client.guilds)}')
    for guild in client.guilds:
        print(guild.name)
for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
@tasks.loop(seconds=3)
async def status_update():
    await client.wait_until_ready
    status_update.start()
    statuses = [f'{(len(client.users))} Members', f'{(len(client.guilds))} Servers', '/help']
    status = random.choice(statuses)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=status))

client.run("ODM5NjkwOTIyNjU2NzkyNTg4.YJNVHA.qChqNL2wd5p7qpagpEeuYG2d5Kg")
