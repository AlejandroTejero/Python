def select_unique_values(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    return result

print(select_unique_values([2, 2, 2, 2, 3, 3, 1, 2, 6, 7, 8, 9, 9, 10]))
print(select_unique_values(['one', 'two', 'one', 'two', 'three', 'one']))
