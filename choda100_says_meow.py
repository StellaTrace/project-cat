import asyncio
import discord
from discord.ext import commands

import asyncio
import discord
from discord.ext import commands,tasks
import os
import yt_dlp as youtube_dl

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
    embed.add_field(name="정보", value="초다 정보", inline=False)
    embed.add_field(name="유튜브채널", value="초다 유튜브채널", inline=False)
    embed.add_field(name="또다른유튜브채널", value="초다 또다른유튜브채널", inline=False)
    await ctx.send(embed=embed)
    embed.add_field(name="디스코드서버", value="초다 디스코드서버", inline=False)
    await ctx.send(embed=embed)

def check(reaction, user):
            return user == message.author

@bot.command(aliases=['정보'])
async def informationofchoda(ctx):
    await ctx.send(f'{ctx.author.mention}, 나는 컴퓨터를 가지고 노는 고양이야.')

@bot.command(aliases=['유튜브채널'])
async def informationofchodayoutubechennel(ctx):
    await ctx.send(f'{ctx.author.mention}, https://www.youtube.com/@choda100')

@bot.command(aliases=['또다른유튜브채널'])
async def informationofchodasecondyoutubechennel(ctx):
    await ctx.send(f'{ctx.author.mention}, https://www.youtube.com/channel/UC1JEORrM7oPouwxoYeRKmjA')

@bot.command(aliases=['디스코드서버'])
async def informationofchodadiscordserver(ctx):
    await ctx.send(f'{ctx.author.mention}, https://discord.com/invite/n5jfJYxwcP')


async def song_start(voice, url):
    try:
        if not voice.is_playing() and not voice.is_paused():
            ydl_opts = {'format': 'bestaudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f'https://www.youtube.com{url}', download=False) # 파일로 다운로드 하지 않고 재생
                URL = info['formats'][0]['url']
            
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        #voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg-4.4-full_build-shared/bin/ffmpeg.exe', source='./song.mp3'))

        while voice.is_playing() or voice.is_paused():
            await asyncio.sleep(0.1)
    except:
        return

@bot.command(aliases = ['play', 'p', 'ㅔ'])
async def Play(ctx,*,  keyword):
    try:
        results = YoutubeSearch(keyword, max_results=1).to_dict() # title과 url_suffix를 사용. 자세한 내용은 하단 링크 참고

        channel = ctx.author.voice.channel
        if bot.voice_clients == []:
            await channel.connect()
            #await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))
        voice = bot.voice_clients[0]
        
        await song_start(voice, results[0]['url_suffix'])
    except:
        await ctx.send("Play Error")


bot.run("MTA5NDUxMDMxNzE2NzQ2NDQ5OA.GYqpry.t-pg0Vp1V9EDv2YoBdXK_KdnPwcKWq_Zpwh98Y")
