import sys

def scc(input_n):
    # mergesort first, then tack on the inversion counts
    n = len(input_n)
    if n == 1:
        return input_n, 0
    else:
        x, x_inv = inv_fast(input_n[:n//2])
        #print('x: ' + str(x))
        y, y_inv = inv_fast(input_n[n//2:])
        #print('y: ' + str(y))
        merge_n = []
        split_inv = 0
        while x and y:
            if x[0] <= y[0]:
                merge_n.append(x.pop(0))
            else:
                merge_n.append(y.pop(0))
                split_inv += len(x)
                # if a y is placed while x is not empty it counts as an inversion
        while x:
            merge_n.append(x.pop(0))
        while y:
            merge_n.append(y.pop(0))

        return merge_n, x_inv + y_inv + split_inv

if __name__ == '__main__':
    input_n = [int(n) for n in sys.stdin]
    # print(input_n)
    print(inv_fast(input_n))
    # 2407905288 inversions
    #print(inv_fast([1, 9, 6, 4, 5]))
    # 5 inversions
    #print(inv_fast([9, 8, 7, 6, 5, 4]))
    # 15 inversions
