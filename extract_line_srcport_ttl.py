from datetime import datetime as dt
import sys

#incomplete

file_name=sys.argv[1]
f = open(file_name,"r")
udp = []
tcp = []
other = []
for line in f:
	#print(int(line[0]))
	if((line[0]).isdigit()):
		l = line.split("|")
    #print(l[3])
		l[2] = int(l[2])
		if l[2] == 53:
			#print(l)
			l[4] = int(l[4])
			if l[4] == 6:
				s = "port number: "+ str(l[3])+ " TTL: "+ str(l[6]) +" Packet Count: "+(l[7].split(",")[1].split("\n")[0])
				tcp.append(s)
			elif l[4] == 17:
				s = ("port number: "+ str(l[3])+ " TTL: "+ str(l[6]) + " Packet Count: "+(l[7].split(",")[1].split("\n")[0]))
				udp.append(s)
			else:
				s = ("port number: "+ str(l[3])+ " TTL: "+ str(l[6]) + " Packet Count: "+(l[7].split(",")[1].split("\n")[0]))
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
