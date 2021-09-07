import sys
input = sys.stdin.readline

# N개의 시험장,
# A, 각 시험장의 응시자수
# 총 감독관 B 명, 부 감독관 C 명
# 총 감독관은 1명, 부 감독관은 여러명 가능
# 필요한 감독관의 최소는 ?

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# print(N)
# print(A)
# print(B, C)

answer = 0


def find_number_of_watcher(A, B, C):
    global answer

    for i in range(len(A)):
        A[i] -= B
        answer += 1
        if A[i] <= 0:
            A[i] = 0

        else:
            if A[i] % C != 0:
                answer += (A[i] // C) + 1
            else:
                answer += A[i] // C

    return answer


print(find_number_of_watcher(A, B, C))