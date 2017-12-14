#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="红包分配算法"
#coding: utf-8
import random

def red_envelope(cents, people_number):
    # 考虑到红包金额不含分数以及人数不含分数
    if (not isinstance(cents, int)) or (not isinstance(people_number, int)):
        raise Exception('invalid type!')
    # 红包金额不能小于人数，否则每个人不能得到1元
    if cents < people_number:
        raise Exception('too many people!')
    # 限制小于0的情况
    if cents <= 0 or people_number <= 0:
        raise Exception('Are you kidding me ?')
    # 当红包金额等于人数时，则平均分钱
    if cents == people_number:
        return [1] * people_number
    # 当人数为1时，拥有整个金额
    if people_number == 1:
        return [cents]
    # 每个人先都获得1元
    fix_result = [1] * people_number
    # 算出剩下的金额
    cents = cents - 1*people_number
    # 另外赋值
    balance = cents

    rand_result = []
    rand_numbers = []
    for _ in range(people_number):
        rand_numbers.append(random.randint(10,100))
    rand_sum = float(sum(rand_numbers))

    for idx in range(people_number):
        if idx == people_number - 1:
            rand_result.append(balance)
        else:
            scale = rand_numbers[idx] / rand_sum
            your_cents = int(cents*scale)
            rand_result.append(your_cents)
            balance = balance - your_cents

    result = []
    for fix, rand in zip(fix_result, rand_result):
        result.append(fix+rand)

    random.shuffle(result)  # shuffle the result

    return result


# test
if __name__ == '__main__':
    result = red_envelope(100, 8)
    print (result, sum(result))