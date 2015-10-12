from datetime import date
from urllib.request import urlopen

from lxml.html import fromstring


today = date.today()
print(today.strftime('%d.%m.%y'))


URLS = {'orakul.ua(general)':
			['http://orakul.ua/horoscope/astro/general/today/gemini.html',
			 'div#wrapper div#content div.mCol div.horoBlock p'],
		'orakul.ua(more)':
			['http://orakul.ua/horoscope/astro/more/today/gemini.html',
			 'div#wrapper div#content div.mCol div.horoBlock p'],
		'horo.mail.ru':
			['https://horo.mail.ru/prediction/gemini/today/',
			 'div.layout div.article__text p']}

def horoskop(URLS):
	horo_keys = []
	for i in URLS:
		horo_keys.append(i) #save keys from dict URLS

	for i in horo_keys:
		f = urlopen(URLS[i][0]) #open URL
		list_html = f.read().decode('utf-8')
		list_doc = fromstring(list_html)
		item = list_doc.cssselect(URLS[i][1])
		horo_text = ''
		for elem in item:
			teg_p = elem.cssselect('p')[0]
			horo_text = horo_text + teg_p.text + '\n'
		print(i)
		print(horo_text)

horoskop(URLS)
