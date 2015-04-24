#coding=utf-8
import urllib
import urllib2
import thread
import time
import re

ip = []
out = []
last=[]
title=[]

def ipout():
	for i in range(1,255):
		ip.append('http://'+ipinput+'.'+str(i)+'/')
	

def scan(ipin):
	try:
		try:
			#content = urllib2.urlopen(ipin,timeout=3).read()
			headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
			req = urllib2.Request(ipin,headers=headers)
			socket = urllib2.urlopen(req)
			content = socket.read()
			socket.close()

			tmp1 = re.findall('<title>(.*)</title>|<TITLE>(.*)</TITLE>',content)
			if len(tmp1) != 0:
				title.append(tmp1[0])
			

			if content == None:
				print '%s is down!'%(ipin)
			else:
				print '%s is up!'%(ipin)
				out.append(ipin)
		except:
			pass
	except urllib2.URLError:
		print '%s is down!'%(ipin)
	return out,title

def thscan():
	for i in range(254):
		#scan(ip[i]) 单线程
		thread.start_new_thread(scan,(ip[i],)) #多线程
		time.sleep(0.05)

def outfile():
	thscan()
	lenout = len(out)
	if lenout != 0:
		file = open(ipinput+'.html','w')
		file.close()
		file = open(ipinput+'.html','a+')
		try:

			for i in range(lenout):
				file.write('<a href="'+out[i]+'" target="_blank">'+out[i]+'</a>')
				file.write(title[i])
				file.write('</br>')
			file.close
		except:
			pass
	else:
		print 'None one is up!'

if __name__ == '__main__':
	print 'Example: 118.180.5'
	ipinput = raw_input('Enter start ip:')
	ipout()
	outfile()
