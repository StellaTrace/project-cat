import asyncio
import discord
from discord.ext import commands,tasks
import os

intents = discord.Intents().all()
client = discord.Client(intents=intents)

game = discord.Game("해킹")
bot = commands.Bot(command_prefix='초다 ',intents=intents, status=discord.Status.online, activity=game)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command(aliases=['도움말'])
async def 도움(ctx):
    embed = discord.Embed(title="poskBot", description="설명", color=0x4432a8)
    embed.add_field(name="음성채널 입장", value="초다 play", inline=False)
    embed.add_field(name="노래 일시중지", value="초다 pause", inline=False)
    embed.add_field(name="음성채널 나가기", value="초다 leave", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['정보'])
async def informationofchoda(ctx):
    await ctx.send(f'{ctx.author.mention}, 나는 컴퓨터를 가지고 노는 고양이야.')

@bot.command(aliases=['유튜브채널'])
async def informationofchodayoutubechennel(ctx):
    await ctx.send(f'{ctx.author.mention}, https://www.youtube.com/@choda100')

@bot.command(aliases=['또다른유튜브채널'])
async def informationofchodasecondyoutubechennel(ctx):
    await ctx.send(f'{ctx.author.mention}, https://www.youtube.com/channel/UC1JEORrM7oPouwxoYeRKmjA')
    
@bot.command(aliases=['디스코드 서버'])
async def informationofchodadiscordserver(ctx):
    await ctx.send(f'{ctx.author.mention}, https://discord.com/invite/n5jfJYxwcP')

bot.run('MTA5NDUxMDMxNzE2NzQ2NDQ5OA.GxxUKx.PK6j3NxMryHTf1a8KzEITqSqZL-HUtc8Jo33bc')
