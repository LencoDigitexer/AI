'''
Вводится последовательность из N чисел. Найти, сколько в ней
нулей и их порядковые номера.
'''
zero_q = 0
zero_serial_num = []
n = int(input("Введите кол-во чисел "))
for i in range(0, n):
    a = int(input())
    if a == 0: 
        zero_q =+ 1
        zero_serial_num.append(i)
print("Колличество нулей " + str(zero_q))
if zero_q > 0:
    print("Они находятся в порядке : ")
    for i in range(0, len(zero_serial_num)):
        print(zero_serial_num[i]+1, end=" ")
