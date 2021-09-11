
def solution(board, skill):
    answer = 0

    for sk in skill:
        for i in range(sk[1], sk[3]+1):
            for j in range(sk[2], sk[4]+1):
                if sk[0] == 1:
                    board[i][j] -= sk[-1]
                else:
                    board[i][j] += sk[-1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
