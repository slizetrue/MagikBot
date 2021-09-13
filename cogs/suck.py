import discord
import os
import random
from discord.ext import commands
from time import sleep

class Fun(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def suckyourmum(self, ctx):
        await ctx.send(f'https://www.youtube.com/watch?v=e5nf4YhJ1Ww')


def setup(client):
    client.add_cog(Fun(client))
