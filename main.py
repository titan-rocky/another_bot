import sys
import discord
from discord.ext import commands, tasks

import random
import time
import asyncio

from datetime import datetime
import pytz

import tracemalloc
import os
from alive import keep_alive

import chatbot
import json

import csv
import testbir

tracemalloc.start()

#Adra nesamani
Intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=Intents)
bot.remove_command('help')
botguilds = [755751678971478049,
             887614433210302478]  #guilds'main channels PRIENDS,NP


@bot.event
async def on_ready():
    '''N E S A M A N I : dedicated for'''
    print('Ready to bell')
    print(bot.user)
    jd = random.randint(1, 6)
    indtime = datetime.now(pytz.timezone('Asia/Calcutta'))
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(
                                  name='Use @Nesamani help',
                                  start=indtime,
                                  end=datetime(indtime.year, indtime.month,
                                               indtime.day, 0, 0, 0)))
    guimem = bot.get_guild(887614433210302474)
    global gex
    gex = bot.get_guild(755751678531338303)
    '''
	if jd==3:
		await bot.get_channel(887614433210302478).send('https://tenor.com/baf7V.gif')
	elif jd in [1,2,4,6]:
		await bot.get_channel(887614433210302478).send('Itho Vanthutten ...')
		if jd==4:
			await bot.get_channel(887614433210302478).send('https://tenor.com/y9h7.gif')
	'''
    morning.start()
    birthday.start()
    #if bot.get(member.status == Status.online


@bot.event
async def on_message(message):
    d = [i.lower() for i in str(message.content).split()]
    if message.author == bot.user:
        return 1
    cxt = chatbot.chatreply(message)
    cxt.reply()
    if cxt.Message:
        await message.reply(f'{cxt.Message}')
    if message.author.id == message.guild.owner_id:
        gox = random.randint(0, 50)
        if gox == 3:
            await message.channel.send(
                'Dei Intha Aiyya Thanda Intha Veetukku Mainu')
            await message.channel.send('https://tenor.com/baf7N.gif')
    await bot.process_commands(message)


@tasks.loop(seconds=60)
async def morning():
    indtime = datetime.now(pytz.timezone('Asia/Calcutta'))
    b = indtime.strftime('%H:%M:%S')

    if b.startswith('00:30'):
        lb = [
            'Good Night Priends !',
            'Mallaakka Paduthu Vittathai Paakkurathu Evlo Sugam , Thoonga poren zzz'
        ]
        ddd = [i.status for i in gex.members if not (i.bot)]
        mo = [i != discord.Status.offline for i in ddd]
        bcount = mo.count(True)
        print(bcount)
        if bcount > 5:
        	#if more than 5 people are not sleeping
            await bot.get_channel(botguilds[0]).send(
                f'Ennada Innum **{bcount}** peru thoongama irukkinga ! Poi Thoongunga!\n**Udambukku nalladhu illa**'
            )
        else:
        	pass
        	#send good night
        	'''
            await bot.get_channel(botguilds[0]).send(random.choice(lb))'''

    elif b.startswith('06:00'):
    	#morning message
        '''lb2 = [
            'Adhukkulayum Vidinjiricha\nhttps://cdn.discordapp.com/attachments/887634920770506752/887634970049388594/goodm.gif\nKaalai Vanakkam',
            'Ellorukkum Iniya Kaalai Vanakkam !'
        ]
        await bot.get_channel(botguilds[0]).send(random.choice(lb2))'''
        pass

    elif b.startswith('00:00'):
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name="This Server"))

    elif b.startswith('06:00'):
        await bot.change_presence(status=discord.Status.idle,
                                  activity=discord.Game(name='@Nesamani help'))

    elif b.startswith('09:00'):
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="🔨 Hitting My Head"))

    elif b.startswith('12:00'):
        await bot.change_presence(status=discord.Status.idle,
                                  activity=discord.Streaming(
                                      name='Dei Apprasandingala',
                                      url='https://www.twitch.tv/titan_rocky'))

    elif b.startswith('18:00'):
        await bot.change_presence(activity=discord.Streaming(
            name="#Pray_For_Nesamani", url='https://www.twitch.tv/titan_rocky')
                                  )


