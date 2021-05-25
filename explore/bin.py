#Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
   # initial conditions
   if n == 0 or W == 0 :
      return 0
   # If weight is higher than capacity then it is not included
   if (wt[n-1] > W):
      return knapSack(W, wt, val, n-1)
   # return either nth item being included or not
   else:
      return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
         knapSack(W, wt, val, n-1))
# To test above function
val = [60,70,80,90,100]
wt = [1,2,3,4,5]
W = 32
n = len(val)
print (knapSack(W, wt, val, n))