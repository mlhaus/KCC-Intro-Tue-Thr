unique_lst = [ ]
max_dup = -1
lst= [1,2,2,3,4,5,6,7,8,8]
for i in range(len(lst)):
	if lst[i]>-1 and lst[i] in unique_lst:
		if lst[i] > max_dup:
		    max_dup = lst[i]
	else:
		unique_lst += [lst[i]]


print(max_dup)