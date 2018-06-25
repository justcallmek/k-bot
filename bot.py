# K bot by K

import discord
import random
import aiohttp
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='k ')

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="with itself"))
    print ("Ready player one")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))

@bot.command(pass_context=True)
async def invite():
  	await bot.say("Add me with this link {}".format(discord.utils.oauth_url(bot.user.id)))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def iam(ctx):
    await bot.say("Gay. Really, really gay.")

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Nah fam',
        'I dont think so',
        'Hmmmm. Hard to tell',
        'It is quite possible, peasant',
        'Definitely',
        'Pappi K says yes',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command(name='bread',
                description="Random bread duck meme",
                brief="Answers from the beyond.",
                pass_context=True)
async def bread(context):
    possible_responses = [
        '<:bread:459074070819110956> ***CRUMB FOR ME DADDY***',
        '<:bread:459074070819110956> ***LET ME WADDLE IN YO ASSHOLE***',
        '<:bread:459074070819110956> ***ALWAYS PEE AFTER SEX***',
        '<:bread:459074070819110956> ***I NUTELLAD ON YOUR GIRLS BUNS***',
        '<:bread:459074070819110956> ***Y’ALL GOT ANY BREAD***',
        '<:bread:459074070819110956> ***LEMME GIVE YOU THIS FRENCH STICK***',
        '<:bread:459074070819110956> ***I’LL PUT A BUN IN YOUR OVEN***',
    ]
    await bot.say(random.choice(possible_responses))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xFF0000)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("Adios, {}. Peasant.".format(user.name))
    await bot.kick(user)

bot.run("NDYwMzg5OTQ3ODkyMDM5Njgy.DhEIyg.O2vqQsKPF4ldoyM34oTZy9nDkNM")
