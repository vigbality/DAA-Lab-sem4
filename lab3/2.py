import matplotlib.pyplot as plt
import numpy as np
import random

def fun_with_n(x):
  global count
  arr=list(range(x))
  ele=random.randint(0, x)
  for i in arr:
    count+=1
    if ele==i:
      break

def rec2(x):
  global count
  if x==0:
    pass
  else:
    fun_with_n(x)
    rec2(x-1)



arr=np.array(range(1,101))
c_array=[]
for i in range(len(arr)):
  count=0
  rec2(arr[i])
  c_array.append(count)
c_array=np.array(c_array)
plt.plot(arr, c_array)
plt.show()