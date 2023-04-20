def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# def append_list(list):
#     numofelement = 0
#     for i in range(len(list)):
#         list_element = int(input(f"введите элемент {numofelement}: "))
#         list.append(list_element)
#         numofelement += 1
#         return list


first_len = int(input("введите размер первого множества: "))
second_len = int(input("введите размер второго множества: "))
listone = []
listtwo = []
numofelement = 1
for i in range(first_len):
    list_element = int(input(f"введите {numofelement} элемент первого множества: "))
    listone.append(list_element)
    numofelement += 1
numofelement = 1
for i in range(second_len):
    list_element = int(input(f"введите {numofelement} элемент второго множества: "))
    listtwo.append(list_element)
    numofelement += 1
listone = set(listone)
listtwo = set(listtwo)
sets = listone.union(listtwo)
sets = list(sets)
print(quick_sort(sets))