import matplotlib.pyplot as plt
import numpy as np
import random

def binary_search(arr, low, high, x):
    global count
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            count+=1
            return mid
        elif arr[mid] > x:
            count+=1
            return binary_search(arr, low, mid - 1, x)
        else:
            count+=1
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1



def rec(n):
  global c_array, count
  count=0
  if n==0:
    pass
  else:
    x=random.randint(1, n)
    binary_search(list(range(1,n+1)), 0, n-1, x)
    c_array.append(count)
    rec(n-1)



arr=np.array(range(1,101))
c_array=[]
rec(100)
c_array.reverse()
c_array=np.array(c_array)
plt.plot(arr, c_array)
b=np.log(arr)
b=100*b
#plt.plot(arr, b)
plt.show()