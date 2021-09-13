import discord
import os
import random
from discord.ext import commands
from time import sleep

class Fun(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def joshua(self, ctx):
        await ctx.send(f'https://tenor.com/view/rachel-green-friends-joshua-joshuafriends-gif-13356999')


def setup(client):
    client.add_cog(Fun(client))
