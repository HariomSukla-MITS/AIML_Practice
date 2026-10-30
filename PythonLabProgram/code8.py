class Swap:
    def swap_numbers(self, a, b):
        a = a + b
        b = a - b
        a = a - b

        print("After Swapping:")
        print("a =", a)
        print("b =", b)

class Main:
    def main(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Before Swapping:")
        print("a =", a)
        print("b =", b)

        obj = Swap()
        obj.swap_numbers(a, b)

if __name__ == "__main__":
    main_obj = Main()
    main_obj.main()