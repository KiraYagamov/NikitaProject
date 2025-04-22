def to_bin(num):
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result


def square(num):
    return num * num


def pow(num, degree):
    result = 1
    for i in range(degree):
        result *= num
    return result


def sqrt(num):
    left = 0
    right = num
    mid_before = 0
    while left < right:
        mid = (right + left) / 2
        if mid_before == mid:
            return mid
        if mid * mid > num:
            right = mid
        elif mid * mid < num:
            left = mid
        else:
            return mid
        mid_before = mid
    return -1



