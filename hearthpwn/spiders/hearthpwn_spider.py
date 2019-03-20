import scrapy
import hearthstone
from hearthstone import deckstrings
import mysql.connector
from mysql.connector import Error

class HearthPwnSpider(scrapy.Spider):
	name = "hearthpwn"
	conn = None

	start_urls = [#start page with the filters for recent patch and standard applied
			'https://www.hearthpwn.com/decks?filter-build=47&filter-show-standard=1&filter-deck-tag=5', 
		]

	def connectToDatabase(self):
		try: 
			# database connection established
			self.conn = mysql.connector.connect(host='localhost', 
				database='test_hsdecks',
				user='root',
				password='Accessdenied1',
				auth_plugin='mysql_native_password') 

			if self.conn.is_connected():
				print('Connected to test_hsdecks')

		except Error as e:
			print(e)


	def parse(self, response):
		page_links = response.css('span.tip a::attr(href)').getall() # gets the 25 links in the table on the search page

		for link in page_links:
			next_link = response.urljoin(link) #link is in the form /decks/737557-aggro-token-druid, urljoin links it to the main url
			print(next_link)
			yield scrapy.Request(next_link, callback=self.parse_deck) #calls parse_deck to scrape the data on the given link

		next_page = response.urljoin(response.css('li.b-pagination-item-next a::attr(href)').get()) # searches for next button at bottom of page
		yield scrapy.Request(next_page, callback=self.parse) #cycles back to the beginning to do this for page 2, 3,...


	def parse_deck(self, response):
		# if tavern brawl deck, don't add it
		deckType = response.css('span.deck-type::text').get()

		self.connectToDatabase()

		data = {}
		data['deck'] = []
		for deckcode in response.css('html'):
			code = deckcode.css('button::attr(data-clipboard-text)').get()
			link = response.css('link::attr(href)')[1].get()
			fullDeck = deckstrings.parse_deckstring(code)
			print(fullDeck)

			# query = "INSERT INTO test1(deckcode,url) " \
			# "VALUES(%s,%s)"
			# args = (code, link)

			# cursor = self.conn.cursor()
			# result = cursor.execute(query, args)
			# self.conn.commit()

			# last_ID = "SELECT deck_id FROM test1 ORDER BY deck_id DESC LIMIT 1" # assumes there is at least 1 row in the table


			#get last ID and add 1 to it
			for i in range(len(fullDeck[0])):
				card = fullDeck[0][i][0] #cycles through the first array in the list, pulling the first item which is the card number
				print(card)

				# card_query = "INSERT INTO test2(card_number) " \
				# "VALUES(%s)"
				# args = (card)

				# card_cursor = self.conn.cursor()
				# card_cursor.execute(card_query, (args, ))
				# self.conn.commit()
				