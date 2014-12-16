#coding:utf8
def fun(x,y):
	if x==y:
		print x,'=',y
	else:
		print x,'!=',y

def mashine(x=3,y='奶油'):
	print "生成一个" ,x, '元',y,'口味的冰激凌!'


# s1 = raw_input("input something:")
# s2 = raw_input("input something:")

# fun(s2,s1)
mashine(5,'巧克力')
mashine()
# mashine(s1,s2)