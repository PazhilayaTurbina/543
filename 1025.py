number = int(input())
array = list(map(int, input().split()))
array.sort()
count = 0
for i in range(number // 2+1): #так как необходимы голоса больше половины
    count += (array[i] // 2) + 1
print(count)
