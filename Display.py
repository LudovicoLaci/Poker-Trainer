#!/usr/bin/pyton3

import poker
import Data
import Deck
import Player2
import Records

class Display:
	def __init__(self, player):
		self.cards = player.cards
		self.pos = player.pos
		self.stack = player.stack

	def show_cards(self):
		return print(f"You have {self.cards[0]}{self.cards[1]}")

	def show_position(self):
		return print(f"Your postion is {self.pos}")

	def show_stack(self):
		return print(f"You have {self.stack}BB")

	def display_situation(self):
		self.show_cards()
		self.show_position()
		self.show_stack()

	def display_question(self, player, records_book):
		self.display_situation()
		answer = input('       ♣♣♣ True or False ? ♣♣♣\n')
		print('\n*****************************************\n')
		record = Records.Record(player.pos, player.stack, player.cards, answer)
		records_book.add_page(record)

	def display_range_terminal(self, record):
		print(record.get_range_obj().to_ascii(boarder=True))
		print(record.get_range_obj().percent, ' %')

	def display_record(self, record):
		print(f"cards: {record.cards}")
		print(f"position: {record.pos}")
		print(f"stack: {record.stack}")
		print(f"answer: {record.answer}")
