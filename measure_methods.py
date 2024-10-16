import numpy as np
import time
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Set precision for Decimal
getcontext().prec = 100

# Fibonacci methods


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_memoized(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


def fib_matrix_iterative(n):
    if n == 0:
        return 0
    F = np.array([[1, 1], [1, 0]])
    result = np.identity(2, dtype=int)
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, F)
        F = np.dot(F, F)
        n //= 2
    return result[0, 1]


def fib_binet(n):
    if n < 0:
        return "Error: Negative input is not allowed."
    if n < 70:  # Limiting Binet to smaller n where it's reliable
        phi = (1 + Decimal(5).sqrt()) / 2
        psi = (1 - Decimal(5).sqrt()) / 2
        return int((phi**n - psi**n) / Decimal(5).sqrt())
    else:
        return None  # Return None for large n instead of an error message

# Measurement function


def measure_methods(duration):
    methods = {
        'Recursive': fib_recursive,
        'Iterative': fib_iterative,
        'Memoized': fib_memoized,
        'Matrix': fib_matrix_iterative,
        'Binet': fib_binet
    }

    results = {}
    for name, method in methods.items():
        try:
            n = 0
            start = time.time()
            print(f"\nCalculating Fibonacci numbers using {name} method...")
            while time.time() - start < duration:
                method(n)
                n += 1
            results[name] = n
        except Exception as e:
            results[name] = f"Error: {e}"
    return results

# Custom y-axis formatter


def decimal_formatter(x, pos):
    return f"{Decimal(x):,.0f}"

# Main function


def main():
    duration = 1  # Duration in seconds for each method
    results = measure_methods(duration)

    # Print results
    for method, count in results.items():
        print(f"{method}: {count} Fibonacci numbers calculated in {duration} seconds")

    # Plotting results
    methods = list(results.keys())
    counts = [results[method] if isinstance(
        results[method], int) else 0 for method in methods]

    plt.plot(methods, counts, marker='o')
    plt.xlabel('Methods')
    plt.ylabel('Number of Fibonacci Numbers Calculated')
    plt.title('Fibonacci Calculation Methods Performance')
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(
        decimal_formatter))  # Set custom formatter
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
