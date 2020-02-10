from datetime import datetime as dt
f = open("dest_proto_feb_1to15.txt","r")
udp = []
tcp = []
other = []
for line in f:
	#print(int(line[0]))
	if((line[0]).isdigit()):
		l = line.split("|")
    #print(l[3])
		l[3] = int(l[3])
		if l[3] == 53:
			#print(l)
			l[4] = int(l[4])
			if l[4] == 6:
				s = "port number: "+ str(l[3])+ " Packet Count: "+(l[7].split(",")[1].split("\n")[0])
				tcp.append(s)
			elif l[4] == 17:
				s = ("port number: "+ str(l[3])+ " Packet Count: "+(l[7].split(",")[1].split("\n")[0]))
				udp.append(s)
			else:
				s = ("port number: "+ str(l[3])+ " Packet Count: "+(l[7].split(",")[1].split("\n")[0]))
				other.append(s)
	elif(line[0] is '#'):
		#if flag == 0:
		dt_object = dt.fromtimestamp(float(line.split(" ")[3]))
		#print(dt_object)
		tcp.append(str(dt_object))
		udp.append(str(dt_object))
		other.append(str(dt_object))	
	
print(tcp)
print(udp)
print(other)
