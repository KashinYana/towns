fin = open('list_towns.txt', 'r')
fout = open('list_towns_for_database.txt', 'w')

listTowns = []

for line in fin:
	if len(line) > 0:
		line = line.strip().split(',')
		if len(line) >= 1:
			if len(listTowns) == 0 or listTowns[-1] != line[0]:
				fout.write(line[0] + "\n")
				listTowns.append(line[0])

fin.close()
fout.close()
