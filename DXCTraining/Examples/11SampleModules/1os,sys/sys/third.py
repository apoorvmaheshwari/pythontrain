import sys
module = __import__('os')
print(module.__file__)
print(sys.modules.keys())
print(sys.platform)

sys.exit(1)

sys.stdout= open('data.out','w')

sys.stdin = open('data.in','r')
print('asfdddddddddsdfsdf')