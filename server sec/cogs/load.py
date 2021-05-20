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
class Load(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Load Cog Is Online")

    @commands.command()
    async def load(self,ctx, extension):
        print(f'Loaded {extension}')
        if ctx.message.author.guild_permissions.administrator:
            try:
                self.client.load_extension(f'cogs.{extension}')
                embed = discord.Embed(description= f'``{extension}`` Has Been Loaded!')
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description='An error has occurred while attempting to run this command!')
                await ctx.send(embed=embed)

    @commands.command()
    async def unload(self,ctx, extension):
        print(f'Unlaoded {extension}')
        if ctx.author.id in administrators:
            try:
                self.client.unload_extension(f'cogs.{extension}')
                embed = discord.Embed(description= f'``{extension}`` Has Been Unloaded!')
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description='An error has occurred while attempting to run this command!')
                await ctx.send(embed=embed)

    @commands.command()
    async def restart(self,ctx,*, extension):
        print(f'Restarted {extension}')
        if ctx.author.id in administrators:
            try:
                self.client.unload_extension(f'cogs.{extension}')
                self.client.load_extension(f'cogs.{extension}')
                embed = discord.Embed(description= f'``{extension}`` Has Been restarted!')
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description='An error has occurred while attempting to run this command!')
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Load(client))