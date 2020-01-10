n1 = int(input())
g1 = set(input().split())
 
n2 = int(input())
g2 = set(input().split())
 
n3 = int(input())
g3 = set(input().split())
 
print(len(g1.intersection(g2,g3))) #находим совпадения у всех игроков вместе
