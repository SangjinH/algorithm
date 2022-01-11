import sys
input = sys.stdin.readline

alphas = list(input().rstrip())
print(alphas)


"""
모든 경우의 수를 다 따져 봐야함 
각 원소를 원래 원소의 인덱스를 통해 배열하면서
결국 원하는 문자를 확인
이전 문자와 같다면 return 
종료조건 idx 가 마지막 원소의 길이만큼이라면 return
"""

# def backtrack(idx, now_string, letters, visited):
#     global answer, answer_dict
#
#     if idx == len(visited) and not answer_dict[now_string]:
#         answer += 1
#         answer_dict[now_string] = 1
#         return
#
#     for i in range(len(letters)):
#         if not visited[i]:
#             if not now_string:
#                 now_string += letters[i]
#                 visited[i] = True
#                 backtrack(idx+1, now_string, letters, visited)
#                 now_string = now_string[:-1]
#                 visited[i] = False
#             else:
#                 if letters[i] != now_string[-1]:
#                     now_string += letters[i]
#                     visited[i] = True
#                     backtrack(idx + 1, now_string, letters, visited)
#                     now_string = now_string[:-1]
#                     visited[i] = False
#
# visited = [False] * len(alphas)
#
# backtrack(0, "", alphas, visited)
#
# print(answer)


