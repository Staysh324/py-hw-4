def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def append_list(list, leng, num):
    numofelement = 1
    for i in range(leng):
        list_element = int(input(f"введите {numofelement}  элемент {num} списка: "))
        list.append(list_element)
        numofelement += 1
    return list


first_len = int(input("введите размер первого множества: "))
second_len = int(input("введите размер второго множества: "))
listone = []
listtwo = []
listone = append_list(listone, first_len, 1)
listtwo = append_list(listtwo, second_len, 2)
listone = set(listone)
listtwo = set(listtwo)
sets = listone.union(listtwo)
sets = list(sets)
print(quick_sort(sets))