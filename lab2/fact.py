import matplotlib.pyplot as plt
import numpy as np
def fact(n):
  global count
  if n==1 or n==0:
    count+=1
    return 1
  else:
    count+=1
    return n*fact(n-1)

arr=np.array(range(1,100))
c_array=[]
for i in range(len(arr)):
  count=0
  fact(arr[i])
  #print("NO of steps: ",count)
  c_array.append(count)
c_array=np.array(c_array)
plt.plot(arr, c_array)
plt.show()
  