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
##                                                                   			  ##
##				    Santa Clara University                                ##                  
##					COEN 177 Lab 3                                    ##
##                                          LFU.py                                        ##
##                             Tested on Python 2.7.10 and 2.6.x                          ##
##                                                                                        ##
############################################################################################
############################################################################################

import sys, operator

pageframe = {}
table = set()
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
	if pnum in table:	
		pageframe[pnum] = pageframe[pnum] + 1
		continue
	elif(len(table) < pages):
		table.add(pnum)
		pageframe[pnum] = 0
		faults = faults + 1
		continue
	elif(len(table) == pages): 
		index = 0
		lfu = 1000
		for i in table:
			if(pageframe[i] < lfu): 
				lfu = i
		del pageframe[lfu]
		table.remove(lfu)
		table.add(pnum)
		pageframe[pnum] = 0
		faults = faults + 1
		continue

print "Total requests: %d" % requests
print "Total faults: %d" % faults

#f.close()
