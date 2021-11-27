from collections import defaultdict

def split_alpha_num(id):
    idx = 0
    for i in range(len(id)):
        if id[i].isalpha():
            idx = i
    return idx


def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id

    check = defaultdict(list)

    for i in registered_list:
        standard = split_alpha_num(i)
        if i[standard+1:] == '':
            num = 0
            check[i[:standard+1]].append(num)

        else:
            check[i[:standard+1]].append(int(i[standard+1:]))

    for k in check.keys():
        check[k].sort()

    st = split_alpha_num(new_id)
    alpha = new_id[:st+1]
    nums = new_id[st+1:]
    # print(new_id)
    if nums == '':
        nums = 0
    else:
        nums = int(nums)

    if not check[alpha]:
        return alpha + str(nums)
    else:
        while True:
            if nums in check[alpha]:
                nums += 1
            else:
                return alpha + str(nums)





print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))

