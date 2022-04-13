from datetime import datetime
import pytz
import csv

indtime=datetime.now(pytz.timezone('Asia/Calcutta'))
_time=indtime.strftime('%H:%M:%S')
_date=indtime.strftime('%Y-%d-%m')[:10]
_year=indtime.strftime('%Y')

def tickman(year,id):
	m=open('birthday.csv','r+',newline='')
	mb=[i for i in csv.reader(m)]
	print(mb)
	m.close()
	if not year in mb[0]:
		yearadd(year)
	dum=[i for i in mb[0]]
	inde=dum.index(f'{year}') #for i in ]if i==f'{year}'
	print(f'index={inde}')
	data=[]
	data.append(mb[0])
	for i in mb[1:]:
		if i[1]==id:
			i[inde]='1'
			print(i)
			data.append(i)
			print('done')
		else:
			data.append(i)
	print(data)
	m2=open('birthday.csv','w',newline='')		
	mb2=csv.writer(m2,delimiter=',')
	mb2.writerows(data)
	m2.close()
	

def yearadd(year):
	m=open('birthday.csv','r+',newline='')
	mb=[i for i in csv.reader(m)]
	m.close()
	data=[]
	mb[0]=mb[0]+[f'{year}']
	data.append(mb[0])
	for i in mb[1:]:
		i=i+['0']
		data.append(i)
	m2=open('birthday.csv','w',newline='')
	mb2=csv.writer(m2)
	mb2.writerows(data)
	m2.close()



def sendto(xdate,xyear):
	m=open('birthday.csv','r',newline='')
	dd=csv.reader(m)
	data=[i for i in dd]
	m.close()
	cc=indtime.strftime('%Y-%d-%m')[:10]
	for j in data[1:]:
		if f'{year}-{j[2]}-{j[3]}'==xdate:
			tickman(xyear,j[1])
			return j


def sendcheck(xdate,xyear):
	m=open('birthday.csv','r',newline='')
	dd=csv.reader(m)
	data=[i for i in dd]
	m.close()
	cc=indtime.strftime('%Y-%d-%m')[:10]
	dum=[i for i in dd[0]]
	inde=dum.index(f'{year}')
	for j in data[1:]:
		if f'{year}-{j[2]}-{j[3]}'==xdate and j[j.index(f'{year}')]=='0':
			tickman(xyear,j[1])
			return j
		

#sendto()

def yearof(date):
	m=open('birthday.csv','r',newline='')
	dd=csv.reader(m)
	m.close()

#tickman(_year,'557914347490508806')
#yearadd('2023')