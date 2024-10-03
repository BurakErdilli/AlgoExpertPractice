import matplotlib.pyplot as plt


def fibHash(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n], mem
    else:
        mem[n], _ = fibHash(n-1, mem)
        mem[n] += fibHash(n-2, mem)[0]
        return mem[n], mem


# Call the function and store both the Fibonacci value and the memoization map
fib_value, memo_map = fibHash(1000)

# Convert memo_map into a list of values for plotting
fib_indices = list(memo_map.keys())
fib_values = list(memo_map.values())

# Calculate the slope (difference between consecutive Fibonacci values)
fib_slopes = [fib_values[i+1] - fib_values[i]
              for i in range(len(fib_values)-1)]

# Create a plot for Fibonacci values
plt.figure(figsize=(12, 6))

# Plot 1: Fibonacci values
# Create a 2-row, 1-column subplot, and this is the first plot
plt.subplot(2, 1, 1)
plt.plot(fib_indices, fib_values, marker='o',
         linestyle='-', color='b', markersize=3)
plt.title("Fibonacci Sequence with Memoization (n=200)", fontsize=16)
plt.xlabel("n (Index)", fontsize=12)
plt.ylabel("Fibonacci Value", fontsize=12)
plt.grid(True)

# Plot 2: Slope of Fibonacci values
plt.subplot(2, 1, 2)  # This is the second plot
plt.plot(fib_indices[:-1], fib_slopes, marker='o',
         linestyle='-', color='r', markersize=3)
plt.title("Slope of Fibonacci Values (Rate of Change)", fontsize=16)
plt.xlabel("n (Index)", fontsize=12)
plt.ylabel("Slope (Δ Fibonacci Value)", fontsize=12)
plt.grid(True)
print(fib_value)
# Adjust layout and show the plot
plt.tight_layout()
plt.show()
