print("************** 1 ***************")
x = input(str("entrez une caractere: "))
if (len(x ) < 10):
    print("string not long enough")
else:
    print("string too long\n")

print("************** 2 ***************")
list = x
print("The first character is: ",x[0], "\n")
print("The last character is: ",x[-1], "\n")
print("************** 3 ***************")
a = ""
for i in list:
    a += i
    print(a)
print("************** 4 Bonus ***************")
from random import shuffle
# t = x
b = []
for j in x:
    b.append(j)
shuffle(b)
c = ""
for z in b:
    c = c + z
print(c)
