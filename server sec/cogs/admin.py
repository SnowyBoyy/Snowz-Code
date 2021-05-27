from discord.ext import commands
import threading
import aiofiles
import discord
import asyncio
import aiohttp
import random
import urllib
import ctypes
import re
import os
import json
import requests
administrators = [821120781714063390]

class Admin(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin Cog Online")

    @commands.command()
    async def role(self,ctx, role: discord.Role, user: discord.Member):
        if ctx.author.guild_permissions.manage_roles:
            await user.add_roles(role)
            await ctx.send(f'{user.mention} was given {role.mention}')

    @commands.command()
    async def remove(self,ctx, role: discord.Role, user: discord.Member):
        if ctx.author.guild_permissions.manage_roles:
            await user.remove_roles(role)
            await ctx.send(f'{role.mention} was removed from {user.mention}')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def purge(self,ctx, amount=10000):
        await ctx.channel.purge(limit=amount)


    @commands.command(description="Mutes the specified user.")
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.manage_roles:
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")

            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")

                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

                await member.add_roles(mutedRole, reason=reason)
                await ctx.send(f"Muted {member.mention} for  {reason}")
                await member.send(f"You were muted in the server {guild.name} for {reason}")
 

        
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self,ctx, *, member):
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send (f'{member.mention} was **unbanned**')
                        return
        
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self,ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
        await ctx.send(ctx.channel.mention + " is now in lockdown.  ")
        

        
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self,ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(ctx.channel.mention +  f'Has been set to {seconds}')
        
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self,ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
        await ctx.send(ctx.channel.mention + " has been unlocked.")
        
            


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def kick(self,ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} Has Been **Kicked**')
     


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} Has Been **Bannned**')
    

def setup(client):
    client.add_cog(Admin(client))