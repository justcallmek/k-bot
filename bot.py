# Lil K bot by Kiedo

import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import random
import aiohttp
import asyncio
import os
import sys
import config
import youtube_dl

initial_extensions = [  # list of the cogs to load
    'ttt',
]

bot = commands.Bot(command_prefix="=", description="Lil K prefix")

@bot.command()
async def bot_cmd():
    await bot.say("This is in the main bot file")

if __name__ == '__main__':

    sys.path.insert(1, os.getcwd() + "/cogs/")  # Allows the cogs in the cogs folder to be loaded

    for extension in initial_extensions:
        bot.load_extension(extension)  # Adds the cogs listed in initial_extensions to the bot

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
async def oosh(ctx):
    await bot.say("https://i.imgflip.com/19yliy.jpg")

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
        'Pappi Widdy says yes',
    ]
    await bot.say(random.choice(possible_responses))

@bot.command(name='coinflip',
                description="Heads or tails",
                brief="Heads or tails",
                pass_context=True)
async def coinflip(context):

    possible_responses = [
        'Heads',
        'Tails',
    ]
    await bot.say(random.choice(possible_responses))

@bot.command(name='bread',
                description="Random bread duck meme",
                brief="Answers from the beyond.",
                pass_context=True)
async def bread(context):
    possible_responses = [
        '***CRUMB FOR ME DADDY***',
        '***LET ME WADDLE IN YO ASSHOLE***',
        '***ALWAYS PEE AFTER SEX***',
        '***I NUTELLAD ON YOUR GIRLS BUNS***',
        '***Y’ALL GOT ANY BREAD***',
        '***LEMME GIVE YOU THIS FRENCH STICK***',
        '***I’LL PUT A BUN IN YOUR OVEN***',
        '***YOUR GRANDMA FED ME BREAD LAST WEEK NIGGA***',
        ' ***BREAD IS JUST RAW TOAST***',
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
async def jazz(ctx, user: discord.Member):
    embed = discord.Embed()
    embed.set_image(url="https://i.imgur.com/OcQx7jN.gif")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hsr(ctx, user: discord.Member):
    embed = discord.Embed()
    embed.set_image(url="https://imgur.com/a/RzXDrwv")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def nou(ctx,):
    embed = discord.Embed(color=0xCCCCFF)
    embed.set_image(url="https://i.imgur.com/0KpVMqp.png")
    await bot.say(embed=embed)

bot.run(config.key)
