class Gen:

    def gener(self, x):
        for number in range(x):
            if number % 7 == 0:
                yield number
        return number


n = 100
num = Gen()
gen_list = num.gener(n)
print(gen_list)