import re
s= 'abc'
s=r'abc'
print re.findall(s,"aaaaaaaaa")
print re.findall(s,'abcshsgajshabc')

st = "top tip tqp twp tep"
res = r"top"
print re.findall(res,st)

res = r"t[io]p"

print re.findall(res,st)

res = r"t[^io]p"

print re.findall(res,st)

