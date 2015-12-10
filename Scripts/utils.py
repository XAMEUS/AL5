from copy import copy
def dcopy(d):
    dd = {}
    for e in d:
        dd[e] = (copy(d[e]))
    return dd