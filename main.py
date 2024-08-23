a=('卍')
b=('квадрат')
c=('треугольник')
w=input('треугольник или квадрат?:')
if w==c:
    p=int(input('Размер ТР:'))
    for i in range(p): 
        print(a*i)
elif w==b:
    z=int(input('Размер КВ:'))
    for i in range(z):
        print(a*z)
else:
    print('иди нахуй')

