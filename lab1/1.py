import matplotlib.pyplot as plt
import numpy as np
import random


def ins(arr):
  global count
  for i in range(1,len(arr)):
    ind=i-1
    cur=arr[i]
    count+=1
    while ind>=0 and arr[ind]>cur:
      count+=1
      arr[ind+1]=arr[ind] 
      ind-=1
    arr[ind+1]=cur
# print(arr)


c_array=[]
for i in range(2,101):
  arr=[random.randint(1,100) for _ in range(i)]
  count=0
  ins(arr)
  c_array.append(count)


c_array=np.array(c_array)
n_array=np.array(range(2,101))
plt.plot(n_array, c_array)
plt.show()
