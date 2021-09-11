"""

"""

def recur(arr, primes_nums):
    if len(arr) == 1:
        return arr

    for i in range(len(primes_nums)):
        if len(arr) % primes_nums[i] == 0:
            new_arr = [[] for _ in range(primes_nums[i])]

            for j in range(len(arr)):
                new_arr[j%primes_nums[i]].append(arr[j])
            break

    result = []
    for i in range(len(new_arr)):
        result += recur(new_arr[i], primes_nums)

    return result


def solution(n):
    primes = [True] * 1000001

    for i in range(2, int((1000001)**(1/2))+1):
        if primes[i]:
            for j in range(2*i, len(primes), i):
                primes[j] = False

    prime_nums = []
    for i in range(2, len(primes)-1):
        if primes[i]:
            prime_nums.append(i)

    arr = [i for i in range(1, n+1)]

    return recur(arr, prime_nums)


print(solution(12))
print(solution(18))