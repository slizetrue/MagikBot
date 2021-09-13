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
        await ctx.send(f'https://media.tenor.co/videos/6c233351834c6bf47b1aef59034ab5ec/mp4')


def setup(client):
    client.add_cog(Fun(client))
