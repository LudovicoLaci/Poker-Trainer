#!/usr/bin/pyton3
from datetime import datetime
import poker
import Data

now = datetime.now()

values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['♣','♦','♥','♠']

class Record:
	def __init__(self, pos, stack, hand, range):
		self.pos = pos
		self.stack = stack
		self.hand = hand
		self.range = range
		self.ser_num = now.strftime("%d/%m/%Y %H:%M:%S")






card1 = poker.Card("{}{}".format('T','♠'))
card2 = poker.Card("{}{}".format('9','♠'))
combo = poker.Combo.from_cards(card1, card2)

record = Record('UTG', 10, combo, 'Range')
print(record.ser_num)
answer = combo in poker.Range(Data.get_range(Data.df,10,'UTG','TOTAL')).combos
print(answer)
