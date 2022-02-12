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


### POKER MODULE TESTS ###

'''
c = poker.Suit('c')
print(c)
print('\n *** \n')

c = poker.Rank('J')
print(c)
print('\n *** \n')

print(list(poker.card.Suit))
print('\n *** \n')

print(list(poker.card.Rank))
print('\n *** \n')

c = poker.Card('Ac')
print(c)
print(type(c))
print(c.is_face)
print(c.is_broadway)
print(c.rank)
print(type(c.rank))
print(c.suit)
print(type(c.suit))
print('\n *** \n')

c = poker.Shape('o')
print(c)
c = poker.Shape
print(list(c))
print('\n *** \n')

c = poker.Hand('ATs')
print(c)
print(type(c))
print(c.first)
print(type(c.first))
print(c.second)
print(c.shape)
print(type(c.shape))
print(c.rank_difference)
print(type(c.rank_difference))
print(c.is_broadway)
print(c.is_connector)
print(c.is_offsuit)
print(c.is_one_gapper)
print(c.is_pair)
print(c.is_suited)
print(c.is_suited_connector)
print(c.is_two_gapper)
print(c.to_combos())
print(type(c.to_combos()))
print('\n *** \n')

c = poker.hand.PAIR_HANDS
print(c)
print(type(c))
print(type(c[0]))
print('\n *** \n')

c = poker.hand.OFFSUIT_HANDS
print(c)
print(type(c))
print(type(c[0]))
print('\n *** \n')

c = poker.hand.SUITED_HANDS
print(c)
print(type(c))
print(type(c[0]))
print('\n *** \n')

c = poker.Combo('AcKc')
#print(c.from_cards(poker.Card('Ac'),poker.Card('Js')))
print(c)
print(type(c))
print(c.first)
print(c.second)
print(c.shape)
print(c.is_broadway)
print(c.is_connector)
print(c.is_offsuit)
print(c.is_one_gapper)
print(c.is_pair)
print(c.is_suited)
print(c.is_suited_connector)
print(c.is_two_gapper)
print(c.rank_difference)
print(c.to_hand())
print(type(c.to_hand()))
print('\n *** \n')

c = poker.Range()
c = c.from_objects((Hand('A2s'), Hand('A3s'), Hand('A4s'), Hand('A5s'),
                    Hand('A6s'), Hand('A7s'), Hand('A8s'), Hand('A9s'),
                    Hand('ATs'), Hand('AJs'), Hand('AQs'), Hand('AKs'),
                    Hand('22'), Hand('33'), Hand('44'), Hand('55'),
                    Hand('66'), Hand('77'), Hand('88'), Hand('99'),
                    Hand('TT'), Hand('JJ'), Hand('QQ'), Hand('KK'),
                    Hand('AA')))
print(c)
print(type(c))
print('\n *** \n')

c = poker.Range('A2s+ 22+')
print(c)
print(type(c))
print('\n *** \n')

c = poker.Range('A2s+ 22+').hands
print(c)
print(type(c))
print(type(c[0]))
print('\n *** \n')


c = poker.Range('A2s+ 22+').combos
print(c)
print(type(c))
print(type(c[0]))
print('\n *** \n')

c = poker.Range('A2s+ 22+').percent
print(c)
print(type(c))
print('\n *** \n')

c = poker.Range('A2s+ 22+').rep_pieces
print(c)
print(type(c))
print(type(c[0]))
print('\n *** \n')

c = poker.Range('A2s+ 22+').to_ascii(border=True)
print(c)
print(type(c))
#classmethod from_objects(iterable)
'''
