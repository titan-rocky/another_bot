import sys
import discord
from discord.ext import commands
import random
import time
import asyncio
from datetime import datetime
import tracemalloc
import os
from alive import keep_alive


tracemalloc.start()

#Adra nesamani
bot=commands.Bot(command_prefix='nesa ')
bot.remove_command('help')
'''K A I P U L L A : dedicated for Type-A'''
@bot.event
async def on_ready():
	'''N E S A M A N I : dedicated for Type-A'''
	print('Ready to bell')
	print(bot.user)
	jd=random.randint(1,6)
	if jd==3:
		await bot.get_channel(887614433210302478).send('https://tenor.com/baf7V.gif')
	elif jd in [1,2,4,6]:
		await bot.get_channel(887614433210302478).send('Itho Vanthutten ...')
		if jd==4:
			await bot.get_channel(887614433210302478).send('https://tenor.com/y9h7.gif')

	p=random.randint(1,2)
	if p==1:
		await bot.change_presence(status=discord.Status.idle,activity=discord.CustomActivity(name='Dei Aprasandingalaa'))
	#if p==2:
	#	await bot.change_presence(activity=discord.Streaming(name="Your First Night", url='https://www.twitch.tv/titan_rocky'))
	if p==2:
		await bot.change_presence(activity=discord.Streaming(name="#Pray_For_Nesamani", url='https://www.twitch.tv/titan_rocky'))

	   #if bot.get(member.status == Status.online

@bot.event
async def on_message(message):
	d=[i.lower() for i in str(message.content).split()]
	if message.author == bot.user:
			return 1
	dx=str(message.content).lower()
	if dx.find('hareesh')!=-1:
		await message.channel.send('Call Him Sticker Sunniyan')
	if dx.lower().find('nesamani')!=-1:
		if dx.lower().find('hi nesamani')!=-1:
			await message.channel.send('Sollra **Venna**')
			#await message.channel.send(file=discord.File('vadivel_1.jpg'))
		elif dx.lower().find('bye nesamani')!=-1:
			await message.channel.send('Vela solliye kollranga ya !')
		elif dx.lower().find('dei nesamani')!=-1:
			await message.channel.send('Ey ey ! mariyadha mariyadha !')
		elif dx.lower().find('gopal')!=-1:
			await message.channel.send(f'Gopalu ! Gopalu !!')
		else:
			await message.channel.send('Dei Ennada Inge Meetingu ?')
	elif dx.lower().find('deepak')!=-1:
			await message.channel.send(f'Vandhuttana avan . Escapeeeeeeee !!!')

	if message.author.id==message.guild.owner_id:
		gox=random.randint(0,13)
		if gox==3:
			await message.channel.send('Dei Intha Aiyya Thanda Intha Veetukku Mainu')
			await message.channel.send('https://tenor.com/baf7N.gif')

	await bot.process_commands(message)

@bot.event
async def on_command_error(ctx,error):
	print(error)
	await ctx.send('Poda vendiyadha podra **Paradesi Payale**')
	await ctx.send('https://tenor.com/7KlK.gif')

@bot.command()
async def kill(ctx,*,ba):
	''' :  Kill All with Words'''
	g=ba.split(',')
	bas=g[0]
	#print(ba)
	#print(f'<@!799901775536062474>'==bas)
	gg=0
	if f'<@!799901775536062474>'==bas or bas.lower()=='nesamani':
		lis=[f'Ennaya da Kolla paakura {ctx.author.mention} ! Dei inaikku unna Kollama vida Maatan !']
		gg=1
	elif not (f'<@!{ctx.author.id}>'==ba) or not (ba.lower().find(ctx.author.name)):
		lis=[f'{bas} died due to the Corona Virus',
		f'{bas} tried to swim in Air after Seeing Shaktiman',
		f'{bas} rided A Female Horse. Bad idea though. It was too rough so that friction Heated the ||pp|| and it melted',
		f'<@{ctx.author.id}> Reaps {bas}\'s 8====D , Ultimately resulting in Fatality',
		f'{bas} Is in Bathroom , Suddently Funni appears .\nWhats next , inevitable Death only ',
		f'<@{ctx.author.id}> : Omae wa MOU SHINDE IRU\n{bas}  : NANI ?\n{bas} gets Disintegered :(',
		f'{bas} : You Can\'t Kill Me\n<@{ctx.author.id}> : I Know , But He Can\n{bas} was killed by **D R A G O** with **M 4 1 6**',
		f'**Kanaku Vaathi** : This boy {bas}\'s Heart , ummm....  , sin θ  is zero now :( ',
		f'Kekala la , Konjam saththama sollunga !',
		f'{bas} Suicided because **His Crush** didnt accept his proposal .',
		f'{bas} was slain by KiRiTo Kun with **Excalibur**',]

	else:
		lis=[f'neeye unna konnuttu enna seiya pora **Moodhevi** ! :( {ctx.author.mention}']
	index=random.randint(0,len(lis)-1);print(index)
	await ctx.send(lis[index])
	if gg==1:
		dd=await ctx.send('Suda Suda news Varudhu Paaru ')
		for i in range(2):
			await dd.edit(content='Suda Suda news Varudhu Paaru **.** ')
			await asyncio.sleep(0.85)
			await dd.edit(content='Suda Suda news Varudhu Paaru **. .** ')
			await asyncio.sleep(0.85)
			await dd.edit(content='Suda Suda news Varudhu Paaru **. . .** ')
			await asyncio.sleep(0.85)
		await ctx.send(f'{ctx.author.mention} Tried to Kill Me ,\nBut unfortunately He can\'t even Think of killing fully.\nHe died Brutually , Pity on him :rofl: ')
		await ctx.send('https://tenor.com/view/kick-vadivel-vadivelu-tamil-ramesh-gif-10667470')
	
	if ctx.message.content:
		pass
		#print(ctx.message.content)
	else:
		#print(ctx.message.content)
		await ctx.send(f'Poda vendiyadha podra **Paradesi Payale** <@{ctx.author.id}>')
		await ctx.send('https://tenor.com/7KlK.gif')

'''
@bot.command()
async def funnyface(ctx):
	''' : Funny Faces Of our Class Specimens'''
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
	col=[0x264653,0xa9d8f,0xe9c46a,0xf4a261,0xe76f51]
	l=random.randint(0,len(col)-1)
	ee='''Use prefix **nesa** to use commands of mine\n\nCommands:\n**nesa kill** : To kill Ya boys with Commands\n**nesa funnyface** : To Spend some time in posting random shitty\n            Images of Our Specimens\n**nesa help** : show this message '''
	e=discord.Embed(title='Help Command',desc=ee,color=col[l])
	e.set_author(name='Nesamani from TYPE A')
	e.add_field(name="\nPrefix:", value=ee)
	e.set_thumbnail(url='https://cdn.discordapp.com/attachments/800768867117826048/809715500258033664/friends.jpg')
	e.set_footer(text=f'Requested By {ctx.author.display_name} ')
	await ctx.send(embed=e)


'''
class kiruba(commands.cog): 
	def init(self,bot):
		self.bot=bot
'''




keep_alive()

TOKEN=os.environ['discord_token']
bot.run(TOKEN)


