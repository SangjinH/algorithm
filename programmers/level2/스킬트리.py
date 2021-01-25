def solution(skill, skill_trees):
    seq_list = [[] for _ in range(len(skill_trees))]

    for i in skill:
        for j in range(len(skill_trees)):
            if i in skill_trees[j]:
                num = skill_trees[j].index(i)
                seq_list[j].append(num)
            else:
                seq_list[j].append(27)

    print(seq_list)

    return seq_list

skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']

solution(skill, skill_trees)

# a = 'ABCDE'

# print(a.index('A'))