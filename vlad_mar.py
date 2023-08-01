list_numbers = [3, 6, 4, 9, 8]
num_order = []
num_revers = []
n = 0
for i in list_numbers:
    n += 1
    if list_numbers[n] > list_numbers[n-1]:
        num_order.append(list_numbers[n])
        print(list_numbers[n])
    else:
        print('k')
print(list_numbers)
print(num_order)
