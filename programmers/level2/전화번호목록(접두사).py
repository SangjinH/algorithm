def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        bigyo = phone_book[i]
        for j in range(len(phone_book)):
            if i == j:
                continue
            if bigyo in phone_book[j][:len(bigyo) + 1]:
                return False

    return answer