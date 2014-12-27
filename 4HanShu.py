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
print '元组'
t=('name','milo')
def w(x,y):
	print "%s : %s" % x,y

print "%s : %s" % ('name' , 'milo')

print t
x(*t)

print '冗余参数(rong yu)'
def a(x,*arr):
	print x
	print arr

a(1,2,3,4,5,5,6,5,4,6,23,235,45,6,5)
def c(x,*arr,**dic):
	print x
	print arr
	print dic

c(1,2,3,4,5,6,y=23,z=30)
