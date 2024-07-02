def fibo(N):
    a, b = 0, 1
    for _ in range(N + 1):
        yield a
        a, b = b, a + b
def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
