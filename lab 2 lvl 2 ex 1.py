n1 = int(input('Введите количество мальчиков в классе'))
n2 = int(input('Введите количество девочек в классе'))
sum1 = float(0)
sum2 = float(0)
if n1 > 0:
    for i in range (1,n1+1):
        print('Введите рост', i, 'мальчика')
        rostmalchika = float(input())
        sum1 = sum1 + rostmalchika
else:
        print('В классе нет мальчиков')
if n2>0:
    for i in range(1,n2+1):
        print('Введите рост', i, 'девочки')
        rostdevochki = float(input())
        sum2 = sum2 + rostdevochki
else:
        print('В классе нет девочек')
if n1 > 0 and n2>0:
    print('Средний рост мальчиков в классе:0', sum1/n1,'','Средний рост девочек в классе:', sum2/n2)