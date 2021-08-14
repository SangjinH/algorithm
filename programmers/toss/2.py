import math


def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료

    if orderAmount - serviceFee - taxFreeAmount == 1:
        return 0

    # 공급대금
    orderAmount - serviceFee



    additionalFee = orderAmount - taxFreeAmount - serviceFee

    if additionalFee == 1:
        answer = 0
    else:
        answer = math.ceil(additionalFee * 0.1)
    return answer