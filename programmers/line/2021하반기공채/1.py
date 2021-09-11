
def solution(student, k):

    answer = 0

    jae = []
    for i in range(len(student)):
        if student[i]:
            jae.append(i)

    check = []
    for i in range(len(jae)-k+1):
        check.append(jae[i:i+k])

    for i in check:
        left = i[0]
        right = i[-1]

        left_0 = 0
        right_0 = 0
        for j in range(left-1, -1, -1):
            if student[j] == 1:
                break
            else:
                left_0 += 1

        for j in range(right+1, len(student)):
            if student[j] == 1:
                break
            else:
                right_0 += 1

        answer += (left_0+1) * (right_0+1)


    return answer



print(solution([0,1,0,0], 1))
print(solution([0, 1, 0, 0, 1, 1, 0], 2))
print(solution([0, 1, 0], 2))