from operator import index


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1 
        return self.data[self.index]



if __name__ == "__main__":
    data = [1, 2, 3, 4]
    print(data)

    reversed_data = Reverse(data)
    for i in reversed_data:
        print(i)
