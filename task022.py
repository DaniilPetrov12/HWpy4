from random import randint
num_1 = set(randint(1,20) for i in range(int(input('Введите количество элементов = '))))
print(num_1)
num_2 = set(randint(1,20) for i in range(int(input('Введите количество элементов = '))))
print(num_2)            
sor_num = sorted(num_1.intersection(num_2))
print(sor_num)