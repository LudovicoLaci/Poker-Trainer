#!/usr/bin/pyton3
from datetime import datetime
import poker
import Data

now = datetime.now()

values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['♣','♦','♥','♠']

class Record:
	def __init__(self, pos=None, stack=None , cards=None, answer=None):
		self.pos = pos
		self.stack = stack
		self.cards = cards
		self.range = Data.get_range(Data.df, player.stack, player.pos, 'TOTAL')
		self.answer = answer
		self.correction = None
		self.time = now.strftime("%d/%m/%Y %H:%M:%S")

	def get_range_obj(self):
		return poker.Range(self.range)

	def is_in_range(self):
		combo = poker.Combo.from_cards(self.cards[0], self.cards[1])
		return combo in self.get_range_obj()

	def answer_is_true(self):
		if self.answer = '':
			return True
		else:
			return False

class Records_book:
	def __init__(self, name):
		self.name = name
		self.records = []
		self.records_count = 0
		self.time = now.strftime("%d/%m/%Y %H:%M:%S")
		self.correct_answers = 0
		self.total_answers = 0

	def add_page(self, record):
		self.records.append(record)
		self.records_count += 1

	def correct_records_book(self):



card1 = poker.Card("{}{}".format('T','♠'))
card2 = poker.Card("{}{}".format('9','♠'))
combo = poker.Combo.from_cards(card1, card2)

record = Record('UTG', 10, combo, 'Range')
print(record.time)
answer = combo in poker.Range(Data.get_range(Data.df,10,'UTG','TOTAL')).combos
print(answer)
