import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
from datetime import datetime

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def ban(self,ctx,member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'The member {user.mention} is banned!')
        
    @commands.command()
    @has_permissions(administrator=True)
    async def mute(self,ctx,member : discord.Member, *, reason = None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        if discord.utils.get(ctx.guild.roles, name="Muted"):
            await member.add_roles(role)
        else:
            role = await ctx.guild.create_role(name='Muted', permissions=discord.Permissions(0))
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, overwrite=overwrite)
        await member.add_roles(role)
        await ctx.send(f'The member {user.mention} is muted!')
        
    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'The member {user.mention} is kicked!')
        
    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
            await ctx.send(f'The member {user.mention} is unbanned!')
            
    @commands.command()
    @has_permissions(administrator=True)
    async def unmute(self,ctx,member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(f"The member {user.mention} is unmuted!")
        
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self,ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)
        sent = await ctx.send(F"**{amount}** message(s) have been cleared! (message will be deleted in a few seconds)")
        sleep(2)
        await sent.delete()

def setup(client):
    client.add_cog(Moderation(client))
