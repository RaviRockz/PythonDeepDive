""""""


class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))


def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count

    return add


a = averager()
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(10))
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(20))
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(30))
print(a.__closure__)
print(a.__code__.co_freevars)


def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total, count
        total += number
        count += 1
        return total / count

    return add


a = averager()
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(10))
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(20))
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(30))
print(a.__closure__)
print(a.__code__.co_freevars)
