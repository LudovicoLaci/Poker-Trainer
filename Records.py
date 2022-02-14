#!/usr/bin/pyton3
from datetime import datetime
import poker
import Data
import Display
import pandas
import Player2
import math

now = datetime.now()

values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['♣','♦','♥','♠']

class Record:
	def __init__(self, player, answer):
		self.pos = player.pos
		self.stack = player.stack
		self.cards = player.cards
		self.combo = poker.Combo.from_cards(self.cards[0], self.cards[1])
		self.range = poker.Range(Data.get_range(Data.df, math.floor(player.stack), player.pos, 'TOTAL')).combos
		self.answer = answer
		self.correction = None
		self.time = now.strftime("%d/%m/%Y %H:%M:%S")

	def get_range_obj(self):
		return poker.Range(self.range)

	def is_in_range(self):
		combo = poker.Combo.from_cards(self.cards[0], self.cards[1])
		return combo in self.get_range_obj()

	def answer_is_true(self):
		if self.answer == '':
			return True
		else:
			return False

	def display_record(self):
		print(f"cards: {self.cards}")
		print(f"position: {self.pos}")
		print(f"stack: {self.stack}")
		print(f"answer: {self.answer}")

class Records_book:
	def __init__(self, name):
		self.name = name
		self.records = []
		self.records_count = 0
		self.time = now.strftime("%d/%m/%Y %H:%M:%S")
		self.correct_answers = 0
		self.total_answers = 0

	def add_record(self, record):
		self.records.append(record)
		self.records_count += 1

	def correct_records_book(self):
		for record in self.records:
			if record.combo in record.range and record.answer:
				record.correction = True
			elif not(record.combo in record.range) and not(record.answer):
				record.correction = True
			else:
				record.correction = False

	def display_book(self):
		for record in self.records:
			record.display_record()
