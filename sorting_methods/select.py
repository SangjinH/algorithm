# 선택정렬
# 버블정렬과 비슷하지만 보다 개선된 정렬
# 버블정렬보다 일반적으로 두배빠름
# 그래도 시간복잡도는 O(N^2)

# 최소값을 찾고 인덱스를 기준으로 변경하기
def select_sort(number_list):

    # 맨 끝값은 제외, 정렬이 완료된 상태
    for i in range(len(number_list)-1):
        # 최소값이 위치한 인덱스 저장
        idx = i

        # 비교하는 건 끝값까지
        for j in range(i+1, len(number_list)):
            if number_list[j] < number_list[idx]:
                idx = j

        number_list[i], number_list[idx] = number_list[idx], number_list[i]

    return number_list


arr = [1, 3, 5, 2, 7, 3, 5]
print(select_sort(arr))
