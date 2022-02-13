#!/usr/bin/pyton3

import poker
import Data
import Deck
import Player2
import Records

class Display:
	def __init__(self, cards, pos, stack):
		self.cards = cards
		self.pos = pos
		self.stack = stack

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
