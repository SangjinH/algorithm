"""
OPO
PO
OP
P 단독
"""
def dec_to_k(number, k):

    k_number = ""

    while number >= k:
        temp = number % k
        k_number += str(temp)
        number //= k

    if number != 0:
        k_number += str(number)

    return str(k_number[::-1])


def solution(n, k):

    num_list = dec_to_k(n, k).split("0")

    for i in num_list:
        if i == '':
            num_list.remove('')

    answer = 0

    n = 1000000
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    if len(num_list) == 1:
        if int(num_list[0]) in primes:
            return 1


    for i in num_list:
        if int(i) in primes:
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
