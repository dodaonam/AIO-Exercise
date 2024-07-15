def find_max_with_sliding_window(num_list, k):
    list_max = []
    for i in range(len(num_list) - k + 1):
        largest = num_list[i]
        for j in num_list[i:i+k]:
            if j > largest:
                largest = j
        list_max.append(largest)
    return list_max


print(find_max_with_sliding_window([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))