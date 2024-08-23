import random 

nomber_0 = random.randint(1,2)
nomber_1 = random.randint(1,3)
nomber_2 = random.randint(1,5)
nomber_3 = random.randint(1,20)

While = 0

print ("Welcome to the casino 'Vulcan 777'")
coin = int(input('Please, insert your coins:'))
chance = int(input("What chace* you need: 50% = 2*  35% = 3*  20% = 4*  *5% = 5*"))
yes_no = input("Go? yes/no:").strip().lower()

while While == 0 :
    if yes_no == "no":
        break
    else:
        While += 1
        print ("Good luck!")

    if chance == 2 and nomber_0 == 2:
        result = (coin*2)
        print (f"U won! Your win: {result}")
    elif chance == 3 and nomber_1 == 3:
        result = (coin*3)
        print (f"U won! Your win: {result}")
    elif chance == 5 and nomber_2 == 5:
        result = (coin*4)
        print (f"U won! Your win: {result}")
    elif chance == 20 and nomber_3 == 20:
        result = (coin*5)
        print (f"U won! Your win: {result}")
    else:
        print (f"U lose! Your win: {result}")