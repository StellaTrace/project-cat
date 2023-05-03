import discord, asyncio
from discord.ext import commands

intents = discord.Intents.all()
game = discord.Game("해킹")
bot = commands.Bot(command_prefix= '초다 ', intents=intents, status=discord.Status.online, activity=game)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(aliases=['정보'])
async def informationofchoda(ctx):
    await ctx.send(f'{ctx.author.mention}, 나는 컴퓨터를 가지고 노는 고양이야.')

@bot.command(aliases=['유튜브채널'])
async def informationofchodayoutubechennel(ctx):
    await ctx.send(f'{ctx.author.mention}, https://www.youtube.com/@choda100')

@bot.command(aliases=['또다른유튜브채널'])
async def informationofchodasecondyoutubechennel(ctx):
    await ctx.send(f'{ctx.author.mention}, https://www.youtube.com/channel/UC1JEORrM7oPouwxoYeRKmjA')


bot.run('MTA5NDUxMDMxNzE2NzQ2NDQ5OA.GxxUKx.PK6j3NxMryHTf1a8KzEITqSqZL-HUtc8Jo33bc')
