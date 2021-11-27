from itertools import combinations


def solution(num_str, k):

    answer = 10 ** len(num_str)

    idx_list = list(range(1, len(num_str)-1))
    candidates = list(combinations(idx_list, k))

    for i in candidates:
        temp = [0] + list(i) + [len(num_str)]
        total = 0

        for j in range(1, len(temp)):
            total += int(num_str[temp[j-1]:temp[j]])

        if total < answer:
            answer = total
            print(num_str)
            print(temp)
            print(total)

    return answer


print(solution("1234567", 2))
print(solution("991231567", 4))
print(solution("12351321", 5))
