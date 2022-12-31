import numpy as np

r=int(input("Enter no of rows: "))
a=[]
for i in range(r):
  a.append(list(map(int,input().split())))
c=len(a[0])
a=np.array(a,np.int32)
a=a.astype(float)
done=False
while not done:
  if np.min(a[r-1]) >=0:
    done=True
    break
  minCol=np.where(a == np.min(a[r-1]))[1]
  pivotVal=99999
  for i in range(r-1):
    if a[i][c-1]/a[i][minCol] < pivotVal:
      pivotVal = a[i][c-1]/a[i][minCol]
      pivotRow = i
  
  a[pivotRow]=a[pivotRow] / a[pivotRow][minCol]
  l=list(range(r))
  l.remove(pivotRow)
  for i in l:
    a[i]=a[i] - (a[i][minCol] * a[pivotRow])

print(a)
if r==3:
  x,y=0,0
  if a[0][0]==1:
    x=a[0][-1]
  elif a[0][1]==1:
    y=a[0][-1]
  
  if a[1][0]==1:
    x=a[1][-1]
  elif a[1][1]==1:
    y=a[1][-1]
  
  print("x = ",x)
  print("y = ",y)
  print("value = ",a[2][-1])
elif r==4:
  x,y,z=0,0,0
  if a[0][0]==1:
    x=a[0][-1]
  elif a[0][1]==1:
    y=a[0][-1]
  elif a[0][2]==1:
    z=a[0][-1]
  
  if a[1][0]==1:
    x=a[1][-1]
  elif a[1][1]==1:
    y=a[1][-1]
  elif a[1][2]==1:
    z=a[1][-1]

  if a[2][0]==1:
    x=a[2][-1]
  elif a[2][1]==1:
    y=a[2][-1]
  elif a[2][2]==1:
    z=a[2][-1]
  
  print("x = ",x)
  print("y = ",y)
  print("z = ",z)
  print("value = ",a[3][-1])