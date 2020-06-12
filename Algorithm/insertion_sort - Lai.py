"""
Time: O(n^2)
Space: O(1)
"""
def selection_sort(list):
    """corner cases"""
    if list is None or len(list) == 0 or len(list) == 1:
        return list

    for i in range(1, len(list)):
        key = list[i]

        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    return list


print (selection_sort([5, 4, 1, 2]))  # 1 2 4 5