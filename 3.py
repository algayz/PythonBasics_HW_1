num = input("Введите номер вашего произдного билета, он состоит из шести чисел: ")
flag = True
while flag:
    if num.isdigit() != True or len(num) != 6:
        num = input("Введите пожалуйста корректный номер: ")
    else:
        flag = False
num = int(num)
a = num % 1000
b = num//1000
sum_a = (a//100)+((a//10) % 10)+(a % 10)
sum_b = (b//100)+((b//10) % 10)+(b % 10)
if sum_a==sum_b:
    print("Поздравляем! Вы выиграли!")
else:
    print("В следующей раз вам обязательно повезет;)")