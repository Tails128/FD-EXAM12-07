import fileinput

indexMachine = 0
indexTotal = 1
currentindex = 1
total = 0


for line in fileinput.input():
	values = line.split('\t')
	machineID = int(values[indexMachine])
	if(machineID != currentindex):
		print(('{0}\t{1}'.format(currentindex, total)).replace("\n",""))		currentindex = machineID;
		total = 0;
	total += int(values[indexTotal].replace("\n",""))
print(('{0}\t{1}'.format(currentindex, total)).replace("\n",""))