import fileinput

indexMachine = 0
indexTotal = 1
data = {}

for line in fileinput.input():
	values = line.split('\t')
	machineID = int(values[indexMachine])
	total = int(values[indexTotal].replace("\n",""))
	temp = {int(machineID) : total}
	if machineID in data.keys():
		data[machineID] = data[machineID] + total
	else:
		data.update(temp)

print(data)