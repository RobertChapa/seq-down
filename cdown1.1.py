#!/bin/python3

import os
import sys
import requests

def i(pgst, pgnd, lnkst, lnknd):
	pgs = range(pgst, pgnd + 1)

	for st in pgs:
		pg = (st)
		url = lnkst + str(pg) + lnknd
		r = requests.get(url)
		with open(str(pg) + lnknd, 'wb') as outfile:
			outfile.write(r.content)

def o(pgst, pgnd, lnkst, lnknd):
	pgs = range(pgst, pgnd + 1)

	for st in pgs:
		if (int(st) > -1) and (int(st) < 10):
			pg = ('0' + str(st))
		else:
			pg = (st)
		url = lnkst + str(pg) + lnknd
		r = requests.get(url)
		with open(str(pg) + lnknd, 'wb') as outfile:
			outfile.write(r.content)

def oo(pgst, pgnd, lnkst, lnknd):
	pgs = range(pgst, pgnd + 1)

	for st in pgs:
		if (int(st) > -1) and (int(st) < 10):
			pg = ('00' + str(st))
		elif (int(st) >= 10) and (int(st) < 100):
			pg = ('0' + str(st))
		else:
			pg = (st)
		url = lnkst + str(pg) + lnknd
		r = requests.get(url)
		with open(str(pg) + lnknd, 'wb') as outfile:
			outfile.write(r.content)

def ooo(pgst, pgnd, lnkst, lnknd):
	pgs = range(pgst, pgnd + 1)

	for st in pgs:
		if (int(st) > -1) and (int(st) < 10):
			pg = ('000' + str(st))
		elif (int(st) >= 10) and (int(st) < 100):
			pg = ('00' + str(st))
		elif (int(st) >= 100) and (int(st) < 1000):
			pg = ('0' + str(st))
		else:
			pg = (st)
		url = lnkst + str(pg) + lnknd
		r = requests.get(url)
		with open(str(pg) + lnknd, 'wb') as outfile:
			outfile.write(r.content)

def s(link, name):
	url = link
	r = requests.get(url)
	with open(name, 'wb') as outfile:
		outfile.write(r.content)

def c(link):
	url = link
	r = requests.get(url)
	with open('cover.jpg', 'wb') as outfile:
		outfile.write(r.content)

def f(set, pgst, pgnd, lnkst, lnknd, nmset, nmst, nmnd, nmfnd):

	pgs = range(pgst, pgnd + 1)
	nms = range(nmst, nmnd + 1)

	if set == '1':
		for st in pgs:
			indi = pgs.index(st)
			pg = (st)
			url = lnkst + str(pg) + lnknd
			r = requests.get(url)

			url = lnkst + str(pg) + lnknd
			r = requests.get(url)

			if nmset == '0':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmset == '00':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '00'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmset == '000':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '000'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '00'
				elif (nms[indi] >= 100) and (nms[indi] < 1000):
					nmsetf = '0'
				else:
					nmsetf = ''
			else:
				nmsetf = ''

			with open(nmsetf + str(nms[indi]) + lnknd, 'wb') as outfile:
				outfile.write(r.content)

	elif set == '0':
		for st in pgs:

			indi = pgs.index(st)

			if (int(st) > -1) and (int(st) < 10):
				pg = ('0' + str(st))
			else:
				pg = (st)

			url = lnkst + str(pg) + lnknd
			r = requests.get(url)

			if nmset == '0':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmset == '00':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '00'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmset == '000':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '000'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '00'
				elif (nms[indi] >= 100) and (nms[indi] < 1000):
					nmsetf = '0'
				else:
					nmsetf = ''
			else:
				nmsetf = ''

			with open(nmsetf + str(nms[indi]) + lnknd, 'wb') as outfile:
				outfile.write(r.content)

	elif set == '00':
		for st in pgs:

			indi = pgs.index(st)

			if (int(st) > -1) and (int(st) < 10):
				pg = ('00' + str(st))
			elif (int(st) >= 10) and (int(st) < 100):
				pg = ('0' + str(st))
			else:
				pg = (st)

			url = lnkst + str(pg) + lnknd
			r = requests.get(url)

			if nmset == '0':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmset == '00':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '00'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmset == '000':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '000'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '00'
				elif (nms[indi] >= 100) and (nms[indi] < 1000):
					nmsetf = '0'
				else:
					nmsetf = ''
			else:
				nmsetf = ''

			with open(nmsetf + str(nms[indi]) + lnknd, 'wb') as outfile:
				outfile.write(r.content)

	elif set == '000':
		for st in pgs:

			indi = pgs.index(st)

			if (int(st) > -1) and (int(st) < 10):
				pg = ('000' + str(st))
			elif (int(st) >= 10) and (int(st) < 100):
				pg = ('00' + str(st))
			elif (int(st) >= 100) and (int(st) < 1000):
				pg = ('0' + str(st))
			else:
				pg = (st)
			url = lnkst + str(pg) + lnknd
			r = requests.get(url)

			if nmst == '0': 

				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmst == '00':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '00'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '0'
				else:
					nmsetf = ''
			elif nmst == '000':
				if (nms[indi] > -1) and (nms[indi] < 10):
					nmsetf = '000'
				elif (nms[indi] >= 10) and (nms[indi] < 100):
					nmsetf = '00'
				elif (nms[indi] >= 100) and (nms[indi] < 1000):
					nmsetf = '0'
				else:
					nmsetf = ''

			with open(nmsetf + str(nms[indi]) + lnknd, 'wb') as outfile:
				outfile.write(r.content)

def defalt(link):
	url = link
	r = requests.get(url)
	with open('outfile.jpg', 'wb') as outfile:
		outfile.write(r.content)

prm = []

for x in sys.argv:
	prm.append(x)

prm = prm[1:]

strt = 0
end = len(prm)

while strt != end:

	if prm[strt] == '-1':
		i(int(prm[strt + 1]), int(prm[strt + 2]), prm[strt + 3], prm[strt + 4])
		strt += 5
	elif prm[strt] == '-0':
		o(int(prm[strt + 1]), int(prm[strt + 2]), prm[strt + 3], prm[strt + 4])
		strt += 5
	elif prm[strt] == '-00':
		oo(int(prm[strt + 1]), int(prm[strt + 2]), prm[strt + 3], prm[strt + 4])
		strt += 5
	elif prm[strt] == '-000':
		ooo(int(prm[strt + 1]), int(prm[strt + 2]), prm[strt + 3], prm[strt + 4])
		strt += 5
	elif prm[strt] == '-s':
		s(prm[strt + 1], prm[strt + 2])
		strt += 3
	elif prm[strt] == '-c':
		c(prm[strt + 1])
		strt += 2
	elif prm[strt] == '-f':
		f(prm[strt + 1], int(prm[strt + 2]), int(prm[strt + 3]), prm[strt + 4], prm[strt + 5], prm[strt + 6], int(prm[strt + 7]), int(prm[strt + 8]), prm[strt + 9])
		strt += 10
	else:
		defalt(prm[strt])
		strt += 1