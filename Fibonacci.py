def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
num = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(num)
print(f"The first {num} Fibonacci numbers are: {fib_sequence}")
