from discord.ext import commands
import discord
import re
import os
import json

from discord.ext.commands.errors import MissingPermissions


class Test(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Error Events ready")

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
            embed = discord.Embed(description=f'**{error}**')
            embed.set_footer(text='Idiot Lol')
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Test(client))
    