# Zachary J. Adam
# Evergreen Login: adazac10
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"


cc = 8.5408
bb = -5.86
aa = 1
xx = bb * bb
yy = xx - 4 * aa * cc
zz = math.sqrt(yy)
Answer = (-bb + zz) / (2 * aa)

i = (-bb +- (math.sqrt(bb * bb - 4 * aa * cc))) / (2 * aa)

print Answer
print i

###
### Problem 2
###

print "Problem 2 solution follows:"



import hw1_test 

print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f


###
### Problem 3
###

print "Problem 3 solution follows:"


Finish = ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f)) 

print Finish

###
### Collaboration
###

# ...collaborators myself and remembering that i imported math but to use 
#    it added (.pi) so hw1_test imported but (.a) ect was needed to use
