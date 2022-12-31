import numpy as np
import matplotlib.pyplot as plt
import random
def part(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      global count
      count+=1
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quick_sort(array, low, high):
  if low < high:
    pi = part(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)
#main
   
n=20
comp=[]
for i in range(1,n+1):
  a=[]
  count=0
  for j in range(1,i+1):
    a.append(random.randint(1,50))
    quick_sort(a,0, len(a) - 1)
  comp.append(count)
x=np.arange(1,n+1)
comp=np.array(comp)
Y=np.log(x)*x
plt.plot(x,comp,color='green',label='comparisons')
plt.plot(x,Y,'blue',label='Nlog(N)')
plt.legend()
plt.show()