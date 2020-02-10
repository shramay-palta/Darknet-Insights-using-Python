f = open("src_april_10.txt","r")
f2 = open("datewise packet count on source tcp.txt","a+")
f3 = open("datewise packet count on source udp.txt","a+")
f4 = open("datewise packet count on source other.txt","a+")
udp = []
tcp = []
other = []
counter = 0
for line in f:
	line  = line[1:]
	line = line[:-1]
	if counter == 0:
		l = line.split(', ')
		for i in range(len(l)):
			l[i] = l[i][1:]
			l[i] = l[i][:-1]
			tcp.append(l[i])
	if counter == 1:
		l = line.split(', ')
		for i in range(len(l)):
			l[i] = l[i][1:]
			l[i] = l[i][:-1]
			udp.append(l[i])
	if counter == 2:
		l = line.split(', ')
		for i in range(len(l)):
			l[i] = l[i][1:]
			l[i] = l[i][:-1]
			other.append(l[i])
	counter = counter+1
#print(tcp)
#print(udp)
#print(other)
arr1 = tcp
for i in range(31):
	num = []
	for m in range(len(arr1)):
		#print(m,arr1[m])
		if m%3 == 0 and int(arr1[m][8:11]) == i+1:
			#print(arr1[m][8:11])
			st = arr1[m+1]
			st = st[29:]
			num.append(int(st))
			m = m+2
	sum_tcp=sum(num)
	if sum_tcp!=0:
		f2.write(str(i+1)+","+str(sum_tcp)+"\n")
	print("i:",i,"sum:",sum_tcp)
#print num

#print("TCP Packet count is")
#print sum_tcp

arr2 = udp

for i in range(31):
	num = []
	for m in range(len(arr2)):
		#print(m,arr1[m])
		if m%3 == 0 and int(arr2[m][8:11]) == i+1:
			#print(arr1[m][8:11])
			st = arr2[m+1]
			st = st[29:]
			num.append(int(st))
			m = m+2
	sum_tcp=sum(num)
	if sum_tcp!=0:
		f3.write(str(i+1)+","+str(sum_tcp)+"\n")
	print("i:",i,"sum:",sum_tcp)

arr3 = other
for i in range(31):
	num = []
	for m in range(len(arr3)):
		#print(m,arr3[m])
		
		if m%3 == 0 and int(arr3[m][8:11]) == i+1:
			#print(arr1[m][8:11])
			st = arr3[m+1]
			st = st[29:]
			num.append(int(st))
			m = m+2
	if sum_tcp!=0:
		f4.write(str(i+1)+","+str(sum_tcp)+"\n")
	sum_tcp=sum(num)
	print("i:",i,"sum:",sum_tcp)
