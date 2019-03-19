import scrapy
import hearthstone
from hearthstone import deckstrings
import mysql.connector
from mysql.connector import Error

class HearthPwnSpider(scrapy.Spider):
	name = "hearthpwn"
	conn = None

	start_urls = ['https://www.hearthpwn.com/decks/1238737-legend-control-warlock',
			'https://www.hearthpwn.com/decks/1240710-control-otk-mage-poor-players-like-me', 
			'https://www.hearthpwn.com/decks/1238561-pogo-rogue',
		]

	def connectToDatabase(self):
		try: 
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
		# if tavern brawl deck, don't add it
		deckType = response.css('span.deck-type::text').get()
		if deckType == 'Tavern Brawl':
			return

		self.connectToDatabase()
		data = {}
		data['deck'] = []
		for deckcode in response.css('html'):
			code = deckcode.css('button::attr(data-clipboard-text)').get()
			link = response.css('link::attr(href)')[1].get()
			fullDeck = deckstrings.parse_deckstring(code)

			query = "INSERT INTO test1(deckcode,url) " \
			"VALUES(%s,%s)"
			args = (code, link)

			cursor = self.conn.cursor()
			result = cursor.execute(query, args)
			self.conn.commit()


			#get last ID and add 1 to it

			# for each card in fulldeck:


