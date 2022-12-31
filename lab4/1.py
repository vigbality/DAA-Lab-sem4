import numpy as np
import random
import matplotlib.pyplot as plt
def mergeSort(arr):
    global c
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                c=c+1
                arr[k] = L[i]
                i += 1
            else:
                c=c+1
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

comp=[]
x=[]
for i in range(1,20):
  arr = []
  c=0
  for j in range(i):
    arr.append(random.randint(1,100))
  mergeSort(arr)
  comp.append(c)
  x.append(i)
x=np.array(x)
y=np.array(comp)
plt.plot(x,y,color="green")
plt.plot(x,x**2,color="blue")
plt.show()

