def summa(num):
    result = 0
    for i in range(1, num+1):
        result += i
    return result


def rec_summa(num):
    if num == 1:
        return 1
    return num + rec_summa(num-1)


print(rec_summa(10))
