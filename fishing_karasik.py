import random 

random_1 = random.randint (0,5)
random_2 = random.randint (0,5)
random_3 = random.randint (0,5)

While = 0
x = 2

print ("Добро пожаловать в клуб 'Karasik'")
print ("Для вас доступно 5 мест для заброса")

while While == 0:
    f = int(input("Куда бросаем?"))
    
    if f == random_1 and f == random_2 and f == random_3:
        print ("Поздравляю! Вы поймали редкую рыбу 'Goldkras'")
        break
    elif f == random_1 and f == random_2:
        print ("Поздравляю! Вы поймали рыбу 'Serikras'")
        break
    elif f == random_1:
        print ("Поздравляю! Вы поймали рыбу 'Karas'")
        break
    elif x == 0:
        print ("Попытки закончлись, ждем вас снова")
        break
    else:
        print (f"Упс! Кажется удача не на вашей стороне, но можете попробовать еще {x} раза")
        x -= 1