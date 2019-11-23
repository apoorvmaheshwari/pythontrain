from commands import *

text = getoutput('ls -l *.py')
print 'ls -l *.py:'
print text

print 

text = getoutput('ls -l *.notthere')
print 'ls -l *.py:'
print text