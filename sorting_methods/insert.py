# 삽입정렬
# Insertion Sort

def insert(number_list):
    for i in range(1, len(number_list)):
        j = i-1
        while j >= 0 and number_list[i] < number_list[j]:
            j -= 1

        number_list.insert(j+1, number_list[i])
        del number_list[i+1]

    return number_list

arr = [1, 3, 5, 2, 7, 3, 5]
print(insert(arr))