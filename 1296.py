number = int(input())
summa = 0
maximum = 0
for step in range(number): #суммируем выборку с 59 до 97
    input_number = int(input())
    summa += input_number
    if summa < 0:
        summa = 0
    maximum = max(summa, maximum)
print(maximum)
