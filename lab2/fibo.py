import matplotlib.pyplot as plt
import numpy as np

def fib(n):
  global count
  if n==1 or n==2:
    count+=1
    return 1
  else:
    count+=1
    return fib(n-1)+fib(n-2)


arr=np.array(range(1,50))
c_array=[]
for i in range(len(arr)):
  count=0
  fib(arr[i])
  #print("NO of steps: ",count)
  c_array.append(count)
c_array=np.array(c_array)
plt.plot(arr, c_array)
plt.show()