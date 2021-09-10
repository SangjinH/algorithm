"""


"""

from collections import deque


def solution(n, k, cmd):

    doubleLinkedList = {i:[i-1, i+1] for i in range(1, n+1)}
    check = ["O" for _ in range(n)]
    k += 1

    ctrl_z = []
    for i in cmd:
        key = i[0]

        if key == 'U':
            for _ in range(int(i[-1])):
                k = doubleLinkedList[k][0]

        elif key == "D":
            for _ in range(int(i[-1])):
                k = doubleLinkedList[k][1]

        elif key == "C":
            prev, next = doubleLinkedList[k]
            ctrl_z.append([prev, next, k])
            check[k-1] = "X"

            if next == n+1:
                k = doubleLinkedList[k][0]
            else:
                k = doubleLinkedList[k][1]

            if prev == 0:
                doubleLinkedList[next][0] = prev
            elif next == n+1:
                doubleLinkedList[prev][1] = next
            else:
                doubleLinkedList[prev][1] = next
                doubleLinkedList[next][0] = prev

        elif key == "Z":
            prev, next, value = ctrl_z.pop()
            check[value-1] = "O"

            if prev == 0:
                doubleLinkedList[next][0] = value
            elif next == n+1:
                doubleLinkedList[prev][1] = value
            else:
                doubleLinkedList[prev][1] = value
                doubleLinkedList[next][0] = value

    return "".join(check)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
