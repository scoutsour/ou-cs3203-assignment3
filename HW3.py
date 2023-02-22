
def main():
    print("Enter five integers")
    arr = []
    for i in range(5):
        num = int(input("Enter an integer: "))
        arr.append(num)

    print("The contents of the array are:")
    for numb in range(5):
        print(numb + 1)

    print("the sum is")
    print(sum(arr))

    print("the product of all nums is")
    print(product(arr))


def sum (array):
    total = 0
    for i in array:
        total+= i
    return total
def product (array2):
    total = 1
    for i in array2:
        total *= i
    return total

main()