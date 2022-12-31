import numpy as np
import matplotlib.pyplot as plt
import random
def newton_method(number):    
  a = number     
  for i in range(100):         
    number = 0.5 * (number + a / number)     
    return number
def sqrt(n):  
  global c  
  c=c+1  
  if(n>2):    
    sqrt(newton_method(n))
steps=[]
x=[]
for i in range(1,5):  
  c=0  
  x.append(2**i)  
  sqrt(2**i)  
  steps.append(c)
  y=np.array(steps)
  x=np.array(x)
  plt.plot(x,y)
  plt.show()