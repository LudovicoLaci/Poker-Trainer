#!/usr/bin/python3
import poker
from Deck import Deck
import Display
from Player import Player
import Save
import Table
import pandas as pd

df = pd.DataFrame(pd.read_excel("Ranges.xlsx"))

def get_range(df, BB, POS, PLAY):
	range = df['RANGE'].loc[(df["BB"] == BB)
		& (df["POS"] == POS)
		& (df["PLAY"] == PLAY)]
	return range.values[0]
#print(type(get_range(df, 10, 'UTG', 'OPEN_SHOVE')))


###  PROGRAMME MAIN RUN ###

def cards_to_combo(player):
	return poker.Combo.from_cards(player.cards[0], player.cards[1])

def combo_to_hand(player):
	return cards_to_combo(player).to_hand()

def is_combo_in_range(df, BB, POS, PLAY, combo):
	return combo in poker.Range(get_range(df,BB,POS,PLAY)).combos

def is_a_good_question(player, combo):
	if player.stack <= 14:
		return is_combo_in_range(df,int('10'),player.position,'TOTAL', combo)
	elif player.stack >= 15 and player.stack <= 19:
		return is_combo_in_range(df,int('15'),player.position,'TOTAL', combo)
	elif player.stack >= 20 and player.stack <= 29:
		return is_combo_in_range(df,int('20'),player.position,'TOTAL', combo)
	else:
		return is_combo_in_range(df,int('30'),player.position,'TOTAL', combo)


def run_game():
	# Initializing player1
	player1 = Player('UTG', 10)
	player1.make_random(5,30)

	# Initializing deck
	deck = Deck()
	deck.deck_shuffle()

	deck.deal_cards_from_deck_to_player(player1)
	combo = cards_to_combo(player1)
	hand = combo_to_hand(player1)

	if is_a_good_question(player1, combo):
		player1.display_question_to_player(0)
	else:
		print('Not good')

	return

run_game()
