# -*- coding: UTF-8 -*-

def division(no):
    result = []
    for i in range(2, int(no ** 0.5 + 2)):
        while no % i == 0:
            no = no // i
            result.append(i)
    if no > i:     # 最后剩下的不能被分解的no,如果存在直接添加到result 如 37，2*2*29这样的数，不要将最后一项因子遗忘了！ 
        result.append(no)
    return result


def test():
    for i in range(1, 50):
        print(i, division(i))


test()