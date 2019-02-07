n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
c=int(n[2])
if (a>c) and (a>b):
  largest=a
  if (b>a) and (b>c):
    largest=b
else:
  largest=c
print(largest)
