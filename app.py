
from requests import Session
from bs4 import BeautifulSoup as sp



class Ebay:
	session = Session()
	session.headers['Accept'] = r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	session.headers['Accept-Language'] = 'en-US,en;q=0.5'
	session.headers['Connection'] = 'keep-alive'
	session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'

	def __init__(self, product=None):
		self.url = 'https://www.ebay.com/'
		self.url_search = 'sch/i.html?_from=R40&_nkw={}&_sacat=2&_pgn='.format(product)

	# this function is for get in website and search the product
	def get_product(self, page=None):
		try:
			response = self.session.get(self.url+self.url_search+page)
			soup = sp(response.text, 'html.parser')
			products = soup.select('div[class="s-item__title"] > span[role="heading"]')
			return products

		except:
			print('VERIFIQUE A SUA INTERNET!')

	# this function is for get all of price of products
	def get_price(self):
		try:
			response = self.session.get(self.url+self.url_search)
			soup = sp(response.text, 'html.parser')
			prices = soup.select('[class="s-item__price"]')
			return prices

		except:
			print('VERIFIQUE A SUA INTERNET!')

	#this function is for get all of descriptions and prices to show on screen
	def show_price_n_product(self, page=None):
		prices = self.get_price()
		products = self.get_product(page)
		del products[0]
		for product in range(len(products)):
			print(f'DESCRIPTION: {products[product].text}')
			print(f'PRICE: {prices[product].text}')
			print('')

	# this function is for countin' the number of pages that the website get
	def get_pages(self):
		list_url_pages = []
		response = self.session.get(self.url+self.url_search)
		soup = sp(response.text, 'html.parser')
		pages = soup.select('ol[class="pagination__items"] > li a[class="pagination__item"]')
		for page in pages:
			list_url_pages.append(page.get('href').split('https://www.ebay.com/')[1].split('pgn=')[1])

		return list_url_pages
