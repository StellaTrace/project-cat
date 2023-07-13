import asyncio
import discord
from youtube_dl import YoutubeDL

from discord.ext import commands

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
class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

def setup(client):
    client.add_cog(Music(client))
	
def __init__(self, client):
    option = {
            'format': 'bestaudio/best',
            'noplaylist': True,
        }
    self.client = client
    self.DL = YoutubeDL(option)

@bot.command(aliases=['음악재생'])
async def play_music(self, ctx, url):
		#봇의 음성 채널 연결이 없으면
    if ctx.voice_client is None: 
        # 명령어(ctx) 작성자(author)의 음성 채널에 연결 상태(voice)
        if ctx.author.voice:
            # 봇을 명령어 작성자가 연결되어 있는 음성 채널에 연결
            await ctx.author.voice.channel.connect()
        else:
            embed = discord.Embed(title = '오류 발생', description = "음성 채널에 들어간 후 명령어를 사용 해 주세요!", color = discord.Color.red())
            await ctx.send(embed=embed)
            raise commands.CommandError("Author not connected to a voice channel.")
    # 봇이 음성채널에 연결되어 있고, 재생중이라면
    elif ctx.voice_client.is_playing():
        # 현재 재생중인 음원을 종료
        ctx.voice_client.stop()
    await ctx.send(url)
    embed = discord.Embed(title = '음악 재생', description = '음악 재생을 준비하고있어요. 잠시만 기다려 주세요!' , color = discord.Color.red())
    await ctx.send(embed=embed)
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

# youtube 음악과 로컬 음악의 재생을 구별하기 위한 클래스 작성.
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
	
    player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "/drive/folders/1hBWtwQbOCenPzUrH1YPxO49C7iwuzfYI")
    ctx.voice_client.play(player)
    
    embed = discord.Embed(title = '음악 재생', description = f'{title} 재생을 시작힐게요!' , color = discord.Color.blue())
        await ctx.send(embed=embed)
bot.run("MTA5NDUxMDMxNzE2NzQ2NDQ5OA.GYqpry.t-pg0Vp1V9EDv2YoBdXK_KdnPwcKWq_Zpwh98Y")
