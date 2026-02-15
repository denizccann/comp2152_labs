print("=" * 60)
print("WEEK 05 LAB: RECURSION & FUNCTIONS")
print("=" * 60)

# Question 1: Fibonacci Number 
print("\n" + "=" * 50)
print("Question 1: Fibonacci Number (#509)")
print("=" * 50)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Test cases
print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    result = fib(i)
    print("F(" + str(i) + ") = " + str(result))

# Question 2: FizzBuzz 
print("\n" + "=" * 50)
print("Question 2: FizzBuzz (#412)")
print("=" * 50)

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test cases for FizzBuzz
print("\nTest Case 3: n = 15")
print("Output: " + str(fizz_buzz(15)))

# Question 3: Binary Search (LeetCode #704)
print("\n" + "=" * 50)
print("Question 3: Binary Search (#704)")
print("=" * 50)

# Part A
def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Part B
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)

def search_recursive(nums, target):
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)

nums_test = [-1, 0, 3, 5, 9, 12]
target_val = 9
print(f"Iterative Result: {binary_search_iterative(nums_test, target_val)}")
print(f"Recursive Result: {search_recursive(nums_test, target_val)}")