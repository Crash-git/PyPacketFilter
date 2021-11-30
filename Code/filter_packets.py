
#Project 2
#filtering wiresharks for ICMP packets


def filter( filename, L) :
	f = open( filename + ".txt", 'r' )
	line = f.readline()

	while "\n" in line:
		if "ICMP" in line:
			if ("Echo (ping) reply") in line :
				splitline = line.strip().split()
				L.append(splitline)
				print(splitline)
			elif ("Echo (ping) request") in line :
				splitline = line.strip().split()	
				L.append(splitline)
				print(splitline)
		
		line = f.readline()
	if "Node1" in filename:
		writefile = open( filename + "_filter.txt", 'w' )	
		print("file made")


L = []
filter("Node1", L)

