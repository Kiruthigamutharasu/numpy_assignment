# ==========================================
# Assignment 9: NumPy Mathematical & Statistical Operations
# ==========================================

import numpy as np

# ------------------------------------------
# Task 1: Creating NumPy Arrays
# ------------------------------------------

print("TASK 1: Creating NumPy Arrays\n")

# 1D array from 1 to 10
arr1 = np.arange(1, 11)

# 2D array of shape (3, 3) with values 1 to 9
arr2 = np.arange(1, 10).reshape(3, 3)

# NumPy array from list
arr3 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Shape:", arr1.shape)
print("Data type:", arr1.dtype, "\n")

print("Array 2:\n", arr2)
print("Shape:", arr2.shape)
print("Data type:", arr2.dtype, "\n")

print("Array 3:", arr3)
print("Shape:", arr3.shape)
print("Data type:", arr3.dtype)

# ------------------------------------------
# Task 2: Important Mathematical Operations
# ------------------------------------------

print("\nTASK 2: Mathematical Operations\n")

A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)
print("Power:", A ** 2)

# Using NumPy functions (optional)
print("np.add:", np.add(A, B))
print("np.subtract:", np.subtract(A, B))

# ------------------------------------------
# Task 3: Important NumPy Mathematical Formulas
# ------------------------------------------

print("\nTASK 3: NumPy Mathematical Functions\n")

values = np.array([2, 4, 6, 8, 10])

print("Square root:", np.sqrt(values))
print("Exponential:", np.exp(values))
print("Natural log:", np.log(values))
print("Sum:", np.sum(values))
print("Cumulative sum:", np.cumsum(values))

# ------------------------------------------
# Task 4: Aggregation Operations
# ------------------------------------------

print("\nTASK 4: Aggregation Operations\n")

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row-wise sum:", np.sum(data, axis=1))
print("Column-wise sum:", np.sum(data, axis=0))
print("Minimum value:", np.min(data))
print("Maximum value:", np.max(data))
print("Overall mean:", np.mean(data))

# ------------------------------------------
# Task 5: Statistical Operations
# ------------------------------------------

print("\nTASK 5: Statistical Operations\n")

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

mean_marks = np.mean(marks)

print("Mean:", mean_marks)
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Range:", np.max(marks) - np.min(marks))

# ------------------------------------------
# Task 6: Percentiles & Sorting
# ------------------------------------------

print("\nTASK 6: Percentiles & Sorting\n")

sorted_marks = np.sort(marks)
print("Sorted marks:", sorted_marks)

print("25th percentile:", np.percentile(marks, 25))
print("50th percentile:", np.percentile(marks, 50))
print("75th percentile:", np.percentile(marks, 75))

above_average = np.sum(marks > mean_marks)
print("Students scoring above average:", above_average)

# ------------------------------------------
# Task 7: Mini Use Case - Sales Analysis
# ------------------------------------------

print("\nTASK 7: Sales Analysis\n")

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

total_sales = np.sum(sales)
average_sales = np.mean(sales)

print("Total weekly sales:", total_sales)
print("Average daily sales:", average_sales)
print("Highest sales:", np.max(sales))
print("Lowest sales:", np.min(sales))
print("Standard deviation:", np.std(sales))

# Days where sales were above average
above_avg_days = sales[sales > average_sales]
print("Days with above average sales:", above_avg_days)
