n = int(input())
n *= 2
m = int(n**0.5) #14 = 2 + 3 + 4 + 5, арифм прогрессия с шагом 1

for i in range(m, -1, -1): #cоздаем ряд чисел для перебора
	if n%i == 0:
		k = n/i-i+1
		if k%2 == 0:
			print (int(k/2), i)
			break
#http://timus.coach/forum/thread.aspx?id=23030&upd=633985933469601250
