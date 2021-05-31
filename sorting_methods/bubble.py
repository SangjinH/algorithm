# 시간복잡도는 가장 큰 값을 찾기위해 길이만큼 비교해야하기 때문에
# O(N^2) 시간복잡도를 가진다.


def bubble_sort(number_list):

    for i in range(len(number_list)):
        for j in range(len(number_list)-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]

    return number_list

arr = [1, 3, 5, 2, 7, 3, 5]
print(bubble_sort(arr))