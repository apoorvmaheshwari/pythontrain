import sys
old=sys.stdout
sys.stdout= open('data.out','a')
print('hiiiiiiii')
print('hiiiiiiii')
print('hiiiiiiii')
sys.stdout=old


#sys.stdin = filename