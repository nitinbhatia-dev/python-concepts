def yieldTest():
    for i in range(1,3):
        yield i

if __name__ == "__main__":
    t = yieldTest()
    print(next(t))
    print(next(t))
    print(next(t)) # this will throw StopIteration Exception