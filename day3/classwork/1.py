'''
Вводится последовательность из N чисел. Найти произведение и
количество положительных среди них чисел
'''
proizvedenie = 1
a = input().split(" ")
for i in range(0, len(a)):
    proizvedenie *= int(a[i])
print("Произведение " + str(proizvedenie))
print("Кол-во чисел " + str(len(a)))