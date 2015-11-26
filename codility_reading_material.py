# time complexity
def dominant(n):
   result = 0
   for i in xrange(n):
      result += 1
   return result

# counting elements
def counting(A, m):
   n = len(A)
   count = [0] * (m + 1)
   for k in xrange(n):
      count[A[k]] += 1
   return count

print counting([1,2,3,4], 4);
