fin = open('list_towns.txt', 'r')
fout = open('list_towns_for_database.txt', 'w')

for line in fin:
	if len(line) > 0:
		line = line.strip().split(',')
		if len(line) >= 1:
			fout.write(line[0] + "\n")

fin.close()
fout.close()
