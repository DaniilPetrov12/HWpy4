from random import randint
kust =int (input('Введите количество кустов = '))
lst = list()
for i in range (kust):
    ygoda = randint(1,10)
    print (ygoda, end=' ')
    lst.append(ygoda)
print()
lst_2 = list()
for i in range(len(lst)):
    lst_2.append(lst[i-2] + lst[i-1] + lst[i],)
    print(lst_2, end = '\n')
print(max(lst_2))