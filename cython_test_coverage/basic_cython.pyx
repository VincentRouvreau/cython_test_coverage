# cython: linetrace=True
# distutils: define_macros=CYTHON_TRACE=1

cimport cython

cpdef int add_test_cython(int a , int b):
    return a+b
