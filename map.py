#!/usr/bin/python
import fileinput

indexIdMachine = 2
indexDowntime = 3

	for line in fileinput.input():
		values = line.split(';')
			idMachine = values[indexIdMachine]
			downtime = values[indexDowntime]
			print(('{0}\t{1}'.format(category, total)).replace("\n",""))