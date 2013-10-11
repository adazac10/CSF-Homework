# Zach Adam
# Evergreen Login: adazac10@evergreen.edu
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2




###
### Problem 1
###
print "Problem 1 solution follows:"


import hw2_test 

loop = hw2_test.n 

while loop > 0:
    print loop    
    loop = loop - 1

###
### Problem 2
###
print "Problem 2 solution follows:"



base = 1.0
count = 1.0

for num in range(0,10):
    base = base / count     
    print base 
    count = count + 1.0
    base = 1.0



###
### Problem 3
###
print "Problem 3 solution follows:"



n = 1
triangular = 0
for i in range(0,10):
    triangular = triangular + i
    print "Triangular number", n, "via loop:",triangular 
    print "Triangular number", n, "via formula:", n*(n+1)/2
    n = n + 1


###
### Problem 4
###
print "Problem 4 solution follows:"



z = 1
ten = 1
for i in range(1,11):
    ten = ten * i
    print "Factorial number", z, "via loop:",ten 
    z = z + 1
    

###
### Problem 5
###
print "Problem 5 solution follows:"



from math import factorial
count = 10
number = 0
print factorial(10)

for e in range(1,11):
    number = factorial(count) 
    print "Factorial reverse number", count, "via loop:",number 
    count = count - 1



###
### Problem 6
###
print "Problem 6 solution follows:"

perm = 1.0 
last = 1.0
first = 1.0

print "Factorial decimal 0 via loop:", first

for g in range(1,11):
    first = first + perm / last
    print "Factorial decimal", g, "via loop:",first 
    last = last + 1.0


###
### Collaboration
###

# Google, Wiki


###
### Reflection; Used import math to make things easy.
###             
            

#  About 2.5 hours, no books only online help but very little
#  mostly just trial and error 