@tasks.loop(seconds=3600)
async def birthday():
    channelid = 755751678971478049
    indtime = datetime.now(pytz.timezone('Asia/Calcutta'))
    b = indtime.strftime('%H:%M:%S')
    ttime = indtime.strftime('%H:%M:%S')
    tdate = indtime.strftime('%Y-%d-%m')[:10]
    tyear = indtime.strftime('%Y')
    cd = open('birthday.csv', 'r')
    data = [i for i in csv.reader(cd)]
    #check1
    if b.startswith('00'):
        a = testbir.sendto(tdate, tyear)
    elif b.startswith('12'):
        a = testbir.sendcheck(tdate, tyear)
    else:
        a = None
    if a:
        await bot.get_channel(channelid).send(
            f'<@&922184605434527845> ! **Attention Please** !\n Today is **<@{int(a[1])}>\'s** Birthday 🎂 🎉'
        )
        await bot.change_presence(status=discord.Status.idle,
                                  activity=discord.Streaming(
                                      name=f'Happy Birthday {a[0]} 🎂',
                                      url='https://www.twitch.tv/titan_rocky'))
        gmm=await bot.get_user(a[0])

        ee = '''இனிய பிறந்தநாள் நல்வாழ்த்துக்கள்!\nजन्मदिन की शुभकामनाएं !'''
        e = discord.Embed(title='Greetings from Me', desc=ee, color=0xA32EFF)
        e.set_author(name=f'Dear {a[0]}')
        e.add_field(
            name=
            f"\nWishing you a Many More Happy Returns of the Day **<@{gmm.mention}>**",
            value=ee)
        e.set_thumbnail(
            url=
            'https://cdn.discordapp.com/attachments/887634920770506752/964008939542958180/nesa.jpeg'
        )
        e.set_image(
            url=
            'https://cdn.discordapp.com/attachments/887634920770506752/964007907379282020/funny-animals-lol.gif'
        )
        e.set_footer(text=f'oru varudam pinbu sandhippom 🙏🏻')
        await bot.get_channel(755751678971478049).send(embed=e)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFoundError):
        await ctx.send('Appadi oru command uh Namma jilla laye illa')
        #await ctx.send('https://tenor.com/7KlK.gif')


@bot.command()
async def kill(ctx, *, ba):
    ''' :  Kill All with Words'''
    g = ba.split(',')
    print(g)
    bas = g[0]
    #print(ba)
    #print(f'<@!799901775536062474>'==bas)
    gg = 0
    if f'<@!799901775536062474>' == bas or bas.lower(
    ) == 'nesamani' or bas.lower() == 'nesa' or bas.lower() == 'yourself':
        lis = [
            f'Ennaya da Kolla paakura {ctx.author.mention} ! Dei inaikku unna Kollama vida Maatan !'
        ]
        gg = 1
    elif not (f'<@!{ctx.author.id}>' == ba) or not (ba.lower().find(
            ctx.author.name)):
        lis = [
            f'{bas} died due to the Corona Virus',
            f'{bas} tried to swim in Air after Seeing Shaktiman',
            f'{bas} rided A Female Horse. Bad idea though. It was too rough so that friction Heated the ||pp|| and it melted',
            f'<@{ctx.author.id}> Reaps {bas}\'s 8====D , Ultimately resulting in Fatality',
            f'{bas} Is in Bathroom , Suddently XoMbiE appears .\nWhats next , inevitable Death only ',
            f'<@{ctx.author.id}> : Omae wa MOU SHINDE IRU\n{bas}  : NANI ?\n{bas} gets Disintegered :(',
            f'{bas} : You Can\'t Kill Me\n<@{ctx.author.id}> : I Know , But He Can\n{bas} was killed by **D R A G O** with **M 4 1 6**',
            f'**Kanaku Vaathi** : This boy {bas}\'s Heart , ummm....  , sin θ  is zero now :( ',
            f'Kekala la , Konjam saththama sollunga !',
            f'{bas} Suicided because **His Crush** didnt accept his proposal .',
            f'{bas} was slain by KiRiTo Kun with **Excalibur**',
        ]
    elif ba.lower().find('myself'):
        lis = [
            f'neeye unna konnuttu enna seiya pora **Moodhevi** ! :( {ctx.author.mention}'
        ]
    else:
        lis = [
            f'neeye unna konnuttu enna seiya pora **Moodhevi** ! :( {ctx.author.mention}'
        ]
    index = random.randint(0,
                           len(lis) - 1)
    print(index)
    async with ctx.channel.typing():
        await asyncio.sleep(4)
    await ctx.send(lis[index])
    if gg == 1:
        dd = await ctx.send('Suda Suda news Varudhu Paaru ')
        for i in range(2):
            await dd.edit(content='Suda Suda news Varudhu Paaru **.** ')
            await asyncio.sleep(0.85)
            await dd.edit(content='Suda Suda news Varudhu Paaru **. .** ')
            await asyncio.sleep(0.85)
            await dd.edit(content='Suda Suda news Varudhu Paaru **. . .** ')
            await asyncio.sleep(0.85)
        await ctx.send(
            f'{ctx.author.mention} Tried to Kill Me ,\nBut unfortunately He can\'t even Think of killing fully.\nHe died Brutually , Pity on him :rofl: '
        )
        await ctx.send(
            'https://cdn.discordapp.com/attachments/887634920770506752/887708970339430480/kick-vadivel.gif'
        )

    if ctx.message.content:
        pass
        #print(ctx.message.content)
    else:
        #print(ctx.message.content)
        await ctx.send(
            f'Poda vendiyadha podra **Paradesi Payale** <@{ctx.author.id}>')
        await ctx.send('https://tenor.com/7KlK.gif')


