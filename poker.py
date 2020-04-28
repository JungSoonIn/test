# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()


class PKCard(Card):
    """Card for Poker game
    """
    pass
    def value(self) :
        values = dict(zip(ranks, range(2, 2 + len(ranks))))
        for i,j in values.items() :
            if self.card[0]==i :
                return j


if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')

    # comparison
    print(c1 > c2 == c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)

import random
class Deck():
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.cards = [cls(r+s) for s in suits for r in ranks]
        self.rand = random.Random(113)

    def __str__(self) :
        return "{}".format(repr(self.cards))
    
    def __len__(self) :
        return len(self.cards)
    
    def __getitem__(self, index) :
        return self.cards[index]
    
    def shuffle(self) :
        self.rand.shuffle(self.cards)
    
    def pop(self) :
        if not self.cards: raise ValueError("No more cards!")
        return self.cards.pop()

if __name__ == '__main__':
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck)
    # testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)


        

# class Hands:
#     def __init__(self, cards):
#         if len(cards) != 5:
#             raise ValueError('not 5 cards')
#         self.cards = sorted(cards, reverse=True)


#     def is_flush():
#         clover = 0
#         diamond = 0
#         heart = 0
#         spade = 0
#         for card in self.cards :
#             if card[1] == 'C' :
#                 clover += 1
#             elif card[1] == 'D' :
#                 diamond += 1
#             elif card[1] == 'H' :
#                 heart += 1
#             elif card[1] == 'S' :
#                 spade += 1
#         if (clover == 5) or (diamond == 5) or (heart == 5) or (spade ==5) :
#             return True
    
#     def is_straight():
#         l = []
#         for card in self.cards :
#             for rank in values.keys() :
#                 if card[0] == rank :
#                     l.append(values[rank])
#         rankSorted = sorted(l)

#         if (rankSorted[4] == rankSorted[3]+1 == rankSorted[2]+2 == rankSorted[1]+3 == rankSorted[0]+4) or (rankSorted[0] == 2 and rankSorted[1] == 3 and rankSorted[2] == 4 and rankSorted[3] == 5 and rankSorted[4] == 14) :
#             return True

            

#     #""":return: the cards making flush in decreasing order if found, 
#     #        None, otherwise
#     #"""
#     #pass
    
#     def classify_by_rank():
#         checkMyCard = {}
#         for rank in ranks :
#             myCardList = []
#             for card in self.cards :
#                 if card[0] == rank :
#                     myCardList.append(card)
#                 checkMyCard[rank] = myCardList
#         return checkMyCard
    
#     #"""Classify the cards by ranks. 
    
#     #:return: dict of the form { rank: [card, ...], ...}
#     #    None if same ranks not found
#     #"""
#     #pass

#     def find_a_kind():
#         cards_by_ranks = self.classify_by_rank()
#         double = 0
#         triple = 0
#         for key in self.cards_by_ranks.keys() :
#             if len(self.cards_by_ranks[key]) == 2 :
#                 double += 1
#             if len(self.cards_by_ranks[key]) == 3 :
#                 triple += 1
#             if len(self.cards_by_ranks[key]) == 4 :
#                 return 'four of a kind'
#         if double == 1 and triple == 1 :
#             return 'full house'
#         elif double == 1 :
#             return 'one pair'
#         elif double == 2 :
#             return 'two pair'
#         elif triple == 1 :
#             return 'three of a kind'

#         pass
#     #"""Find if one pair, two pair, or three, four of a kind, or full house
    
#     #:return: hand-ranking name including 'Full house'
#     #"""

#     def tell_hand_ranking():
#         if self.is_straight() == True and self.is_flush() == True :
#             return 'straight flush'
#         elif self.is_straight() == True :
#             return 'straight'
#         elif self.is_flush() == True :
#             return 'flush'
#         return self.find_a_kind()


