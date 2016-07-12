#!/usr/bin/python
import fileinput

indexIdMachine = 2		#field IDMachine's position
indexDowntime = 3		#field downtime's position

for line in fileinput.input():				#read and split of the csv
	values = line.split(';')
	idMachine = values[indexIdMachine]		#mapping
	downtime = values[indexDowntime]
	print(('{0}\t{1}'.format(idMachine, downtime)).replace("\n",""))  #mapped output