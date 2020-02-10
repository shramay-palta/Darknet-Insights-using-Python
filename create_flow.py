f = open("same_source_ip1.txt","r")
dict = {}

for l in f:
    #print(l[3])
    if dict.has_key(l) == True:
    	try:
        	dict[l] = dict[l]+1
        except:
			print("An exception occurred") 
    else:
        try:
            dict[l] = 1
        except:
			print("An exception occurred")
f2 = open("source_tuples1.txt","w+")
for s in dict:
	f2.write(str(int(s))+","+str(dict[s])+"\n")
