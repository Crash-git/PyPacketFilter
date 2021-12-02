#Claire Lavergne
import sys, csv

def parse(num):
	print('called parse function in packet_parser.py')
	L = []
	
	#file fields: 0 is num, 1 is time, 2 is source, 3 is dest, 4 is type, 5 is size, 6 is request or reply, 7 is id, 8 is seq, 9 is ttl, 10 is reply spot
	f = open("Node" + str(num) + "_filter.csv", 'r')
	reader = csv.reader(f, delimiter=",")
	included_cols = [0, 1, 2, 5, 6, 8, 9]

<<<<<<< HEAD
		for row in reader:
			content = list(row[i] for i in included_cols)
			if ("Echo (ping) request" in content[4]):
				content[4] = "8"
			elif ("Echo (ping) reply" in content[4]):
				content[4] = "0"
			L.append(content)
		print(L)
	return L
=======
	for row in reader:
		content = list(row[i] for i in included_cols)
		if ("Echo (ping) request" in content[4]):
			content[4] = "8"
		elif ("Echo (ping) reply" in content[4]):
			content[4] = "0"
		L.append(content)
	print(L)
	return L

parse()
>>>>>>> 0061abdd06bc753585c17312d8201176368419b3
