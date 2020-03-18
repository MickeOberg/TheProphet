import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from races import *
from classes import *
from builds import build_search


client = commands.Bot(command_prefix='!')
load_dotenv()




@client.command(name="race", help="Usage: !race <race> \nAvailable races: Breton, Redguard, Orc, Altmer, Bosmer, Khajiit, Nord, Dunmer, Argonian, Imperial")
async def race(ctx, *, name):
    if name:
        name = name.lower()
        if name in eso_desc:
            embed = discord.Embed(title=name.capitalize(), description=eso_desc.get(name), color=0x00ff00)
            embed.add_field(name="Alliance", value=eso_alliance.get(name), inline=False)
            embed.add_field(name="Passives", value=eso_passive.get(name), inline=False)
            embed.set_thumbnail(url=eso_raceimg.get(name))
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(f"```{name.capitalize()} is not a valid race.\nAvailable races are: Breton, Redguard, Orc, Altmer, Bosmer, Khajiit, Nord, Dunmer, Argonian, Imperial```")
    else:
        await ctx.channel.send(f"```Usage: !race <race>\nAvailable races are: Breton, Redguard, Orc, Altmer, Bosmer, Khajiit, Nord, Dunmer, Argonian, Imperial```") 

@client.command(name="info", help="Usage: !info <class>\nAvailable classes: Dragonknight, Nightblade, Sorcerer, Templar, Warden, Necromancer")
async def info(ctx, *, name):
    if name:
        name = name.lower()
        if name in eso_class:
            embed = discord.Embed(title=name.capitalize(), description=eso_class.get(name), color=0x00ff00)
            embed.add_field(name="Skill Lines", value=eso_classskill.get(name), inline=False)
            embed.add_field(name="Pro's", value=eso_classpro.get(name), inline=True)
            embed.add_field(name="Con's", value=eso_classcon.get(name), inline=True)
            embed.set_thumbnail(url=eso_classimg.get(name))
            embed.set_image(url=eso_classchar.get(name))
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(f"```{name.capitalize()} is not a valid class.\nAvailable classes are: Dragonknight, Nightblade, Sorcerer, Templar, Warden, Necromancer```")
    else:
         await ctx.channel.send(f"```Usage: !info <class>\nAvailable classes are: Dragonknight, Nightblade, Sorcerer, Templar, Warden, Necromancer```")

@client.command(name="alliance", help="Usage: !alliance <alliance> \nAvailable alliances: Daggerfall, Aldmeri, Ebonheart \nExample: !alliance Daggerfall")
async def alliance(ctx, *, name):
    if name:
        name = name.lower()
        if name in eso_allianceinfo:
            embed = discord.Embed(title=name.capitalize(), description=eso_allianceinfo.get(name), color=0x00ff00)
            embed.set_thumbnail(url=eso_allianceimg.get(name))
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(f"```{name.capitalize()} is not a valid alliance.\nAvailable alliances are: Daggerfall, Aldmeri, Ebonheart```")
    else:
        await ctx.channel.send(f"```Usage: !alliance <alliance>\nAvailable alliances are: Daggerfall, Aldmeri, Ebonheart```")



@client.command(name="builds", help="Usage: !builds <class> \nAvailable classes: Dragonknight, Nightblade, Sorcerer, Templar, Warden, Necromancer")
async def builds(ctx, *, name):
    if name:
        name = name.lower()
        if name in eso_class:
            beginner_builds, pvp_builds, pve_builds = build_search(name)
            embed = discord.Embed(title=name.capitalize(), description=eso_class.get(name), color=0x00ff00)
            embed.add_field(name="Beginner Guides", value="The following guides are beginner friendly", inline=False)
            for link, text in beginner_builds.items():
                embed.add_field(name=text, value=link, inline=True)
            embed.add_field(name="PvP Builds", value="The following builds are PvP oriented", inline=False)
            for link, text in pvp_builds.items():
                embed.add_field(name=text, value=link, inline=True)
            embed.add_field(name="PvE Builds", value="The following builds are PvE oriented", inline=False)
            for link, text in pve_builds.items():
                embed.add_field(name=text, value=link, inline=True)
            embed.set_thumbnail(url=eso_classimg.get(name))
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(f"```{name.capitalize()} is not a valid class.\nAvailable classes are: Dragonknight, Nightblade, Sorcerer, Templar, Warden, Necromancer```")
    else:
        await ctx.channel.send(f"```Usage: !builds <class>\nAvailable classes are: Dragonknight, Nightblade, Sorcerer, Templar, Warden, Necromancer```")


@client.command(name="ping", help="Latency test")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv("TOKEN"))
