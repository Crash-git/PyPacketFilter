def read_data ( document, List ):
	fr = open(document, 'r')
	line = fr.readline().strip()
	sub = "ICMP"
	
	while line:
		split_line =  line.split(' ')
		no = split_line[0]
		time  = split_line[1]
		#print(time.strip())
		#print(no.strip())
		source =  split_line[2]
		destination = split_line[3]
		protocol = split_line[4]
		length = split_line[5]
		info = split_line[6]
		#print(no)
		#print(time)
		#print(source)



		if(protocol == "ICMP"):
			#print(no)
			split_line[0] = no 
			split_line[1] = time  
			split_line[2] = source 
			split_line[3] = destination 
			split_line[4] = protocol 
			split_line[5] = length 
			split_line[6] = info 
			List.append(split_line)
		line = fr.readline().strip()
	fr.close

User_document = "Node1.txt"
L = []
read_data(User_document, L) 
#print(L)

