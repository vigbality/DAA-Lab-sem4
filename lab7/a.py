import numpy as np
w=np.array([2,1,3])
p=np.array([6,5,3])
m=4
n=3
p_w=p/w
d={}
pwd={}
for i in range(len(w)):
  d[w[i]]=p[i]
  pwd[w[i]]=p_w[i]
print(d,'\n',pwd)
profit=0
a=[pwd.values()]
a.sort()
l=list()
while sum(l)<m:
  print(l)
  for i in pwd.keys():
    if pwd[i]==a[-1] and (i not in l):
      max_key=i
      print('hiii')
  profit+=d[max_key]
  a=a[:-1]
  l.append(max_key)
print(profit)
print(l)