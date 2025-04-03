"""
E(n)=4×E(n−1)+E(n−2)
To efficiently solve this problem in Python for large inputs, we need to generate Fibonacci numbers up to
4
×
1
0
16
4×10
16
  and sum the even-valued terms. Given the constraints, a brute-force approach would be too slow, so we'll use a mathematical observation: every third Fibonacci number is even. This allows us to generate only the even Fibonacci numbers directly, significantly optimizing the solution.

Approach
Mathematical Insight: The Fibonacci sequence starts with 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Notice that every third term is even (2, 8, 34, ...). This pattern holds because:

Odd + Odd = Even

Odd + Even = Odd

Even + Odd = Odd
Thus, the sequence of parity is Odd, Odd, Even, Odd, Odd, Even, ...

Efficient Generation: Instead of generating all Fibonacci numbers, we can generate only the even ones using the recurrence relation for even Fibonacci numbers:

E
(
n
)
=
4
×
E
(
n
−
1
)
+
E
(
n
−
2
)
E(n)=4×E(n−1)+E(n−2)
where
E
(
1
)
=
2
E(1)=2 and
E
(
2
)
=
8
E(2)=8.

Summation: For each test case, generate even Fibonacci numbers up to
N
N and sum them.

Solution Code
python
Copy
import sys

def sum_even_fibonacci_up_to(N):
    if N < 2:
        return 0
    total = 0
    a, b = 2, 8  # First two even Fibonacci numbers
    while a <= N:
        total += a
        a, b = b, 4 * b + a
    return total

def main():
    input_lines = sys.stdin.read().split()
    T = int(input_lines[0])
    test_cases = list(map(int, input_lines[1:T+1]))
    for N in test_cases:
        print(sum_even_fibonacci_up_to(N))

if __name__ == "__main__":
    main()
Explanation
Reading Input Efficiently: The input is read all at once using sys.stdin.read() for efficiency, especially given the constraints
1
≤
T
≤
1
0
5
1≤T≤10
5
 .

Generating Even Fibonacci Numbers: The function sum_even_fibonacci_up_to(N) starts with the first two even Fibonacci numbers (2 and 8). It then uses the recurrence relation
E
(
n
)
=
4
×
E
(
n
−
1
)
+
E
(
n
−
2
)
E(n)=4×E(n−1)+E(n−2) to generate subsequent even Fibonacci numbers until the next number exceeds
N
N. Each valid number is added to the running total.

Output: For each test case, the function computes the sum of even Fibonacci numbers not exceeding
N
N and prints the result.

This approach efficiently handles the large input constraints by leveraging mathematical properties to minimize computation, ensuring optimal performance.
"""

def gen_even_fibo(n):
    if n < 2:
        return 0
    total = 0
    a, b = 2, 8
    while a <= n:
        print(a)
        total += a
        a,b = b, 4 * b + a
    return total

if __name__ == "__main__":
    res = gen_even_fibo(100)
    print(res)