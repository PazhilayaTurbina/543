string = input()
count = 0
for i in range(len(string)): #суммируем очки за каждую букву, т.е нажатие на кнопку
    if string[i] in ("a", "d", "g", "j", "m", "p", " ", "s", "v", "y", "."):
        count += 1
    elif string[i] in ("b", "e", "h", "k", "n", "q", "t", "w", "z", ","):
        count += 2
    else:
        count += 3
print(count)
