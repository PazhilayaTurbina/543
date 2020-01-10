def to_minutes(strt):
    hh, mm = map(int, strt.split('.'))
    return hh*60 + mm #переводим все часы в минуты
    
def get_data():
    dt1, at1 = input().split()
    dt2, at2 = input().split()
    dt1, at1, dt2, at2 = map(to_minutes,
    [dt1, at1, dt2, at2])
    return dt1, at1, dt2, at2 #получаем время вылета и прилета в минутах
    
def print_data(tzdiff):
    print(tzdiff)

def normalize_diff(diff): #функция указывающая на сложение или вычитание времени полета, так как время исчисляется в часах с 0 до 24
    while diff > 6*60:
        diff -= 24*60
    while diff < 0:
        diff += 24*60
    return diff
    
def calculate (dt1, at1, dt2, at2):
    for i in range(-5, 6):
        diff1 = normalize_diff(at1 - dt1 + i*60) #считаем время в полете прямого рейса
        diff2 = normalize_diff(at2 - dt2 - i*60) #считаем время в полете обратнго рейса
        if abs(diff2 - diff1) <=10: #сверяем разность в времени полета не более 10 минут как указано в условии задачи
            return abs(i)
    return None
    
def main():
    print_data(calculate(*get_data())) #главная функция вывода результата
    
if __name__ == '__main__': #вывод результата
    main() 
