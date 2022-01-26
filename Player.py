class Player:
    POSITIONS = ['UTG','UTG+1','UTG+2','MP','HJ','CO','BU','SB']
    def __init__(self, position, stack):

        self.input_record = []
        self.record = []
        self.cards = []
        self.position = position
        self.stack = stack


    def add_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        return print("{} {}{}".format('We have: ',self.cards[0],self.cards[1]))

    def show_position(self):
        return print( 'Position:' + ' ' + str(self.position) )

    def show_stack(self):
        return print( 'Stack:' + ' ' + str(self.stack) +' BB')

    def drop_card(self):
        return self.cards.pop(0)

    def make_random(self,x,y):
        positions = self.POSITIONS
        random.shuffle(positions)
        self.position = positions[0]
        self.stack = random.randint(x,y)

    def assign_position_to_player(self, position):
        self.position = position

    def assign_stack_to_player(self, stack):
        self.stack = stack

    def assign_cards_to_player(self, card_1, card_2):
        self.cards.append(card_1)
        self.cards.append(card_2)

    def display_situation(self):
        print('\n            ♣♣♣ Q'+ str(i+1) +' ♣♣♣\n')
        self.show_cards()
        self.show_position()
        self.show_stack()

    def display_question_to_player(self, i):
        self.display_situation()
        self.add_record()

    def add_record(self):
        answer = input('       ♣♣♣ True or False ? ♣♣♣\n')
        print('\n*****************************************\n')
        self.input_record.append(answer)
        self.record.append([str(poker.Combo.from_cards(self.cards[0],self.cards[1])), self.position, str(self.stack) + ' BB', answer])

    def get_range_from_record(self, stack_record, record, category='OPEN_SHOVE'):
        return poker.Range(BENCB789_OPEN_RANGES_DATABASE[stack_record][record[1]][category])

    def is_in_range(self, stack_record, record, category):
        if poker.Combo(record[0]) in self.get_range_from_record(stack_record, record, category).combos:
            return True
        if poker.Combo(record[0]) not in self.get_range_from_record(stack_record, record, category).combos:
            return False

    def answer_is_true(self, record):
         if record[3] == 'True' or 'T' or '1' or '':
             return True
         if record[3] == 'False' or 'f' or '0' or 'F':
             return False

    def display_review(self, review_count, card_record, position_record, stack_record, answer_record):
        print('                               ♣♣♣ Q'+ str(review_count+1) +' ♣♣♣')
        print('players cards were: ' + card_record , '      ***', poker.Combo.to_hand(poker.Combo(card_record)), '***')
        print('players position was: ' + position_record)
        print('players stack was: '+ stack_record)
        print('Your answer was: ' + answer_record)


    def stack_strip(self, record):
            return int(record[2].strip(' BB'))

    def print_range_from_record(self, stack_record, record, category='OPEN_SHOVE'):
        print('\n'+ 'The Correct Range is:')
        print(self.get_range_from_record(stack_record, record, category).to_ascii(border=True))
        print(self.get_range_from_record(stack_record, record, category).percent, ' %')

    def review_record(self):
        print('Reviewing Record...')
        print('Reviewing Record...')
        print('Reviewing Record...')

        review_count = 0
        TOTAL_CORRECT_ANSWERS = 0
        for records in self.record:
            print('                               Record number: '+str(review_count+1))
            print(records)
            if self.stack_strip(records) < 15:
                if self.is_in_range('10BB', records, 'OPEN_SHOVE') and self.answer_is_true(records):
                    self.display_review(review_count, records[0],records[1],records[2],records[3])
                    print('Your answer is Correct           11')
                    self.print_range_from_record('10BB', records)
                    records.append([self.is_in_range('10BB', records, 'OPEN_SHOVE'), self.answer_is_true(records), True])
                    TOTAL_CORRECT_ANSWERS +=1
                elif self.is_in_range('10BB', records, 'OPEN_SHOVE') or self.answer_is_true(records):
                    self.display_review(review_count, records[0],records[1],records[2],records[3])
                    print('Your answer is wrong             12')
                    self.print_range_from_record('10BB', records)
                    records.append([self.is_in_range('10BB', records, 'OPEN_SHOVE'), self.answer_is_true(records), False])
                elif not(self.is_in_range('10BB', records, 'OPEN_SHOVE') and self.answer_is_true(records)):
                    self.display_review(review_count, records[0],records[1],records[2],records[3])
                    print('Your answer is Correct           13')
                    self.print_range_from_record('10BB', records)
                    records.append([self.is_in_range('10BB', records, 'OPEN_SHOVE'), self.answer_is_true(records), True])
                    TOTAL_CORRECT_ANSWERS +=1
            elif 15 <= self.stack_strip(records) < 20:
                if self.is_in_range('10BB', records, 'OPEN_SHOVE') and self.answer_is_true(records):
                    self.display_review(review_count, records[0],records[1],records[2],records[3])
                    print('Your answer is Correct           21')
                    self.print_range_from_record('15BB', records)
                    records.append([self.is_in_range('10BB', records, 'OPEN_SHOVE'), self.answer_is_true(records), True])
                    TOTAL_CORRECT_ANSWERS +=1
                elif self.is_in_range('10BB', records, 'OPEN_SHOVE') or self.answer_is_true(records):
                    self.display_review(review_count, records[0],records[1],records[2],records[3])
                    print('Your answer is Wrong             22')
                    self.print_range_from_record('15BB', records)
                    records.append([self.is_in_range('10BB', records, 'OPEN_SHOVE'), self.answer_is_true(records), False])
                elif not(self.is_in_range('10BB', records, 'OPEN_SHOVE') and self.answer_is_true(records)):
                    self.display_review(review_count, records[0],records[1],records[2],records[3])
                    print('Your answer is Correct           23')
                    self.print_range_from_record('15BB', records)
                    records.append([self.is_in_range('10BB', records, 'OPEN_SHOVE'), self.answer_is_true(records), True])
                    TOTAL_CORRECT_ANSWERS +=1
            else:
                print('pppppppppppp')
            review_count+=1
        print(player.record)
        print('Total correct answers : ' +str(TOTAL_CORRECT_ANSWERS) +'/'+ str(review_count))

