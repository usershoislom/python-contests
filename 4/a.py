def pascal_triangle():
    p = [1]
    yield p[0]
    while True:
        row = [1] * (len(p) + 1)
        for j in range(1, len(row)-1):
            row[j] = p[j-1] + p[j]
        p = row
        yield from p
