#!/usr/bin/pyton3

import random
import poker
import Data

POSITIONS = ['UTG','UTG+1','UTG+2','MP','HJ','CO','BU','SB']

class Player:
	def __init__(self):
		self.cards = []
		self.pos = None
		self.stack = None

	def add_card(self, card):
		self.cards.append(card)

	def make_random(self, low, high):
		positions = POSITIONS
		random.shuffle(positions)
		self.pos = positions[0]
		self.stack = random.randint(low, high)

	def assign_position_to_player(self, position):
		self.pos = position

	def assign_stack_to_player(self, stack):
		self.stack = stack

	def assign_cards_to_player(self, card_1, card_2):
		self.cards.append(card_1)
		self.cards.append(card_2)
