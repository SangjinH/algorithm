n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

def solution(n, k, cmd):

    arr = [i for i in range(n)]
    z_stack = []

    # 처음 시작 위치
    idx = k

    for c in cmd:
        c = list(c.split())
        # C or Z
        if len(c) == 1:
            if c[0] == 'C':
                z_stack.append((idx, arr[idx]))
                del arr[idx]
                # 마지막 원소를 가리키고 있다면
                if idx >= len(arr):
                    idx -= 1
            else:
                ins_idx, value = z_stack.pop()
                arr.insert(ins_idx, value)
                if ins_idx <= idx:
                    idx += 1
        # U, D X
        else:
            if c[0] == 'U':
                idx -= int(c[1])
            else:
                idx += int(c[1])
    result = ''
    for i in range(n):
        if i in arr:
            result += 'O'
        else:
            result += 'X'
    return result

print(solution(n, k, cmd))