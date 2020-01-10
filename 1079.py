from  functools import lru_cache

@lru_cache(maxsize=100000) 
def a(n):                   #Дерево Штерна — Броко
    if n<=0:
        return 0
    if n == 1:
        return 1
    if n%2 == 0:
        return a(n//2)
    i=(n-1)//2
    return a(i)+a(i+1)

def solve(n):
    return max((a(i) for i in range(0,n+1)))

def solve_multi(nn):
    for n in nn:
        yield solve(n)
        
def main(): #функция вывода результата
    while True:
        n=int(input())
        if n==0:
            return
        print(solve(n))
        
if __name__ == '__main__': #вывод результата
    main()
