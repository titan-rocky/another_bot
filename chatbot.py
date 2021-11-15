import random

class chatreply:
	def __init__(self,cont):
		self.content=str(cont.content)
		self.Message=''
		self.Type=''

	def reply(self):
		word=[i.lower() for i in self.content.split(' ')]
		print(word)
		if any(i=='?' for i in word) or any('?' in i for i in word ):
			self.Type='Question'

		name=['nesamani','nesa']
		c_nesa=any(i in word for i in name)
		c_vanakkam=any(i in word for i in name) and any(i in word for i in ['vanakkam','namaste','hi','hii','vanakko'])
		c_bye=any(i in word for i in name) and any(i in word for i in ['bye','kelamburan','byee','tata']) and len(word)==2
		c_call=any(i in word for i in name) and any(i in word for i in ['adei','dei','dai','yow','yo']) and len(word)==2
		c_kichina=any(i in word for i in ['chithappa','siththappu','chithappu'])
		c_whattodo=any(i in word for i in name) and all(i in word for i in ['ippo','enna','panradhu'])
		c_disapp=all(i in word for i in ['inaikki','gaali','nee','nesamani']) or all(i in word for i in ['inaikki','gaali','nee','nesa']) or all(i in word for i in ['romba panra','nesamani']) or all(i in word for i in ['inaikki','seththa','da','nee','nesamani']) 
		c_contract='contract' in word or 'contractu' in word
		c_sad=any(i in word for i in ['sad','depressed','sogam','unhappy','saava','saaga'])
		c_depart=any(i in word for i in name) and any(i in word for i in ['pogala','thoongala','kelambu','poda','po'])
		c_die=any(i in word for i in name) and any(i in word for i in ['saavu','die','seththu','sethu'])

		if c_vanakkam:
			self.Type='Reply'
			replies=['Sollra **Venna**','Vanakkam 🙏','*Ada Namma Paiyan*\n**Sollupa**','**marupadiyum modhalendha!**']
			self.Message=random.choice(replies)

		elif c_bye:
			self.Type='Reply'
			replies=['Torture panra Rascal , vitta kirukkan aakiruvanga pola','Nandri , Vanakkam 🙏','Vela solliye kollranga pa','Appada , ippo dhan Nimmadhi ya irukku ']
			self.Message=random.choice(replies)

		elif c_call:
			self.Type='Reply'
			replies=['Enthirichchi Teayap Podura En Venru','Vanakkam 🙏','*Ada Namma Paiyan*\n**Sollupa**','Kadupethuraru My Lord <@683707288120590372>']
			self.Message=random.choice(replies)
			
		elif c_nesa:
			self.Type='Reply'
			if len(word)==1:
				self.Message='Idho Vandhuttan !! \nhttps://cdn.discordapp.com/attachments/887634920770506752/887712177258111006/vadivelu-comedy.gif'
		
		elif c_kichina:
			self.Type='Reply'
			self.Message='Dei Kichinamoorthy ! Eppadra irukka ?'

		elif c_disapp or c_contract:
			self.Type='Reply'
			self.Message='Saami Thayavu Seinchu En Contractla Mattum Kai Vechchidaathinga'

		elif c_sad:
			self.Type='Reply'
			self.Message='Dei Enna Feeilinga !'

		elif c_whattodo:
			self.Type='Reply'
			self.Message='Oru Aani yum Pudunga Venam'
		elif c_depart:
			self.Type='Reply'
			self.Message='Naanga Povom Illa Ingaye Mallaka Padupom'

		elif c_die:
			self.Type='Reply'
			self.Message='Aaha kilambitaanya!!'

	#def username_check(self):
		#b=self.content.author.














'''
		if word.lower().find('nesamani')!=-1:
		if dx.lower().find('hi nesamani')!=-1:
			await message.channel.send('Sollra **Venna**')
			#await message.channel.send(file=discord.File('vadivel_1.jpg'))
		elif dx.lower().find('bye nesamani')!=-1:
			await message.channel.send('Vela solliye kollranga ya !')
		elif dx.lower().find('dei nesamani')!=-1:
			await message.channel.send('Ey ey ! mariyadha mariyadha !')
		elif dx.lower().find('gopal')!=-1:
			await message.channel.send(f'Gopalu ! Gopalu !!')
		elif dx.lower()=='nesamani':
			await message.channel.send(
	elif dx.lower().find('deepak')!=-1:
			await message.channel.send(f'Vandhuttana avan . Escapeeeeeeee !!!')
	
	if 
		await message.reply('Oru Aani yum Pudunga Venam')
'''