import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='~')
version = 1.0
chatuser = ""
admin_id = ""
abuse_degree = 1
welcome = 'none'
rule = 'none'

f = open(os.path.dirname(os.path.abspath(__file__)) + '\\abuse_list.txt', "r", encoding='UTF8')
word_list = f.read()
word_list = list(word_list.split('\n'))

def new_welcome_message(newwelcome, newrule):
    global welcome
    global rule
    welcome = newwelcome
    rule = newrule

@client.command()
async def 검열제외(ctx, word):
    await ctx.reply(f'`{word}` 을/를 검열목록에서 제외시켰습니다.')
    word_list.remove(word)

@client.command()
async def 검열목록(ctx):
    await ctx.reply('DM으로 메시지를 보내드렸습니다.', mention_author=False)
    await ctx.author.send('||' + ', '.join(word_list) + '||\n\n검열될 단어 목록입니다.\n욕설이 다수 포함되어 있을 수 있습니다.')

@client.command()
async def 핑(ctx):
    await ctx.reply(str(round(client.latency * 1000)) + 'ms')

@client.command()
async def 도움(ctx):
    embed=discord.Embed(title="추가적인 정보는 클릭해서 확인", url="https://lavi27.github.io/lavbot-website/cmd.html", color=0x6f6fff)
    embed.set_author(name="랍봇 도움", icon_url="https://i.imgur.com/6LE8eOw.png")
    embed.add_field(name="~검열제외", value=" 검열 할 단어중 원하는 단어를 제외", inline=False)
    embed.add_field(name="~검열목록", value=" 검열 할 단어 목록(DM전송)", inline=False)
    embed.add_field(name="~핑", value="ping 상태", inline=False)
    embed.add_field(name="~도움", value="도움", inline=False)
    embed.add_field(name="~서버정보", value="서버 정보", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def 서버정보(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 추방(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 밴(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 권한(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 닉변(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 어드설정(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 검열추가(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 명령추가(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 실험(ctx):
    await ctx.send(welcome)
    print(welcome)

@client.command()
async def 청소(ctx, num : int):
    if num >= 30:
        msg = await ctx.reply('30 이상의 수를 입력하셨습니다. 확실합니까?')
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    else:
        await ctx.channel.purge(limit=num)
        await ctx.send(f'{num}개의 메시지가 지워졌습니다.')

@client.command()
async def 환영(ctx, newwelcome, newrule):
    new_welcome_message(newwelcome=newwelcome, newrule=newrule)
    await ctx.send(f'환영 메시지를 {welcome}에서 {rule}에 대해 보내도록 설정했습니다.')

@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.online, activity = discord.Game('~도움'))
    print('랍봇 준비완료.')

@client.event
async def on_member_join(member):
    print(f"{member}안녕하세요.")

@client.event
async def on_member_remove(member):
    print(f"{member}22")

client.run(os.getenv('token'))