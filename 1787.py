povernuvshieCar, minute = map(int, input().split()) #5*3=15 машин, остальные машины встают в пробку
array = map(int, input().split())
probkaCar = 0
for podiehavshieCar in array:
    if podiehavshieCar <= povernuvshieCar:
        probkaCar -= povernuvshieCar-podiehavshieCar
        if probkaCar < 0:
            probkaCar = 0
    else:
        probkaCar += podiehavshieCar - povernuvshieCar
print(probkaCar)
