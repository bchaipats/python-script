def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


if __name__ == "__main__":
    
    data = [1, 2, 3, 4, 5]
    print(data)
    
    for i in reverse(data):
        print(i)

    # generator expression
    print()
    total = sum(i*i for i in range(3))
    print(total)