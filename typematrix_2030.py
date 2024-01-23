
hwd_layout = dict()

for k in 'FN123' :
	hwd_layout[k] = list()
	for i in range(6) :
		hwd_layout[k].append(["1x075", 21 + i*21, 0])
	for i in range(7) :
		hwd_layout[k].append(["1x075", 7*21 + (i*21), 0])

print(hwd_layout)