import discord
import os
import random
from discord.ext import commands
from time import sleep

class Fun(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def josh(self, ctx):
        await ctx.send(f'https://www.youtube.com/channel/UCYI6ZNNlu1vdaY7yzo1Z66w')


def setup(client):
    client.add_cog(Fun(client))
