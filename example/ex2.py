def f(n):

    ans = ""
    while n >= 1000:
        res = n % 1000
        ans = "," + (3-len(str(res)))*'0' + str(res) + ans
        n //= 1000

    if n != 0:
        ans = str(n) + ans
    return ans


print(f(10000001234))