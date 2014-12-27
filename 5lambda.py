#coding:utf8
print '匿名函数'
def f(x,y):
	return x*y
print f(2,3)

g = lambda x,y:x*y
print g(2,3)
print lambda x,y:x*y
print 'redece函数' 

l=range(1,6)
print l
def r(x,y):
	return x*y

print reduce (f,l)

s = lambda x,y:x*y

reduce (f,l)