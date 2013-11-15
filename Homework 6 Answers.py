################################### 
    ###PROBLEM 5### 

x = 22

y = x

print y 

z =  x = 'blah'

print x

#No x is not always the same because
#it is changed multiple times but z is
#since it is only defined once

################################### 
    ###PROBLEM 6### 

w = 1 == 2

print w #yes we knew it would be false

w = 1 ==1 

print w #For 500$ what is the difference
        #between true and flase
################################### 
    ###PROBLEM 4###    
                      
def anything():
    
    stuff = float(3.1)
     
    return stuff
    
print anything()

a = anything()

print a 

d = 4

d = d == a

print d

################################### 
    ###PROBLEM 3### 
 
def anythingPART2():
    return 3.1
    
assert anything() == anythingPART2()
print "test past"

A = anything()
B = anythingPART2()

result = A == B 

print "Results!!!! :",result

# it is true.
# so ya we compared our functions
# and they return the same float,
# hurray it = true

P = 'stuff'
Q = 'more stuff'
t = 0

while t <= 2:
    t = t + 1
    
    if P == Q:
        i = P == Q
        print 'stuff and more stuff are:',i
        Q = 1
    
    elif P != Q:
        i = P ==Q
        print 'stuff and more stuff are:',i
        Q = 'stuff'
    
    else:
        pass  
'''
Our answers were fasle because our strings were different, and yes it 
would be the same false for another type such as an integer.
'''

################################### 
    ###PROBLEM 7###
    
assert P == P   ## This will be true 
print 'test passed again hurray!'   
## assert P == Q   This will be false
    
assert anything() == 3.1
print 'wow passed again A+++'
        
'''
If assert is ever false it crashes/ halts the program with an assertion 
error, if true nothing happens, the program continues.  
'''
    
    