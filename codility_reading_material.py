# time complexity
def dominant(n):
   result = 0
   for i in xrange(n):
      result += 1
   return result

# counting elements
# https://codility.com/media/train/2-CountingElements.pdf
def counting(A, m):
   n = len(A)
   count = [0] * (m + 1)
   for k in xrange(n):
      count[A[k]] += 1
   return count

print counting([1,2,3,4], 4);

# Exercise 2.2
def slow_solution(A, B, m):
   n = len(A)
   sum_a = sum(A)
   sum_b = sum(B)
   for i in xrange(n):
      for j in xrange(n):
         change = B[j] - A[i]
         sum_a += change
         sum_b -= change
         if sum_a == sum_b:
            return True
         sum_a -= change
         sum_b += change
   return False

# Exercise 2.3
def fast_solution(A, B, m):
   n = len(A)
   sum_a = sum(A)
   sum_b = sum(B)
   d = sum_b - sum_a
   if d % 2 == 1:
      return False
   d //= 2
   count = counting(A, m)
   for i in xrange(n):
      if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
         return True
   return False


# Prefix sums
# https://codility.com/media/train/3-PrefixSums.pdf

def prefix_sums(A):
   n = len(A)
   P = [0] * (n + 1)
   for k in xrange(1, n + 1):
      P[k] = P[k - 1] + A[k - 1]
   return P
