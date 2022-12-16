import re
class Monkey:
    def __init__(self, items, op, test, oT, oF):
        self.items = [int(x) for x in items]
        self.operation = op
        self.test = int(test)
        self.oT = int(oT)
        self.oF = int(oF)
        self.timesInspect = 0

    def addValues(self, num):
        self.items.append(num)

    def performOperation(self, num):
        # operation + - * /
        if self.operation[-1] == "old":
            op = num
        else:
            op = self.operation[-1]

        if self.operation[0] == '+':
            return (num + int(op)) % mod  # // 3
        elif self.operation[0] == '-':
            return (num - int(op)) % mod  # // 3
        elif self.operation[0] == '*':
            return (num * int(op)) % mod  # // 3
        elif self.operation[0] == '/':
            return (num / int(op)) % mod  # // 3
        return 0

    def resultTest(self, num, flag):
        self.items.remove(num)
        if flag:
            monkeys[self.oT].addValues(self.performOperation(num))
        else:
            monkeys[self.oF].addValues(self.performOperation(num))

    def performTest(self, num):
        if self.performOperation(num) % self.test == 0:
            self.resultTest(num, True)
        else:
            self.resultTest(num, False)
        return 0

    def play(self):
        for num in (self.items.copy()):
            # self.performOperation(num)
            self.performTest(num)
            self.timesInspect += 1


if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()

    num_Monkeys = 8

    monkeys = [Monkey(items=re.findall(r'\d+', data[1 + (7 * i)]), op=data[2 + (7 * i)].split()[-2:],
                      test=data[3 + (7 * i)].split()[-1], oT=data[4 + (7 * i)].split()[-1],
                      oF=data[5 + (7 * i)].split()[-1]) for i in range(num_Monkeys)]
    mod = 1
    for monkey in monkeys:
        mod *= monkey.test

    for _ in range(10000):
        for m in monkeys:
            m.play()

    for m in monkeys:
        print(m.timesInspect)
