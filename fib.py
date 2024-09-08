# o(2**n) time, o(n) space

def fib(n):

    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:

        return (fib(n-1)+fib(n-2))


def fibHash(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = fibHash(n-1, mem)+fibHash(n-2, mem)
        return mem[n]


a = fibHash(2000)