'''
@bot.command()
async def funnyface(ctx):
	' : Funny Faces Of our Class Specimens'
	lis=['https://cdn.discordapp.com/attachments/800768867117826048/801859500242894949/PicsArt_01-21-10.32.38.jpg',
	'https://cdn.discordapp.com/attachments/800768867117826048/801859500789334016/PicsArt_01-21-10.27.21.jpg',
	'https://cdn.discordapp.com/attachments/800768867117826048/801859501040336936/PicsArt_01-21-10.21.13.jpg',
	'https://cdn.discordapp.com/attachments/800768867117826048/802187708096315433/PicsArt_01-22-08.17.17.jpg',
	'https://cdn.discordapp.com/attachments/800768867117826048/802187708403154954/PicsArt_01-22-08.13.06.jpg',
	'https://cdn.discordapp.com/attachments/800768867117826048/802222466264727612/PicsArt_01-22-10.35.19.jpg']
	dng=random.randint(0,len(lis)-1)
	await ctx.send(lis[dng])
'''


@bot.command()
async def help(ctx):
    col = [0x264653, 0xa9d8f, 0xe9c46a, 0xf4a261, 0xe76f51]
    l = random.randint(0, len(col) - 1)
    ee = '''Mention <@799901775536062474> to use commands of mine\n\nCommands:\n**<@799901775536062474> kill** : To kill Ya boys with Commands\n**<@799901775536062474> funnyface** : To Spend some time in posting random shitty\n            Images of Our Specimens\n**<@799901775536062474> tigerjoke** : jokes from palaya joke thangadurai\n**<@799901775536062474> help** : show this message '''
    e = discord.Embed(title='Help Command', desc=ee, color=col[l])
    e.set_author(name='Nesamani')
    e.add_field(name="\nPrefix:", value=ee)
    e.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/800768867117826048/809715500258033664/friends.jpg'
    )
    e.set_footer(text=f'Requested By {ctx.author.display_name} ')
    await ctx.send(embed=e)


@bot.command()
async def tigerjoke(ctx):
    file = open('tigergarden.json', 'r')
    cont = json.load(file)
    joke = random.choice(cont['jokes'])
    oe = discord.Embed(
        title='Tiger Thangadurai',
        color=0x57F287,
        description=
        'Warning ! Palaya Joke\nJokes from general , as well as KPY Champions',
        url='https://www.hotstar.com/in/tv/kpy-champions/14465')
    oe.set_author(name='Best-Picked Jokes of')
    oe.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/887634920770506752/887989766631596032/Tiger-Thangadurai-Images-6.jpg'
    )

    if joke['type'] == 'kadi':
        a = joke['content']
        b = joke['subcontent']
        oe.add_field(name=f"\n{a}", value=f'***Yen ?***\n{b}')
    elif joke['type'] == 'single':
        a = joke['dialogue']
        oe.add_field(name=f'Joke :', value=f'{a}')
    elif joke['type'] == 'qa':
        a = joke['question']
        b = joke['answer']
        oe.add_field(name=f'{a}', value=f'{b}')
    elif joke['type'] == 'convo':
        text = ''
        for i in range(1, 8):
            if f'line{i}' in joke:
                cx = joke[f'line{i}']
                text = text + f'{cx}' + '\n'
            else:
                break
        print(text)
        oe.add_field(name='Conversation :', value=text)

    await ctx.send(embed=oe)
    file.close()


'''
class kiruba(commands.cog): 
	def init(self,bot):
		self.bot=bot
'''

keep_alive()

TOKEN = os.environ['discord_token']
bot.run(TOKEN)
