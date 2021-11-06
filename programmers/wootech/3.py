from collections import defaultdict, Counter

def solution(ings, menu, sell):

    check = defaultdict(int)
    answer = 0

    for i in ings:
        gradient, price = i.split()
        check[gradient] = int(price)

    profits = defaultdict(int)
    for m in menu:
        name, gradients, price = m.split()
        gradients = Counter(gradients).most_common()

        total = 0
        for g, cnt in gradients:
            total += check[g] * cnt

        profits[name] = int(price) - total

    for s in sell:
        name, cnt = s.split()
        answer += profits[name] * int(cnt)

    return answer



print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],
               ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))


print(solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"]))
