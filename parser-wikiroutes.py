from urllib.request import urlopen
from urllib.parse import urljoin
import re
from lxml.html import fromstring

ROUTE_TARGET = 'div.gwt-HTML.RoutePartInfo-content'
TRANSPORT_TYPE = 'div.RoutePartInfo-TransportType.RoutePartInfo-content'

FILENAME = 'transport_kiev.doc'

links = []

page = urlopen('http://wikiroutes.info/kiev/catalog').read().decode('utf-8')
#page = urlopen('http://wikiroutes.info/kiev?routes=6880').read().decode('utf-8')



r = re.compile('(?<=href=").*?routes=\d*(?=")')
for i in r.findall(page):
	links.append(urljoin('http://wikiroutes.info', i))

f = open(FILENAME, 'w')

for i, link in enumerate(links):
	page_route = urlopen(links[i]).read().decode('utf-8')

	list_doc = fromstring(page_route)
	item_route = list_doc.cssselect('div.gwt-HTML.RoutePartInfo-content')
	item_transport_type = list_doc.cssselect('div.RoutePartInfo-TransportType.RoutePartInfo-content')

	f.write(item_transport_type[-1].text)
	f.write('\n')
	f.write(item_route[-3].text)
	f.write('\n')
	#print(item_transport_type[-1].text)
	#print(item_route[-3].text)
f.close()

