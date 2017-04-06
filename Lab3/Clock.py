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
##                                         Clock.py                                       ##
##                             Tested on Python 2.7.10 and 2.6.x                          ##
##                                                                                        ##
############################################################################################
############################################################################################

from collections import deque
import sys, operator

pageframe = deque()
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
        if pnum in table:
                for j in range(0, pages):
                        if(pageframe[j][0] == pnum):
                                pageframe[j][1] = 1
                                break
        elif(len(table) < pages):
                table.append(pnum)
                faults = faults + 1
                pageframe.append([pnum, 0])
        elif(len(table) == pages):
		while(True):
			if(pageframe[0][1] == 1):
				pageframe[0][1] = 0
				pageframe.rotate(-1)
			elif(pageframe[0][1] == 0):
        	        	table.remove(pageframe[0][0])
                		pageframe.popleft()
                		pageframe.appendleft([pnum, 0])
                		table.append(pnum)
                		faults = faults + 1
				break
				
print "Total requests: %d" % requests
print "Total faults: %d" % faults

