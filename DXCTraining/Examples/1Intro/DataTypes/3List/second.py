l=['a','b','c','d','e','f']
print(len(l))
# print(sum(l) )
print(max(l) )
print(min(l) )
l.append('g')
print(l)
l2=['h','i','j','k']
l.extend(l2)
print(l)
l.insert(2,'z')
print(l)
print(l.pop(2))
print(l)
print(l.pop())
print(l)
l.remove('a')
print(l)
l.reverse()
print(l)
l.sort(reverse=True)
print(l)  
print(l.count('a'))
print('a' in l)









#stack operations->
stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
stack.pop()
stack.pop()
stack.pop()

#queue operations:
queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
queue.pop(0)
queue.pop(0)
queue.pop(0)

#dequeue