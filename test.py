#!/usr/bin/pyton3

def p_hand(hand):
	"""
	Prints the hand of a player.
	"""
	print(f"\n			Your Hand is: {hand}\n")

def p_flop(flop):
	"""
	Prints the flop.
	"""
	print(f"The Flop is: {flop}")

def p_turn(turn):
	"""
	Prints the turn.
	"""
	print(f"The Turn is: {turn}")

def p_river(river):
	"""
	Prints the river.
	"""
	print(f"The River is: {river}\n")


p_hand('AsAc')
p_flop('AdKs7s')
p_turn('Qh')
p_river('7h')
