#!/usr/bin/python
############################################################################################
############################################################################################
##   ___                                               __                                 ##
##  |   \     _    _ _____ _______ _______ ___    _   |  |     ____  _     _     _______  ##
##  | |\ \   | |  | |  ___|__   __|__   __|   \  | |  |  |    /  _  | |   | |   |__   __| ##
##  | | \ \  | |  | | |___   | |     | |  | |\ \ | |  |  |    | | | | |   | |      | |    ##
##  | |__\ \ | |  | |___  |  | |     | |  | | \ \| |  |  |    | | | | |   | |      | |    ##
##  |  __   \| \__/ |___| |  | |   __| |__| |  \   |  |  |____| |_| | |___| |______| |__  ##
##  |_|   \ _\\____/|_____|  |_|  |_______|_|   \__|  |_______\_____|_____|_____|_______| ##
##                                                                                        ##
##                                  Santa Clara University                                ##                  
##                                      COEN 177 Lab 3                                    ##
##                                     Second_Chance.py                                   ##
##                             Tested on Python 2.7.10 and 2.6.x                          ##
##                                                                                        ##
############################################################################################
############################################################################################

from random import randint
import sys, operator

pageframe = set()
table = []
pnum = 0
requests = 0
faults = 0
data = []
pages = int(sys.argv[1])


for line in sys.stdin:
        d = line.rstrip('\n')
        if(d.isdigit):
                data.append(d)

for i in range(0, len(data)):
        pnum = data[i]
        requests = requests + 1
        if(pnum in pageframe):
                continue
        elif(len(pageframe) < pages):
                pageframe.add(pnum)
		table.append(pnum)
		faults = faults + 1
		continue
        elif(len(pageframe) == pages):
        	x = randint(0, pages - 1)
		pageframe.remove(table.pop(x))    
		faults = faults + 1
                continue

print "Total requests: %d" % requests
print "Total faults: %d" % faults
	
