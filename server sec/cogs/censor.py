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
blacklisted = []
with open('combined.txt') as file:
    file = file.read().split()
class Censor(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Censor Cog Is Online")
        blacklisted.clear()
    with open('combined.txt', 'r') as f:
        for x in f.readlines():
            blacklisted.append(x.replace('\n', ''))
    
   

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        else:
                for badword in file:
                    if badword in message.content.lower():
                        await message.delete()
                        await message.channel.send(f'Your Message Was Deleted For One of Two Reasons,\n One being You used a blacklisted word which is not allowed\n and Two You Pinged A No Ping Member')

    @commands.command()
    async def add(self, ctx, *, channel):
        if ctx.message.author.guild_permissions.administrator:
            try:
                global blacklisted
                blacklisted.append(str(channel).lower())
                with open('combined.txt', 'w') as f:
                    for x in blacklisted:
                        f.write(f'{x}' + '\n')
                f.close()
                embed = discord.Embed( description=f'The Word `{channel}` has been blacklisted.')
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description='An error has occurred while attempting to run this command!')
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete()



def setup(client):
    client.add_cog(Censor(client))