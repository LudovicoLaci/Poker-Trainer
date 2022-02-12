#!/usr/bin/python3
import poker
from Deck import Deck
import Display
from Player import Player
import Save
import Table
import Data


###  PROGRAMME MAIN RUN ###

def cards_to_combo(player):
	return poker.Combo.from_cards(player.cards[0], player.cards[1])

def combo_to_hand(player):
	return cards_to_combo(player).to_hand()

def is_combo_in_range(df, BB, POS, PLAY, combo):
	return combo in poker.Range(Data.get_range(Data.df,BB,POS,PLAY)).combos

def is_a_good_question(player, combo):
	if player.stack <= 14:
		return is_combo_in_range(Data.df,int('10'),player.position,'TOTAL', combo)
	elif player.stack >= 15 and player.stack <= 19:
		return is_combo_in_range(Data.df,int('15'),player.position,'TOTAL', combo)
	elif player.stack >= 20 and player.stack <= 29:
		return is_combo_in_range(Data.df,int('20'),player.position,'TOTAL', combo)
	else:
		return is_combo_in_range(Data.df,int('30'),player.position,'TOTAL', combo)


def run_game():
	# Initializing player1
	player1 = Player('UTG', 10)
	player1.make_random(5,39)

	# Initializing deck
	deck = Deck()
	deck.deck_shuffle()

	question_count = 0
	while question_count < 10:
		deck.deal_cards_from_deck_to_player(player1)
		combo = cards_to_combo(player1)
		hand = combo_to_hand(player1)
		if is_a_good_question(player1, combo):
			player1.display_question_to_player(0)
			question_count += 1
		else:
			print('Not good')
		deck.drop_cards_back_in_deck(player1)
		deck.deck_shuffle()
		player1.make_random(5,39)

	player1.review_record()
	return

run_game()
