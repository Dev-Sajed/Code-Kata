a=int(input())
b=int(input())
c=int(input())
if (a>c) and (a>b):
  largest=a
  if (b>a) and (b>c):
    largest=b
else:
  largest=c
print(largest)
