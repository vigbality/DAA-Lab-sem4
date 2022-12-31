import matplotlib.pyplot as plt
import numpy as np

def rec1(x):
  global count
  if x==0:
    pass
  else:
    count+=1
    rec1(x-1)



arr=np.array(range(1,101))
c_array=[]
for i in range(len(arr)):
  count=0
  rec1(arr[i])
  c_array.append(count)
c_array=np.array(c_array)
plt.plot(arr, c_array)
plt.show()