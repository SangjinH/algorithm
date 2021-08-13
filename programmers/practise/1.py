import math

def solution(b):
    for i in range(1, b):
        if math.sqrt(i**2 + b**2) == int(math.sqrt(i**2 + b**2)):
            return int(math.sqrt(i**2 + b**2))

    return -1



b = 4
print(solution(b))


b = 12
print(solution(b))



b = 5
print(solution(b))