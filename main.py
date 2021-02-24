import discord

from datetime import datetime
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix="p/")

@client.event
async def on_member_join(member):
    channel = client.get_channel(750371106346762372)
    channel.send(f"{member.mention} sa práve pripojil! privítajte ho!")

@client.event
async def on_ready():
    print("Palko2 je ready :)")

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(color=0xff0000, title="Help")
    embed.add_field(name="p/help", value="Zobrazi toto :)")
    await ctx.send(embed=embed)

@client.command(name="clear")
@has_permissions(manage_messages=True)
async def clear_cmd(ctx, limit: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=limit)
    channel = client.get_channel(810407959033151548)
    if 100 <= limit:
        await channel.send(f"{ctx.author.mention} vymazal 100 sprav v {ctx.channel.mention}.")
    else:
        await channel.send(f"{ctx.author.mention} vymazal {limit} sprav v {ctx.channel.mention}.")

@client.command(name="say", pass_context=True)
@has_permissions(manage_messages=True)
async def say_cmd(ctx, channel : discord.TextChannel, color="", *,message=""):
    #channel = discord.utils.get(ctx.guild.channels, name=channel)
    #channel = client.get_channel(channel.id)

    x = str(tuple(int(color[i:i+2], 16) for i in (0, 2, 4)))
    RGB = ''.join(x).replace('(','').replace(')', '')
    r,g,b = RGB.split(',')
    c = discord.Colour.from_rgb(int(r),int(g),int(b))

    name, msg = message.split("|", 1)

    embed = discord.Embed(color=c, timestamp=datetime.utcnow())
    embed.add_field(name=name, value=msg)
    #embed.set_thumbnail(url=ctx.author.avatar_url)
    #embed.set_author(icon_url=guild.icon_url)
    embed.set_footer(text=ctx.author.name)
    await channel.send(embed=embed)

client.run(token)