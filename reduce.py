import fileinput

indexMachine = 0
indexTotal = 1
currentindex = 1
total = 0


for line in fileinput.input():
	values = line.split('\t')
	machineID = int(values[indexMachine])
	if(machineID != currentindex):
		print( currentindex + "\t" + currentsum);
		currentindex = machineID;
		total = 0;
	total += int(values[indexTotal].replace("\n",""))
	if machineID in data.keys():
		data[machineID] = data[machineID] + total
	else:
		data.update(temp)

print(data)