
cpdef int loop_cython(int n):
    cdef int j = 0
    for i in range(n):
        j += 1
    return j