nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls): # пузырьковая сортировка
    # чтобы цикл сработал хотя бы 1 раз, задаем значение переменной True
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i] # a, b = b, a
                # меняем значение переменной swap для следующего повтора цикла
                swap = True


bubble_sort(nums)
print(nums)


def selection_sort(ls): # сортировка выбором
    # i - количество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        low = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[low]:
                low = j
        # самый минимальный элемент меняем с первым элементом
        ls[i], ls[low] = ls[low], ls[i]


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)


selection_sort(nums)
print(nums)