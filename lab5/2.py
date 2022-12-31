import matplotlib.pyplot as plt
import numpy as np
import random

arr=np.array(range(3,100))
c_array=[]
def rec(n,x,t):
  global count
  count+=1
  root = 0.5 * (x + (n / x))
  if abs(root-x)<t:
    count+=1
    return
  rec(n,root,root)

for n in arr:
  count=0
  rec(n,2)
  c_array.append(count)
c_array = np.array(c_array)
plt.plot(arr, c_array)
plt.show()