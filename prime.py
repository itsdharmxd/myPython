n=20000
nonprimes = n * [False]
    count = 0
    nonprimes[0] = nonprimes[1] = True
    for i in range(2, n):
        if not nonprimes[i]:
            count += 1
            for j in range(2*i, n, i):
                nonprimes[j] = True
    stop = time()
    print("Count =", count)
