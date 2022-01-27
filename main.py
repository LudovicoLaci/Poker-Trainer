#!/usr/bin/python3

import Deck
import Display
import Player
import Save
import Table

VALUES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
SUITS = ['♣','♦','♥','♠']












###  PROGRAMME MAIN RUN ###
TOTAL_CARD_DEALT = 0
TOTAL_INR_CARD_DEALT = 0
TOTAL_OOFR_CARD_DEALT = 0

deck = Deck()
deck.deck_shuffle()
player = Player('UTG',10)

player.make_random(15,19)

deck.deal_cards_from_deck_to_player(player)
TOTAL_CARD_DEALT += 1

combo = poker.Combo.from_cards(player.cards[0],player.cards[1])
combo_to_hand = combo.to_hand()

for i in range(30):

    ### If 10BB Ranges :
    if int(player.stack) <= 14:
        ### If Player Combo is INR or INBR :
        if combo in poker.Range(BENCB789_OPEN_RANGES_DATABASE['10BB'][player.position]['OPEN_SHOVE']).combos or combo in poker.Range(BENCB789_OPEN_RANGES_DATABASE['10BB'][player.position]['BORDER_RANGE']).combos :
            print('*****************************************')
            print('Combo in range: ' + str(combo))
            player.display_question_to_player(TOTAL_INR_CARD_DEALT)

            TOTAL_INR_CARD_DEALT += 1
        ### If Combo is not INR or INBR :
        else :
            #print('Combo out of range: '+ str(combo))
            TOTAL_OOFR_CARD_DEALT +=1
    ### If 15BB <= Ranges < 20BB:
    elif (int(player.stack) >= 15) and (int(player.stack) <=19):
        ### If Player Combo is INR or INBR :
        if combo in poker.Range(BENCB789_OPEN_RANGES_DATABASE['15BB'][player.position]['OPEN_SHOVE']).combos or combo in poker.Range(BENCB789_OPEN_RANGES_DATABASE['15BB'][player.position]['BORDER_RANGE']).combos :
            print('*****************************************')
            print('Combo in range: ' + str(combo))
            player.display_question_to_player(TOTAL_INR_CARD_DEALT)

            TOTAL_INR_CARD_DEALT += 1
        ### If Player Combo is not INR or INBR:
        else:
            #print('Combo out of range: ' + str(combo))
            TOTAL_OOFR_CARD_DEALT +=1

    deck.drop_cards_back_in_deck(player)
    player.make_random(15,19)
    deck.deck_shuffle()
    deck.deal_cards_from_deck_to_player(player)
    TOTAL_CARD_DEALT += 1
    combo = poker.Combo.from_cards(player.cards[0],player.cards[1])
    combo_to_hand = combo.to_hand()

print('OOFR / CARD DEALT: ' + str(TOTAL_OOFR_CARD_DEALT) + '/' + str(i+1) )
print('INR / CARD DEALT: ' + str(TOTAL_INR_CARD_DEALT) + '/' + str(i+1) )

player.review_record()

output = run("pwd", capture_output=True).stdout

