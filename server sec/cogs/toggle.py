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


class Toggle(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Toggle Cog Is Online")

    @commands.command()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)

        if command is None:
            await ctx.send("Please State A Command To Turn On/Off!")
        
        elif ctx.command == command:
            await ctx.send('Cannot disable This cmd dummy')

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f'I have {ternary} {command.qualified_name} for you')

        
        


def setup(client):
    client.add_cog(Toggle(client))