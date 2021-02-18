import discord
import asyncio
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from discord.ext import commands
global mode

bot = commands.Bot(command_prefix="~")
client = discord.Client()
version = 1.0
f = open(os.path.dirname(os.path.abspath(__file__)) + '\\abuse_list1.txt', "r", encoding='UTF8')
word_list1 = f.read()
word_list1 = list(word_list1.split('\n'))

@client.event
async def on_message(message):
    return None
    abuse_degree = 1
    chatuser = ""
    admin_id = ""

    if '~검열삭제' in message.content:
        await message.delete()
        if message.content[6:] in word_list1:
            word_list1.remove(message.content[6:])
            await message.channel.send('||' + message.content[6:] + '|| 이/가 삭제되었습니다')
        else:
            await message.channel.send('단어가 없습니다.')
        return None

    for i in range(len(word_list1)):
        if word_list1[i] in message.content.lower():
            await message.delete()
            await message.channel.send('<@' + str(message.author.id) + '> ||' + message.content + '||')
            return None

    if message.content == '~도움':
        await message.delete()
        embed = discord.Embed(color=0x6753ff)
        embed.set_author(name = '랍봇 (v' + str(version) + ')')
        embed.set_thumbnail(url = 'https://i.imgur.com/6LE8eOw.png')
        embed.add_field(name = '실행 가능한 명령어 모음', value = '~서버정보\n~도움\n~투표 (내용)\n~추방 (유저 이름)\n~밴 (유저 이름)\n~유저검색 (유저 이름)\n~스치유저검색 (유저 이름)\n~권한설정\n~별명변경 (다른 별명)\n~검열목록\n~검열추가 (단어)\n~검열삭제 (검열 단어)\n~명령어설정\n~코로나\n~코로나검색 (시 이름)\n~짤(짤 이름)\n~짤모음\n~짤추가(짤 이름)\n~짤삭제(짤 이름)\n~짤랜덤\n~인사말 변경', inline = False)
        embed.add_field(name = '개발자', value = '<@469008754097127434> 라비', inline = False)
        embed.add_field(name = '개발자 웹사이트', value = 'c11.kr/lnw6', inline = False)
        embed.add_field(name = '최초 제작일', value = '2020-8-14', inline = False)
        embed.add_field(name = '추가정보', value = 'c11.kr/lnw6', inline = False, url = 'c11.kr/lnw6')
        await message.channel.send(embed = embed)
        return None

    if message.content == '~역할글작성':
        await message.delete()
        await message.channel.send('표시될 글을 써주시거나, 이미지를 보내주세요.')


    if message.content == '~서버정보':
        await message.delete()
        embed = discord.Embed(color = 0x6753ff)
        embed.set_thumbnail(url = message.guild.icon_url)
        embed.add_field(name = '서버정보', value = '서버 이름 : ' + message.guild + '\n서버 인원 : ' + '\n서버 봇 : ' + '\n서버 들어왔던 사람 : ' + '\n서버 나간 사람 : ' + '\n서버 밴 된 사람 : ' + '\n서버 차단 된 사람 : ' + '\n서버 주인 : ' + '\n서버 최초 개설일 : ' + '\n서버 채팅 채널 : ' + '\n서버 음성 채널 : ' + '\n서버 카테고리 : ' + '\n서버 총 채널 : ' + '\n서버 삭제 된 채널 : ' + '\n서버 역할 : ' + '\n서버 부스트 : ', inline = False)
        await message.channel.send(embed = embed)
        return None

    if message.content == '~욕설':
        await message.channel.sent("~욕설검열설정, 등등이 있습니다.")

    if message.content == '~욕설검열설정':
        await message.channel.sent("레벨은 1, 2, 3 이 있습니다. 채팅으로 1, 2, 3 중 하나를 선택해주세요.")
        chatuser = message.author.id

    if message.content == "실험22":
        print(message.author.roles[2])

    if chatuser == message.author.id:
        chatuser = ""
        if message.content == '1':
            abuse_degree = message.content[4:]
            await message.channel.sent("욕설강도가 1로 설정되었습니다.")
        elif message.content == '2':
            abuse_degree = message.content[4:]
            await message.channel.sent("욕설강도가 2로 설정되었습니다.")
        elif message.content == '3':
            abuse_degree = message.content[4:]
            await message.channel.sent("욕설강도가 3으로 설정되었습니다.")
        else:
            await message.channel.sent("아무것도 선택하지 않으셨습니다.")

    if message.content == '~어드민설정':
        if mdmin_id 
        await message.channel.sent(word_list1)

    if '~투표' in message.content:
        await message.delete()
        await message.channel.send(message.content[4:])
        return None

    if message.content == '~검열목록':
        await message.delete()
        await message.channel.send('<@' + str(message.author.id) + '''>
||''' + ', '.join(word_list1) + '''||
            
검열 될 단어 목록입니다.''')
        return None

    if '~검열추가' in message.content:
        await message.delete()
        word_list1.append(message.content[6:])
        await message.channel.send('||' + message.content[6:] + '|| 이/가 추가되었습니다')
        return None
        
    if '~추방' in message.content:
        if message.content[4:]:
            await message.delete()
            await message.channel.send(message.content[4:] + '님이 추방되었습니다.')
            return None

    if '~시험' in message.content:
        await message.delete()

        name = input(message.content[4:])
        url = ("https://scratch.mit.edu/users/" + name + "/")
        response = urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')

        for i in soup.select("div.avatar"):
            icon = i.find("img")["src"]
        for i in soup.select("span.group"):
            group = i.get_text().strip('\n').strip(' ').split("\n")[0]
        for i in soup.select("span.location"):
            location = i.get_text()
        for i in soup.select("p.profile-details"):
            date = i.get_text().strip('\n').strip(' ').split("\n")[4].strip(' ')
        for i in soup.select("p.overview"):
            WhatImworkingon = str(i).replace('<br/>', '\n').replace('</p>', '').replace('<p class="overview">', '')
        for i in soup.select("div.about"):
            Aboutme = i.get_text()
            Aboutme = Aboutme[Aboutme.find('About me')+11 : Aboutme.find("What I'm working on")-3]
        for i in soup.select("div.box-head"):
            Aboutme = i.get_text()
        for i in soup.select("div.stage"):
            FeaturedProject = i.find("img")["src"]
        for i in soup.select("div.stage"):
            FeaturedProjecturl = "https://scratch.mit.edu" + i.find("a")["href"]

        response = urlopen("https://scratch.mit.edu/users/" + name + "/projects/")
        soup = BeautifulSoup(response, 'html.parser')

        for i in soup.select("div.portrait"):
            SharedProjects = i

        FavoriteProjects = 0
        following = 0
        followers = 0

        print(name + group + lang + url + icon)

        embed = discord.Embed(color=0x6753ff)
        embed.set_author(name= name + " | " + group + " | " + date + " | " + lang , url=url, icon_url=icon)
        embed.add_field(name="내 소개", value=Aboutme, inline=True)
        embed.add_field(name="내가 하고 있는 일", value=WhatImworkingon, inline=True)
        embed.add_field(name="특집 프로젝트", value=FeaturedProject, inline=True)
        embed.add_field(name="공유한 프로젝트 수", value=SharedProjects, inline=True)
        embed.add_field(name="좋아하는 프로젝트 수", value=FavoriteProjects, inline=True)
        embed.add_field(name="팔로잉한 수", value=following, inline=True)
        embed.add_field(name="팔로워 수", value=followers, inline=True)
        mbed.set_image(url="https://images.unsplash.com/photo-1585255318860-a65b32b03585?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")

        await message.channel.send(embed = embed)
        return None

@client.event
async def on_ready():
    print('랍봇 v' + str(version) + ' is ready')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('~도움'))

@client.event
async def on_member_join(member):
    await member.send(+ '님 안녕하세요. ' + + '에서 규칙을 숙지해주시기 바랍니다.')
f = open(os.path.dirname(os.path.abspath(__file__)) + '\\token.txt', 'r', encoding='UTF8')

client.run(f.read())