#     def rank() :
#         if self.tell_hand_ranking() == 'straight flush' :
#             return '1'
#         elif self.tell_hand_ranking() == 'four of a kind' :
#             return '2'
#         elif self.tell_hand_ranking() == 'full house' :
#             return '3'
#         elif self.tell_hand_ranking() == 'flush' :
#             return '4'
#         elif self.tell_hand_ranking() == 'straight' :
#             return '5'
#         elif self.tell_hand_ranking() == 'three of a kind' :
#             return '6'
#         elif self.tell_hand_ranking() == 'two pair' :
#             return '7'
#         elif self.tell_hand_ranking() == 'one pair' :
#             return '8'
#         else :
#             return '9'
    
#     if self.rank() > other.rank() :
#         return 'You Win'
#     if self.rank() == other.rank() :
#         if self.rank() == 1 or self.rank() == 4 or self.rank() == 5 :
#             if self.cards[0] > other.cards[0] :
#                 return 'You win'
#             elif self.cards[0] < other.cards[0] :
#                 return 'You lose'
#             else :
#                 if self.cards[1] > other.cards[1] :
#                     return 'You win'
#                 elif self.cards[1] < other.cards[1] :
#                     return 'You lose'
#                 else :
#                     if self.cards[2] > other.cards[2] :
#                         return 'You win'
#                     elif self.cards[2] < other.cards[2] :
#                         return 'You lose'
#                     else :
#                         if self.cards[3] > other.cards[3] :
#                             return 'You win'
#                         elif self.cards[3] < other.cards[3] :
#                             return 'You lose'
#                         else :
#                             if self.cards[4] > other.cards[4] :
#                                 return 'You win'
#                             else :
#                                 return 'You lose'                  

#         if self.rank() == 2 :
#             def fc() :
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 4 :
#                         return key
#                         #print(key)

#             if self.fc() > other.fc() :
#                 return 'You win'
#             elif self.fc() < other.fc() :
#                 return 'You lose'
#             elif self.fc() == other.fc() :
#                 if self.cards_by_ranks[key][4] > other.cards_by_ranks[key][4] :
#                     return 'You win'
#                 else :
#                     return 'You lose'

#         if self.rank() == 3 :
#             def fh() :
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 3 :
#                         return key
#             def fh2() :
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 2 :
#                         return key

#             if self.fh() > other.fh() :
#                 return 'You win'
#             elif self.fh < other.fh() :
#                 return 'You lose'
#             elif self.fh == other.fh() :
#                 if self.fh2() > other.fh2() :
#                     return 'You win'
#                 else :
#                     return 'You lose'

#         if self.rank() == 6 :
#             def trip() :
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 3 :
#                         return key

#             if self.trip() > other.trip() :
#                 return 'You win'
#             elif self.trip() < other.trip() :
#                 return 'You lose'
#             else :
#                 return 'You lose'

#         if self.rank() == 7 :
#             def tp() :
#                 l = []
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 2 :
#                         l.append(key)
#                         l.sort
#                 return l[0]
            
#             def tp2() :
#                 l = []
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 2 :
#                         l.append(key)
#                         l.sort
#                 return l[1]

#             if self.tp() > other.tp() :
#                 return 'You win'
#             elif self.tp() < other.tp() :
#                 return 'You lose'
#             else :
#                 if self.tp2() > other.tp2() :
#                     return 'You win'
#                 else : 
#                     return 'You lose'
        
#         if self.rank() == 8 :
#             def op() :
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 2 :
#                         return key
            
#             if self.op() > other.op() :
#                 return 'You win'
#             elif self.op() < other.op() :
#                 return 'You lose'
#             else :
#                 return 'You lose'

#         if self.rank() == 9 :
#             def np() :
#                 l = []
#                 for key in cards_by_ranks.keys() :
#                     if len(cards_by_ranks[key]) == 1 :
#                         l.append(key)
#                         return max(l)

#             if self.np() > other.np() :
#                 return 'You win'
#             elif self.np() < other.np() :
#                 return 'You lose'
#             else :
#                 return 'You lose'

    
# if __name__ == '__main__':
#     import sys
#     def test(did_pass):
#         """  Print the result of a test.  """
#         linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
#         if did_pass:
#             msg = "Test at line {0} ok.".format(linenum)
#         else:
#             msg = ("Test at line {0} FAILED.".format(linenum))
#         print(msg)

#     # your test cases here
#     pass