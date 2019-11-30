class Gen:
    def gener(self, x):
        return [number for number in range(x) if number % 7 == 0]

n = 100
num = Gen()
gen_list = num.gener(n)
print(gen_list)