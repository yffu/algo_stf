def karatsuba_mult(x, y):

    len_x = len(x)
    len_y = len(y)

    if len_x == 1 or len_y == 1:
        return int(x) * int(y)
    else:
        half_x = len_x//2
        half_y = len_y//2
        a = x[:half_x]
        b = x[half_x:]
        c = y[:half_y]
        d = y[half_y:]
        print(' a: ' + a + ' b: ' + b + ' c: ' + c + ' d: ' + d)
        s1 = karatsuba_mult(a, c)
        s2 = karatsuba_mult(b, d)
        s3 = (int(a) + int(b)) * (int(c) + int(d))
        print(' s1: ' + str(s1) + ' s2: ' + str(s2) + ' s3: ' + str(s3))
        result = pow(10, half_x+half_y)*s1 + pow(10, half_x)*(s3-s1-s2) + s2
        print(' result: ' + str(result))
        return result


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [x for x in input().split()]
    print(karatsuba_mult(input_numbers[0], input_numbers[1]))
