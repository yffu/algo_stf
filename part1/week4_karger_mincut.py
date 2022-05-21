import sys, re, copy
from random import randrange
debug= False
def min_cut(A):
    while len(A) > 2:
        # select an edge (u, v) uniformly at random
        u = A.pop(randrange(len(A)))
        v = A.pop(randrange(len(A)))
        contract(A, u, v)
    return A

def contract(A, u, v):
    # replace u and v by a new vertex called uv
    i_u = u.pop(0)
    i_v = v.pop(0)
    u.sort()
    v.sort()
    if debug: print('u: ' + str(u))
    if debug: print('v: ' + str(v))
    # instead of creating a new vertex number, just choose one of u or v and replace all occurrences of 1 with the other
    # pick edge at random and collapse its 2 endpoints into a single node, what goes on at the data structure representation level?
    # pick u and v, merge distinct elements into uv. all other vertices reference u instead of v, in other words they point to the merged vertices
    # what about removing self-references? edges between u and v so if u had references to any of v, remove it. let's do a simple input example
    if debug: print('i_u: ' + str(i_u) + ' i_v: ' + str(i_v))
    uv = u + v
    # uv = list(set(u+v)) you should not do the set, since it removes multiple edges
    uv.sort()
    # delete all edges (u, v)
    if debug: print('uv: ' + str(uv))
    for i_A in range(len(A)):
        # for every edge (w, u), replace it by (w, uv)
        # similarly for every edge (w, v) replace it by (w, uv)
        w = A[i_A]
        i_w = w[0]
        if debug: print('i_w: ' + str(i_w))
        if i_w in v:
            # has an edge incident to v, change v to u
            if debug: print('v incident to w')
            if debug: print('w before update: ' + str(w))
            while i_v in w[1:]:
                w[w[1:].index(i_v)+1] = i_u
            # pad out index with 1 since search was on array without first element.
        else:
            continue
        if debug: print('w: ' + str(A[i_A]))
    while i_u in uv: uv.remove(i_u)
    while i_v in uv: uv.remove(i_v)
    uv.insert(0, i_u)
    if debug: print('uv: ' + str(uv))
    A.append(uv)
    if debug: print('A: ')
    if debug: print(*A, sep='\n')


if __name__ == '__main__':
    A = [re.split(r'\t+', n.rstrip()) for n in sys.stdin]
    cnt = len(A)*(len(A)-1)/2
    itr = 0
    while True:
        B = copy.deepcopy(A)
        B = min_cut(B)
        if debug: print(B)
        if debug: print(len(B[0]))
        if len(B[0])-1 < cnt: cnt = len(B[0])-1
        itr+=1
        print ('itr: ' + str(itr))
        print ('cnt: ' + str(cnt))

