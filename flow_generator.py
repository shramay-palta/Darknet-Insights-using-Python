f = open("Plain Text.txt","r")
common_source = []
common_destination = []
dict1 = {}
dict2 = {}
for line in f:
    l = line.split("|")
    #print(l[3])
    if dict1.has_key(l[0]) == True:
    	try:
        	dict1[l[0]] = dict1[l[0]]+int(l[7].split(",")[1])
        except:
			print("An exception occurred") 
    else:
        try:
            dict1[l[0]] = int(l[7].split(",")[1])
        except:
			print("An exception occurred")
    if dict2.has_key(l[1]) == True:
    	try:
        	dict2[l[1]] = dict2[l[1]]+int(l[7].split(",")[1])
        except:
			print("An exception occurred")
    else:
    	try:
        	dict2[l[1]] = int(l[7].split(",")[1])
        except:
			print("An exception occurred")
for s in dict1:
    common_source.append(dict1[s])
for s in dict2:
    common_destination.append(dict2[s])
print(common_source)
print(common_destination)
f1 = open("same_source_ip1.txt","w+")
f2 = open("same_dest_ip1.txt","w+")
common_source.sort(reverse=True)
common_destination.sort(reverse=True)
for i in common_source:
    f1.write(str(i)+"\n")
for i in common_destination:
    f2.write(str(i)+"\n")
