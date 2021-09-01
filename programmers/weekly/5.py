def solution(word):
    char_list = []

    def dfs(temp):

        if len(temp) == 5:
            return

        for i in ['A', 'E', 'I', 'O', 'U']:
            char_list.append(temp+i)
            dfs(temp+i)

    dfs("")
    answer = char_list.index(word) + 1

    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
