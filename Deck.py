#!/usr/bin/pyton3
import random
import poker


class Deck:
	def __init__(self):
		values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
		suits = ['♣','♦','♥','♠']
		self.cards = []
		for value in values:
			for suit in suits:
				self.cards.append(poker.Card("{}{}".format(value,suit)))

	def deck_shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		return self.cards.pop(0)

	def show_length(self):
		return len(self.cards)

	def deal_cards_from_deck_to_player(self,player):
		player.cards.append(self.draw_card())
		player.cards.append(self.draw_card())

	def drop_cards_back_in_deck(self,player):
		self.cards.append(player.drop_card())
		self.cards.append(player.drop_card())
