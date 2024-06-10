class EvenNumbers:

    start = 0
    end = 1

    def __init__(self, start, end):
        self.i = 0
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start - 2
        return self

    def __next__(self):
        if self.i % 2:
            self.i +=1
            return
        else:
            self.i += 2
            if self.i > self.end:
                raise StopIteration()
            return self.i


print("После перебора и вывода:")
en = EvenNumbers(10, 25)

for i in en:
    print(i)
