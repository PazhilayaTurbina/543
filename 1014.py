number = int(input())
result = ""
if number == 0:
    print(10)
elif number == 1:
    print(1)
else:
    i = 9
    while i >= 2:
        while number % i == 0:
            result += str(i)
            number /= i #чтоб не было бесконечности
        i -= 1
    if number == 1:
        print(result)
    else:
        print(-1)
