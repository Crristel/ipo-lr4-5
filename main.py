num =int(input("Введите число:")) # вводим число 
sum=0 #создаём переменную суммы и присваиваем значение 0
for i in range(1, num+1): #создаём цикл и нужные условия 
    sum+=i # считаем сумму чисел 
print("Сумма чисел от 1 до числа, введённого вами = ",sum) # вывод на экран 
