
#Question 1
l1=[1,2,3,4,5]
print(list(reversed(l1)))

#Question 2
s=input("Enter A string")
for i in range(len(s)):
    if s[i].isupper():
        print(s[i])

#Question 3
s=input("Enter Values").split(",")
l=[]
for i in s:
    l.append(int(i))
print(l)

#Question 4
x=int(input("Enter A number"))
y=x
f=0
re=0
while x!=0:
    f=x%10
    re=re*10+f
    x//=10
if y==re:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")



#Question 5
from copy import *
print("DeepCopy:- ")
lst1 = ['a','b',['ab','ba']]

lst2 = deepcopy(lst1)

lst2[2][1] = "d"
lst2[0] = "c";

print(lst2)
print(lst1)
print("Shallow Copy:- ")
lst3=lst1
lst3[0]="hello"
print(lst3)
print(lst1)

