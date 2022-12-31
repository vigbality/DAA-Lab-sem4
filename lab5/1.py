import matplotlib.pyplot as plt
import numpy as np
import random

arr=np.array(range(3,100))
c_array=[]
def rec(n,i):
  global count
  if i>n**0.5:
    count+=1
    return
  elif n%i==0:
    count+=1
    return
  else:
    count+=1
    rec(n,i+1)


for n in arr:
  count=0
  rec(n,2)
  c_array.append(count)
c_array = np.array(c_array)
plt.plot(arr, c_array)
plt.show()