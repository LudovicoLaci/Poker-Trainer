#!/usr/bin/python3

import poker
from Deck import Deck
from Display import Display
from Player2 import Player
from Records import Record, Records_book
import Table
import Data

def run_game():

	player1 = Player()
	deck = Deck()
	book1 = Records_book("First book")

	player1.make_random()
	deck.deck_shuffle()

	deck.deal_cards_from_deck_to_player(player1)
	display1 = Display(player1)
	record = Record(player1)

	if player1.is_a_good_question:
		answer = display1.display_question(player1, book1)
		record.set_answer(answer)
		book1.add_record(record)

	book1.display_book()
	print(len(player1.cards))
	print(len(deck.cards))
	deck.drop_cards_back_in_deck(player1)
	print(len(player1.cards))
	print(len(deck.cards))
	book1.display_book()

	return

run_game()
