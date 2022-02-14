#!/usr/bin/python3
import poker
from Deck import Deck
from Display import Display
from Player2 import Player
from Records import Record, Records_book
import Table
import Data


###  PROGRAMME MAIN RUN ###

def run_game():
	# Initializing player1
	player1 = Player()
	player1.make_random()

	# Initializing deck
	deck = Deck()
	deck.deck_shuffle()

	# Initializing book
	book1 = Records_book("First book")
	print(type(book1))

	# Initializing display



	question_count = 0
	while question_count < 10:
		deck.deal_cards_from_deck_to_player(player1)
		display1 = Display(player1)
		combo = player1.cards_to_combo()
		hand = player1.combo_to_hand()

		if player1.is_a_good_question:
			answer = display1.display_question(player1, book1)
			record = Record(player1, answer)
			print(record.pos)
			print(record.stack)
			print(record.cards)
			print(record.combo)
			book1.add_record(record)
			book1.display_book()
			question_count += 1
		else:
			print('Not good')

		deck.drop_cards_back_in_deck(player1)
		deck.deck_shuffle()
		player1.make_random()

	display1.display_book(book1)
	book1.display_book()
	return
"""
	book1.display_book()
	book1.correct_records_book()
	print(type(book1))
	book1.display_book()
"""

run_game()
