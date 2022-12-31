import matplotlib.pyplot as plt
import numpy as np
def sum(n):
  global count
  sum=0
  for i in range(2,n+1,2):
    sum+=i
    count+=1
  return sum

arr=np.array(range(1,100))
c_array=[]
for i in range(len(arr)):
  count=0
  print(sum(arr[i]))
  #print("NO of steps: ",count)
  c_array.append(count)
c_array=np.array(c_array)
plt.plot(arr, c_array)
plt.show()
  