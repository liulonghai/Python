__author__ = 'Longhai Liu'

s1=(1,3,5,7)
s2=[2,4,6,8]

print len(s1)
print(len(s2))

print min(s1)
print(max(s2))

print all(s1)
print(any(s2))

print sum(s1)
print sum(s2)

print s1.count(1)
print s1.index(1)

print s2.extend(s1),s2

print s2.append(100),s2


print s2.sort(),s2
print s2.reverse(),s2
print s2.pop()
del s2[1]
print s2


str="Hello Word."
print str.isalnum()
str1="HelloWord"
print str1.isalnum()
print str1.isalpha()
print str1.isdigit()
print str.istitle()
print str.isspace()
print str.islower()
print str.isupper()
print str.split("ll")
print str.rsplit()
print str.join(str1)
print str.strip(".")
print str.replace("ll", "oo")

print str.lower()
print str.lower().capitalize()
print str.upper()
print str.swapcase()
print str.lower().title()
print str.center(20)
print str.ljust(20)
print str.rjust(20)