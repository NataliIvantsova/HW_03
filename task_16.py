# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих cтроках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Пример: n = 5; элементы 1 2 3 4 5; x = 3;


n = int(input('Введите размер элементов списка: '))
list_user = list(map(int, input('Введите элементы списка через пробел: ').split()))
if len(list_user) != n or n == 0:
    print('Введенные элементы не соответствуют заявленному размеру списка!')
else:
    x = int (input('Введите число х: '))
    count = 0
    for i in range(n):
        if list_user[i] == x:
            count += 1
    print(f'Число {x} встречается в списке А {count} раз.')