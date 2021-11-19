from math import factorial
from math import pow
from math import log

X = []

for i in range(10):
  if i % 2 == 0:
    X.append(pow(3,i) + 7*factorial(i))
  else:
    X.append(pow(2,i) + 4*log(i))

average = sum(X)/len(X)

print("A posição do maior número é", X.index(max(int(number) for number in X)), "e a média é %.2f" %average)
