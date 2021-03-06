#!/usr/bin/python
#coding=utf-8
#C:\NPTI_CLI\Case\team\data2\FangS\v7.5>C:/Python27/python.exe d:/fluent/FTPbanner.py d:/fluent/banner.txt

import socket
import sys
import os
 
def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return
 
def checkVulns(banner,filename):
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print ('[+] Server is vulnerable: ' + banner.strip('\n'))
 
def main():
 
	if len(sys.argv) == 2:
 
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + ' does not exit.'
			exit(0)
 
		if not os.access(filename,os.R_OK):
			print '[-] ' + filename + ' access denied.'
			exit(0)
 
		print '[+] Reading From: ' + filename
	else:
		print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
		exit(0)
 
	portList = [21,22,25,80,110,443]
	ip = '10.10.10.128'
	for port in portList:
		banner = retBanner(ip,port)
		if banner:
			print '[+] ' + ip + ':' + str(port) + '--' + banner
			if port == 21:
				checkVulns(banner,filename)
 
if __name__ == '__main__':
	main()