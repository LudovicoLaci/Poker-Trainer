#!/usr/bin/pyton3

import random
import poker
import Data
import math

POSITIONS = ['UTG','UTG+1','UTG+2','MP','HJ','CO','BU','SB']

class Player:
	def __init__(self):
		self.cards = []
		self.pos = None
		self.stack = None
		self.combo = None

	def cards_to_combo(self):
		return poker.Combo.from_cards(self.cards[0], self.cards[1])

	def combo_to_hand(self):
		return self.cards_to_combo().to_hand()

	def add_card(self, card):
		self.cards.append(card)

	def drop_card(self):
		return self.cards.pop(0)

	def make_random(self):
		positions = POSITIONS
		stacks = ['10', '15', '99', '20', '30']
		random.shuffle(positions)
		random.shuffle(stacks)
		self.pos = positions[0]
		self.stack = int(stacks[0])

	def assign_position_to_player(self, position):
		self.pos = position

	def assign_stack_to_player(self, stack):
		self.stack = stack

	def assign_cards_to_player(self, card_1, card_2):
		self.cards.append(card_1)
		self.cards.append(card_2)
		self.combo = self.cards_to_combo()

	def is_combo_in_range(self, df, BB, POS, PLAY):
		return self.combo in poker.Range(Data.get_range(df,BB,POS,PLAY)).combos

	def is_a_good_question(self):
		if self.stack == 10:
			return self.is_combo_in_range(Data.df,'10',self.pos,'TOTAL')
		elif self.stack == 15:
			return self.is_combo_in_range(Data.df,'15',self.pos,'TOTAL')
		elif self.stack == 99:
			return self.is_combo_in_range(Data.df,'15A',self.pos,'TOTAL')
		elif self.stack == 20:
			return self.is_combo_in_range(Data.df,'20',self.pos,'TOTAL')
		elif self.stack == 30:
			return self.is_combo_in_range(Data.df,'30',self.pos,'TOTAL')
		else:
			print("ERROR!!!")
