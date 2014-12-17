# coding:utf8

# def f(x):
# 	print x

# f(10)
# f('hello')
# f('你好')
# f([1,2,3,4])
# f(range(8))
# l=range(10)
# f(l)
# f(('a','b'))

def x(x,y):
	print x,y
x(('a','b'),('c','v'))

t=('name','milo')
def w(x,y):
	print "%s : %s" % x,y

print "%s : %s" % ('name' , 'milo')

print t
x(*t)