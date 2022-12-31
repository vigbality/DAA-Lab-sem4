import matplotlib.pyplot as plt
import numpy as np
import random

def sel(arr):
  global count
  n=len(arr)
  for i in range(n):
    small=i
    count+=1
    for j in range(i,n):
      count+=1
      if arr[j]<arr[small]:
        small=j
        count+=1
    arr[i],arr[small]=arr[small],arr[i]
    count+=1



c_array=[]
for i in range(2,101):
  arr=[random.randint(1,100) for _ in range(i)]
  count=0
  sel(arr)
  c_array.append(count)


c_array=np.array(c_array)
n_array=np.array(range(2,101))
plt.plot(n_array, c_array)
plt.show()