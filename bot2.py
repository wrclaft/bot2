import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents=intents)   

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def rastgele_harf(ctx, *choices: str):
    choices = 'QWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç'
    await ctx.send(random.choice(choices))


bot.run("botun tokeni")
