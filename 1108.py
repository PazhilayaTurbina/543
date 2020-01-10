n = int(input())
a = 2
for i in range(n):
	print (a)
	if i == n-1: #остановка если n=1
		break
	a = a**2 - a + 1 #не отдаем всю долю так как нужно отдать часть церкви
