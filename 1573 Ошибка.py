array =  map (int, input().split())
numbers = int(input())
count = 1
for i in range (numbers): 
    recipe = input()
    if recipe == "Blue":
        count*= array [0]
    if recipe == "Red":
        count*= array [1]
    if recipe == "Yellow":
        count*= array [2]
print (recipe)
