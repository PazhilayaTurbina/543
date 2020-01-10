m, n = map(int, input().split())
if m*n%2: #для победы карлсону нужно ходить вторым при любом нечетном m*n 
    print("[second]=:]")
else:
    print("[:=[first]")
