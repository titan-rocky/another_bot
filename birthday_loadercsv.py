import csv

def appends():
	a=open('birthday.csv','r+',newline='')
	b=csv.writer(a)
	b.writerow(['Name','dis_id','day','month','2022'])
	b.writerow(['jas',578286315594973205,'09','05','0'])
	b.writerow(['shylu',483138041251364864,'05','04','0'])
	b.writerow(['deepu',756797730143338516,'08','10','0'])
	b.writerow(['hari',683707288120590372,'14','11','0'])
	b.writerow(['sid',663735540264337419,'10','10','0'])
	b.writerow(['ans',756810477597753374,'17','10','0'])
	b.writerow(['kiri',679588706612805632,'23','03','0'])
	b.writerow(['thar',751322262573023273,'06','12','0'])
	b.writerow(['xombie',755807766601269290,'06','12','0'])
	b.writerow(['jaya',755458636431753358,'26','06','0'])
	b.writerow(['prat',629699453737238548,'27','03','0'])
	b.writerow(['sai',755372766789632000,'05','11','0'])
	b.writerow(['kokki',758563302434406430,'13','10','0'])
	b.writerow(['lolboy',690826217477242910,'06','02','0'])
	b.writerow(['test',557914347490508806,'13','04','0'])
	a.close()
'''
for i in a:
	print(i)
'''

appends()