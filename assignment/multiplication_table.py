

def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} x {j} = {i*j}\t", end="")
        print()

def main():
    n = int(input("Enter the size of the multiplication table: "))
    print_multiplication_table(n)

if __name__ == "__main__":
    main()

