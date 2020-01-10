n, k = map(int, input().split())
readyPc, hours = 1, 0 #так как пк на котором есть программа только 1
while readyPc < n and readyPc <= k: #так как 3 провода
	readyPc *= 2
	hours += 1
if readyPc < n:
	if (n-readyPc)%k == 0: #если нет остатка в пк
		hours += (n-readyPc)/k
	else:
		ostatok = (n-readyPc)%k #если есть остаток в пк
		hours += (n-readyPc-ostatok)/k + 1
print (int (hours))
