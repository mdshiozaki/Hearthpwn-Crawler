import hearthstone
from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType
import mysql.connector
from mysql.connector import Error


try: 
	conn = mysql.connector.connect(host='localhost', 
		database='test_hsdecks',
		user='root',
		password='Accessdenied1') # change these values based on the authorization for our server db

	if conn.is_connected():
		print('Connected to test_hsdecks')


		# query inserts into TABLE_NAME(COLUMN1, COLUMN2) where columns are the columns from the table
		query = "INSERT INTO test1(deckcode, url) " \
		"VALUES('testitem1', 'testitem1part2')" # random values that are inserted as a test

		cursor = conn.cursor()
		result = cursor.execute(query)
		conn.commit()
		print("Inserted data")



		deckstring = "AAECAf0GCvIFiQbbBooHzAiX0wLb6QKc+AKPgAOggAMK9wS2B+EHm8IC58sC8dAC8tAC/dACiNIC6OcCAA=="
		deck = deckstrings.Deck().from_deckstring(deckstring)	

		while i < len(fullDeck):
			card = fullDeck[i][0]

			query = "INSERT INTO test2(deckID, "
			



except Error as e:
	print(e)

finally:
	conn.close()



