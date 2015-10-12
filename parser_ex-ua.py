from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring
from lxml.etree import XMLSyntaxError
from os.path import isfile

import xlsxwriter

URL = 'http://www.ex.ua'
TARGET = '/87716417?r=28739,23777'

def parse_ex_ua():
	links = []
	names = []
	url = urljoin(URL, TARGET)
	page = urlopen(url)
	list_html = page.read().decode('utf-8')
	list_doc = fromstring(list_html)
	ex = list_doc.cssselect('head title')[0]
	print(ex.text)

	item = list_doc.cssselect('td.small span.r_button_small a')
	item2 = list_doc.cssselect('table.list tr td a')
	for name in item2:
		q = name.get('title')
		rel = name.get('rel')
		if rel != "nofollow" and q != None:
			#pass
			#print(q)
			names.append(q)
	for link in item:
		a = link.get('href')
		if link.text == 'загрузить':
			a = urljoin(URL,a)
			links.append(a)
			#print(link.text,a)
	return names, links

def download_from_ex_ua(names, links):
	for name, link in zip(names,links):
		ex_file = urlopen(link).read()
		filename = name
		if isfile(filename):
			continue
		f = open(filename,'wb')
		f.write(ex_file)
		f.close()
	return 'All files was downloaded'


n,l = parse_ex_ua()
download_from_ex_ua(n, l)