n, k = map(int, input().split())
minute = n / float(k) #если котлет больше чем вмещается на сковородке
if 0 < minute <= 1.0:
    print(2)
elif 0 < (minute - int(minute)) <= 0.5:
    print(int(minute) * 2 + 1)
elif 0.5 < (minute - int(minute)) < 1.0:
    print(int(minute) * 2 + 2)
else:
    print(int(minute) * 2)
