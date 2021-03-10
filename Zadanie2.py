kalkulator = input('''
Podaj jeden ze znakow dzialania:
+ dodawanie
- odejmowanie
/ dzielenie
* mnozenie
''')
nr1 = int(input('Podaj liczbe: '))
nr2 = int(input('podaj druga liczbe: '))
if kalkulator == '+':
    print('{} + {} = '.format(nr1, nr2))
    print(nr1 + nr2)

elif kalkulator == '-':
    print('{} - {} = '.format(nr1, nr2))
    print(nr1 - nr2)

elif kalkulator == '/':
    print('{} / {} = '.format(nr1, nr2))
    print(nr1 / nr2)

elif kalkulator == '*':
    print('{} * {} = '.format(nr1, nr2))
    print(nr1 * nr2)

else:
    print('Cos poszlo nie tak.')