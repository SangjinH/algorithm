from collections import defaultdict

def solution(phone_numbers, phone_owners, number):

    check = defaultdict(list)

    for i in range(len(phone_numbers)):
        check[phone_numbers[i]].append(phone_owners[i])

    print(check)
    return