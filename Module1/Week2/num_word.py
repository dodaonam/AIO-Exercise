def word_count(filename):
    count = {}
    with open(filename, 'r') as file:
        lines = file.read().split()
        for word in lines:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    return count


print(word_count('P1_data.txt'))