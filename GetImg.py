#coding:utf8
import re
import urllib

def getHTML(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(.*?\.jpg)" width'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s,jpg' % x)
		x+=1

html = getHTML("http://www.baidu.com/")
