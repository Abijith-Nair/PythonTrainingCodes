class Calculator:
    def __init__(self):
        self.lim = 0
        self.num = []
        self.temp = 0

    def input_numbers(self):
        self.temp = 0
        self.num = []
        self.num.clear()
        self.lim = int(input("Enter limit of numbers: "))
        print('')
        for i in range(0, self.lim):
            x = int(input("Enter value: "))
            self.num.append(x)

    def add(self):
        n = self.num.copy()
        print("")
        tot = sum(self.num)
        print("Sum =", tot)
        self.call(n, 1)

    def sub(self):
        n = self.num.copy()
        print("")
        tot = self.num[0]
        for i in range(1, self.lim):
            tot = self.num[i] - tot
        print("Difference =", tot)
        self.call(n, 1)

    def div(self):
        n = self.num.copy()
        print("")
        tot = []
        for i in range(0, self.lim - 1):
            tot.append(self.num[i] / self.num[i + 1])
            print("Quotient for given numbers [(x, y)...] format = [", tot[i], "]")
        self.call(n, 1)

    def mult(self):
        n = self.num.copy()
        print("")
        tot = self.num[0]
        for i in range(1, self.lim):
            tot *= self.num[i]
        print("Product =", tot)
        self.call(n, 1)

    def exp(self):
        n = self.num.copy()
        print("")
        tot = []
        power = int(input("Enter power value: "))
        for i in range(self.lim):
            tot.append(self.num[i] ** power)
            print("Exponential value for given numbers and given power value = [", tot[i], "]")
        self.call(n, 1)

    def mod(self):
        n = self.num.copy()
        print("")
        tot = []
        for i in range(0, self.lim - 1):
            tot.append(self.num[i] % self.num[i + 1])
            print("Floor value for given numbers [(x, y)...] format = [", tot[i], "]")
        self.call(n, 1)

    def call(self, num, temp):
        print("")
        if temp > 0:
            ch1 = input("Enter new list of numbers? (y/n): ")
            print("")
            if ch1 == 'y':
                self.input_numbers()
        ch = input("Enter operation (+ - / * ^ %) or (x):")
        if ch == '+':
            self.add()
        elif ch == '-':
            self.sub()
        elif ch == '/':
            self.div()
        elif ch == '*':
            self.mult()
        elif ch == '^':
            self.exp()
        elif ch == '%':
            self.mod()
        elif ch == 'x':
            exit

if __name__ == "__main__":
    calc = Calculator()
    calc.input_numbers()
    calc.call(calc.num, calc.temp)
