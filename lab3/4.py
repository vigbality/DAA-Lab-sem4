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


def fun_with_logn(x):
  arr=list(range(x))
  ele=random.randint(0, x)
  binary_search(arr, 0, x-1, ele)

def rec4(x):
  global count
  if x==0:
    pass
  else:
    fun_with_logn(x)
    rec4(x-1)
    rec4(x-1)
    



arr=np.array(range(1,21))
c_array=[]
for i in range(len(arr)):
  count=0
  rec4(arr[i])
  c_array.append(count)
c_array=np.array(c_array)
plt.plot(arr, c_array)
plt.show()