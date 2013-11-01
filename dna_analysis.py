# Zach Adam
# Evergreen Login: adazac10
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

################################################
# Total nucleotides seen so far.
total_count2 = 0
# Number of A and T nucleotides seen so far.
at_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count2 = total_count2 + 1

    # next, if the bp is a T or a A,
    if bp == 'T' or bp == 'A':
        # increment the count of a T
        at_count = at_count + 1


# divide the at_count by the total_count
at_content = float(at_count) / total_count2

#####################################################
total_count3 = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0

for bp in seq:
    # increment the total number of bps we've seen
    total_count3 = total_count3 + 1

    
    if bp == 'A':
        # increment the count of a
        a_count = a_count + 1
    elif bp == 'T':
        # increment the count of t
        t_count = t_count + 1
    elif bp == 'G':
        # increment the count of g
        g_count = g_count + 1
    elif bp == 'C':
        # increment the count of c
        c_count = c_count + 1


# divide the a,t,g,c_count by the total_count
a_content = float(a_count) / total_count3
t_content = float(t_count) / total_count3
g_content = float(g_count) / total_count3
c_content = float(c_count) / total_count3

####################################################
sumcount = 0
test = 0

sumcount = a_content + t_content + g_content + c_content

## (G+C)/(A+T+G+C)
test = gc_content / sumcount 

####################################################
ATGC = 0

ATGC = at_content / gc_content

####################################################

HighGC = 0
LowGC = 0
HighGC = sumcount * .60 
LowGC = sumcount * .40

###Test to see what 60% and 40% are###
# print 'HighGC:', HighGC
# print 'LowGC:', LowGC

if gc_content > HighGC:
    print 'high GC content'
elif gc_content < LowGC:
    print 'low GC content'
else:
    print 'moderate GC content'


####################################################

# Print the answer
print 'GC-content:', gc_content

# Print the answer 2
print 'AT-content:', at_content


# Print the answer
print 'A-content:', a_content
print 'T-content:', t_content
print 'G-content:', g_content
print 'C-content:', c_content

# Print the Answer
print 'A,T,G,C-content total:', sumcount
print 'total count variable:', total_count
print 'total count2 variable:', total_count2
print 'total count3 variable:', total_count3
print 'length of sequence varialbe:', len(seq)
print 'test to see if GC is correct:', test

# Print the Answer
print 'At/GC ratio:', ATGC
