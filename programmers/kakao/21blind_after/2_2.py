

def dec_to_k(number, k):
    if number < k:
        return str(number)

    temp = ""
    while number >= k:
        temp += str(number % k)
        number //= k

    if number != 0:
        temp += str(number)

    return temp[::-1]

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]


def solution(n, k):
    answer = -1

    if k != 10:
        num_list = dec_to_k(n, k).split("0")
    else:
        num_list = str(n).split("0")
    primes = prime_list(1000001)
    # print(primes)

    if len(num_list) == 1:
        if int(num_list[0]) in primes:
            return 1

    if num_list:
        answer = 0
        for i in num_list:
            if i.isdigit():
                if int(i) in primes:
                    answer += 1
    return answer







print(solution(437674, 3))
print(solution(110011, 10))
print(solution(1000000, 2))
