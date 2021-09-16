import random

class chatreply:
	def __init__(self,cont):
		self.content=cont.content
		self.Message=''
		self.Type=''

	def reply(self):
		word=[i.lower() for i in self.content.split(' ')]
		print(word)
		if any(i=='?' for i in word) or any('?' in i for i in words ):
			self.Type='Question'

		c_nesa='nesamani' in word  or 'nesa' in word 
		c_hi=all(i in word for i in ['hi','nesamani']) or all(i in word for i in ['hi','nesa'])
		c_vanakkam=all(i in word for i in ['vanakkam','nesamani']) or all(i in word for i in ['vanakkam','nesa'])
		c_bye=all(i in word for i in ['bye','nesamani']) or all(i in word for i in ['bye','nesa'])
		c_call=all(i in word for i in ['dei','nesamani']) or all(i in word for i in ['dei','nesa'])
		c_kichina=any(i in word for i in ['chithappa','siththappu','chithappu'])
		c_whattodo=all(i in d for i in ['ippo','enna','panradhu'])
		c_disapp=all(i in word for i in ['inaikki gaali nee','nesamani']) or all(i in word for i in ['inaikki gaali nee','nesa']) or all(i in word for i in ['romba panra','nesamani']) 
		c_contract='contract' in word or 'contractu' in wor
		c_sad=any(i in word for i in ['sad','depressed','sogam','unhappy','saava','saaga'])

		if c_hi or c_vanakkam:
			self.Type='Reply'
			replies=['Sollra **Venna**','Vanakkam 🙏','*Ada Namma Paiyan*\n**Sollupa**',]
			self.Message=random.choice(replies)

		elif c_bye:
			self.Type='Reply'
			replies=['Torture panra Rascal , vitta kirukkan aakiruvanga pola','Nandri , Vanakkam 🙏','Vela solliye kollranga pa']
			self.Message=random.choice(replies)

		elif c_call:
			self.Type='Reply'
			replies=['Enthirichchi Teayap Podura En Venru','Vanakkam 🙏','*Ada Namma Paiyan*\n**Sollupa**']
			self.Message=random.choice(replies)
			
		elif c_nesa:
			self.Type='Reply'
			if len(word)==1:
				self.Message='Idho Vandhuttan !! \nhttps://cdn.discordapp.com/attachments/887634920770506752/887712177258111006/vadivelu-comedy.gif'
		
		elif c_kichina:
			self.Type='Reply'
			self.Message='Dei Kichinamoorthy ! Eppadra irukka ?'

		elif c_contract:
			self.Type='Reply'
			self.Message='Saami Thayavu Seinchu En Contractla Mattum Kai Vechchidaathinga'

		elif c_sad:
			self.Type='Reply'
			self.Message='Dei Enna Feeilinga !'

		elif c.c_whattodo:
			self.Type='Reply'
			self.Message='Oru Aani yum Pudunga Venam'

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