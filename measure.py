import numpy
import os
import random
import time
#from pymongo import MongoClient#doesn't work for some reason

def temperature(x,y):
	'''This function one day should get the temperature from
	the sensor. Right now it returns a random value from [x,y]
	every 10 min. A crude preparation for mongodb is given.'''
	x = int (x)
	y = int (y)
	if y > x:
		return random.random()*(y-x)+x
	else:
		return random.random()*(x-y)+y
		
def humidity():
    return random.random()*100

if __name__ == '__main__':
	#print 'This program is being run by itself'
	#print os.getcwd()
	#print __name__
	#print temperatures(13,25)
	#print time.localtime()
	
	##If you do not specify any arguments to MongoClient, 
	##then MongoClient defaults to the MongoDB instance that 
	##runs on the localhost interface on port 27017:
	#client = MongoClient()
	#doesn't work for some reason
	
	meas = { 'time' : time.strftime("%a %b %Y %H:%M:%S +0000", time.localtime()),
	         'temp' : 10,
	         'RH'   : 50 
	       }
	
	while True:
		#get local time
		t = time.localtime()
		#print time.strftime("%a, %d %b %Y %H:%M:%S +0000", t)
		print int(time.strftime("%M", t))
		
		if int(time.strftime("%M", t)) in range(0,59,1):
			meas['temp'] = temperature(13,25)
			meas['RH']   = humidity()
			meas['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			print meas
			
		time.sleep(60)