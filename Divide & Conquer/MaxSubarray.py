def merge(a, l, mid, r):
  ### Max subarray de [L+x, mid]
  sumL = a[mid]
  bestL = a[mid]
  for i in range(mid-1, l-1, -1):
    sumL += a[i]
    bestL = max(sumL, bestL)
  
  ##Max subarray de [mid+1, R-y]
  sumR = a[mid+1]
  bestR = a[mid+1]
  for i in range(mid+2, r+1):
    sumR += a[i]
    bestR = max(sumR, bestR)
  return bestL + bestR

def solve(a, l, r):
  if l == r:
    return a[l]
  mid = (l+r)//2
  left_ans = solve(a,l,mid)
  right_ans = solve(a,mid+1,r)
    ### Combinar las respuestas
  mid_ans = merge(a, l ,mid, r)
  return max(left_ans, right_ans, mid_ans)

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(solve(arr,0,len(arr)-1)) 