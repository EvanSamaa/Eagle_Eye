# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 23:17:07 2018

@author: allabwan
"""
# I think 840 is average stable state value
#function definitions:
#Defined the repeat function for the code to keep reading values after
#recoginzing a gesture.
from csvreader import *
import csv
import numpy as np
import pickle
import matplotlib.pyplot as plt

def repeat(portList): #portlist = [port1, port2, port3, port4]
	#all the code here

	UpwardSpike = 0
	DownwardSpike = 0
	for dataPoint in portList: # iterate through in interval
		for i in range (4, 5):
			try:
				# print(UpwardSpike, DownwardSpike)
				if DownwardSpike > 0 and UpwardSpike > 0:
					print("Blink registered!")
					return 0
				elif (float(dataPoint[i]) > 1000):
					DownwardSpike = 1
				elif (float(dataPoint[i]) < 840) and (DownwardSpike > 0):
					UpwardSpike = UpwardSpike + 1
			except:
				kk = 3
# if False:
#     if port1 < 700:
#             DownwardSpike = 1
#             row = row + 20
#     if (DownwardSpike = 1) and (port1 > 600) and (port2 > 200):
#             print "Looking left"
#             repeat()
	
#     if port1 > 900:
#             UpwardSpike = 1
#             row = row + 20
#     if (UpwardSpike = 1) and (port1 < 600) and (port2 < 200):
#             print "Looking down"
#             repeat()

#     if port1 < 700:
#             DownwardSpike = 1
#             row = row + 20
#     if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
#             print "Looking up"
#             repeat()
			
#     if port0 < 700 and port3 < 700 :
#             DownwardSpike = 1
#             row = row + 20
#     if (DownwardSpike = 1) and (port1 > 900) and (port2 > 900):
#             print "Looking Blink"
#             repeat()

#End of function definition 
#Below is the main code
# def random():
# 	while True:
# 	UpwardSpike = 0
# 	DownwardSpike = 0
# 	if port1 < 700:
# 			DownwardSpike = 1
# 			row = row + 20
# 	if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
# 			print "Looking left"
# 			repeat()

# 	if port1 > 900:
# 			UpwardSpike = 1
# 			row = row + 20
# 	if (UpwardSpike = 1) and (port1 < 600) and (port2 < 200):
# 			print "Looking down"
# 			repeat()

# 	if port1 < 700:
# 			DownwardSpike = 1
# 			row = row + 20
# 	if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
# 			print "Looking up"
# 			repeat()
		
# 	if port0 < 700 and port3 < 700 :
# 			DownwardSpike = 1
# 			row = row + 20
# 	if (DownwardSpike = 1) and (port1 > 900) and (port2 > 900):
# 			print "Looking Blink"
# 			repeat()

	
 
info = getcsv("Blinks1.csv")
print (len(info)/256)
interval = 100
print(interval, "looks like:")
for i in range (0, len(info),interval):
	repeat(info[i: i + interval])
	

		
