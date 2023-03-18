a = int(input("Введите высоту шоколадки: "))
b = int(input("Введите ширину шоколадки: "))
c = int(input("Введите количество долек: "))

if c < b * a and (c % b == 0 or c % a == 0):
    print ("yes")
else:
    print("no")