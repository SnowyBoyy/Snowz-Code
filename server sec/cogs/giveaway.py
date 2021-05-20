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
from PIL import Image, ImageFont, ImageDraw

class Giveaway(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Giveaway Cog Online")

        @commands.command()
        @commands.has_permissions(kick_members=True)
        async def reroll(self, client, ctx, channel: discord.TextChannel, id_: int) :
            try :
                new_msg = await channel.fetch_message(id_)
            except :
                await ctx.send("The id was entered incorrectly.")
                return

            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            winner = random.choice(users)

            await channel.send(f"Congratulations! The new winner is {winner.mention}.!")


        @commands.command(aliases=['Giveaway', 'gstart'])
        @commands.has_permissions(kick_members=True)
        async def giveaway(self, client, ctx):
            emb = discord.Embed(
                color=16711680,
                title=None,
                description="Let's start with this giveaway! Answer these questions within 15 seconds!"

            )

            await ctx.send(embed=emb)
            questions = ["Which channel should it be hosted in?",

                        "What should be the duration of the giveaway? (s|m|h|d)",

                        "What is the prize of the giveaway?"]

            answers = []

            def check(m) :
                return m.author == ctx.author and m.channel == ctx.channel

            for i in questions :
                await ctx.send(i)

                try :
                    msg = await client.wait_for('message', timeout=15.0, check=check)
                except asyncio.TimeoutError :
                    emb = discord.Embed(
                        color=discord.Color(0xffff),
                        title=None,
                        description='You didn\'t answer in time, please be quicker next time!'

                    )

                    await ctx.send(embed=emb)

                    return
                else :
                    answers.append(msg.content)

            try :
                c_id = int(answers[0][2 :-1])
            except :

                emb = discord.Embed(
                    color=16711680,
                    title=None,
                    description=f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time."

                )

                await ctx.send(embed=emb)
                return

            channel = client.get_channel(c_id)

            time = convert(answers[1])
            if time == -1 :
                emb = discord.Embed(
                    color=16711680,
                    title=None,
                    description=f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!"

                )

                await ctx.send(embed=emb)

                return
            elif time == -2 :

                emb = discord.Embed(
                    color=16711680,
                    title=None,
                    description=f"The time must be an integer. Please enter an integer next time"

                )

                await ctx.send(embed=emb)
                return

            prize = answers[2]

            emb = discord.Embed(
                color=16711680,
                title=None,
                description=f"The Giveaway will be in {channel.mention} and will last {answers[1]}! Make sure to use the reroll command, when I get restarted"

            )

            await ctx.send(embed=emb)

            embed = discord.Embed(title="Giveaway!", description=f"Giveaway Prize is ->{prize}", color=16711680)

            embed.add_field(name="Hosted by:", value=ctx.author.mention)

            embed.set_footer(text=f"Ends {answers[1]} from now!")

            my_msg = await channel.send(embed=embed)

            await my_msg.add_reaction("🎉")

            await asyncio.sleep(time)

            new_msg = await channel.fetch_message(my_msg.id)

            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            winner = random.choice(users)

            message = await channel.send(f"Congratulations! {winner.mention} won {prize}!")

            emb = discord.Embed(
                title='🎊Giveaway🎉', description=f'Congratulations you won {prize} [here]({message.jump_url})', color=16711680
            )
            await winner.send(embed=emb)


        def convert(time) :
            pos = ["s", "m", "h", "d"]

            time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600 * 24}

            unit = time[-1]

            if unit not in pos :
                return -1
            try :
                val = int(time[:-1])
            except :
                return -2


        @reroll.error
        async def reroll_error(self, ctx, error) :
            if isinstance(error, commands.MissingRequiredArgument) :
                em = discord.Embed(title="<:x:805446555422425119> Reroll Error", color=16711680)
                em.add_field(name="Reason:", value="Missing Required Arguments!")
                em.add_field(name="Args:", value="```\nReroll <channel> <giveaway/message id>\n```")
                await ctx.send(embed=em)

   

def setup(client):
    client.add_cog(Giveaway(client))