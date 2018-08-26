# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 23:17:07 2018

@author: allabwan
"""
# I think 840 is average stable state value
#function definitions:
#Defined the repeat function for the code to keep reading values after
#recoginzing a gesture.
def repeat():
    #all the code here
    while True:
    UpwardSpike = 0
    DownwardSpike = 0
    if port1 < 700:
            DownwardSpike = 1
            row = row + 20
    if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
            print "Looking left"
            repeat()
    
    if port1 > 900:
            UpwardSpike = 1
            row = row + 20
    if (UpwardSpike = 1) and (port1 < 600) and (port2 < 200):
            print "Looking down"
            repeat()

    if port1 < 700:
            DownwardSpike = 1
            row = row + 20
    if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
            print "Looking up"
            repeat()
            
    if port0 < 700 and port3 < 700 :
            DownwardSpike = 1
            row = row + 20
    if (DownwardSpike = 1) and (port1 > 900) and (port2 > 900):
            print "Looking Blink"
            repeat()
    
#End of function definition 
#Below is the main code

while True:
    UpwardSpike = 0
    DownwardSpike = 0
    if port1 < 700:
            DownwardSpike = 1
            row = row + 20
    if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
            print "Looking left"
            repeat()
    
    if port1 > 900:
            UpwardSpike = 1
            row = row + 20
    if (UpwardSpike = 1) and (port1 < 600) and (port2 < 200):
            print "Looking down"
            repeat()

    if port1 < 700:
            DownwardSpike = 1
            row = row + 20
    if (DownwardSpike = 1) and (port1 >) and (port2 > 200):
            print "Looking up"
            repeat()
            
    if port0 < 700 and port3 < 700 :
            DownwardSpike = 1
            row = row + 20
    if (DownwardSpike = 1) and (port1 > 900) and (port2 > 900):
            print "Looking Blink"
            repeat()

    
            
        
        
        