import discord, asyncio, os
import youtube_dl
import ffmpeg
from discord.ext import commands

intents = discord.Intents.all()
game = discord.Game("해킹")
bot = commands.Bot(command_prefix= '초다 ', intents=intents, status=discord.Status.online, activity=game)

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

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("음성채널에 접속중")

@join.error
async def join(ctx,error):
    await ctx.send(f'{ctx.author.mention}님이 음성채널에 접속중이 아니다냥.') #when voice channel doesn't joined(?)

@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()
    await ctx.send("음성채널에서 나갔다냥.")

@leave.error
async def leave(ctx,error):
    await ctx.send(f'{ctx.author.mention} 이미 음성채널에서 나갔다냥.')

@bot.command()
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("이미 일시중지 됐다냥.")
@bot.command()
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
       await ctx.send("이미 재시작 됐다냥.")

@bot.command()
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("노래가 플레이중이 아니다냥.")

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("해당 채널에 접속했다냥 -> " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@play.error
async def play(ctx,error):
    await ctx.send(f'URL 링크가 잘못되었거나, 다운로드에 오류가 났다냥.')

bot.run('MTA5NDUxMDMxNzE2NzQ2NDQ5OA.GxxUKx.PK6j3NxMryHTf1a8KzEITqSqZL-HUtc8Jo33bc')
