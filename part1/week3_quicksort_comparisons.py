import sys

def quick_comp(A, l, r):
    # mergesort first, then tack on the inversion counts
    #print(A)
    #print('l: ' + str(l) + ' r: ' + str(r) + ' p: ' + str(A[l]))
    if r - l <= 0:
        # print('done')
        return 0
    cnt = (r-l) + ChoosePivot3(A, l, r)
    return cnt


def ChoosePivot1(A, l, r):
    # partition A around p, the first element of the segment
    p = A[l]
    i = l + 1
    for j in range(i, r+1):
        if A[j] < p:
            # place smaller item in first half
            A[j], A[i] = A[i], A[j]
            i += 1
    # place pivot in between, switch with leftmost smaller item
    A[l], A[i-1] = A[i-1], A[l]
    # recursively sort 1st part
    cnt_l = quick_comp(A, l, i-2)
    # recursively sort 2nd part
    cnt_r = quick_comp(A, i, r)
    # return both l and r side
    return cnt_l + cnt_r

def ChoosePivot2(A, l, r):
    # partition A around p, the last element of the segment
    A[r], A[l] = A[l], A[r]
    p = A[l]
    i = l + 1
    for j in range(i, r+1):
        if A[j] < p:
            # place smaller item in first half
            A[j], A[i] = A[i], A[j]
            i += 1
    # place pivot in between, switch with leftmost smaller item
    A[l], A[i-1] = A[i-1], A[l]
    # recursively sort 1st part
    cnt_l = quick_comp(A, l, i-2)
    # recursively sort 2nd part
    cnt_r = quick_comp(A, i, r)
    # return both l and r side
    return cnt_l + cnt_r

def ChoosePivot3(A, l, r):
    # partition A around p, the median of the left right and mid elements
    lst = []
    lst.append((A[l], l))
    lst.append((A[r], r))
    lst.append((A[(l+r)//2], (l+r)//2))
    lst.sort(key = lambda x: x[0])
    i_median = lst[1][1]

    A[i_median], A[l] = A[l], A[i_median]
    p = A[l]
    i = l + 1
    for j in range(i, r+1):
        if A[j] < p:
            # place smaller item in first half
            A[j], A[i] = A[i], A[j]
            i += 1
    # place pivot in between, switch with leftmost smaller item
    A[l], A[i-1] = A[i-1], A[l]
    # recursively sort 1st part
    cnt_l = quick_comp(A, l, i-2)
    # recursively sort 2nd part
    cnt_r = quick_comp(A, i, r)
    # return both l and r side
    return cnt_l + cnt_r

if __name__ == '__main__':
    input_n = [int(n) for n in sys.stdin]
    # input_n = [2, 3, 8, 9, 12, 1, 4]
    # print(input_n)
    print(quick_comp(input_n, 0, len(input_n)-1))
    print(input_n)

# [1, 2, 8, 9, 12, 3, 4]
# [1, 2, 8, 3, 12, 9, 4]
# [1, 2, 8, 3, 4, 9, 12]
# [1, 2, 4, 3, 8, 9, 12]
