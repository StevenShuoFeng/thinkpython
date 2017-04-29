"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# from Card import *
from main18 import *

class Hist(object):
    def __init__(self, l = []):
        self.histogram = {}

        for i in l:
            self.histogram[i] = self.histogram.get(i, 0) + 1

    def get(self, x):
        return self.histogram.get(x, 0)


class PokerHand(Hand):

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush', 'straight', 'threekind', 'twopair', 'pair']

    def get_label(self):
        if self.label == None:
            return 'Nothing'
        return self.label

    def suit_hist(self):
        """Builds a histogram of the suits and ranks that appear in the hand.
        """
        self.suits = {}
        self.ranks = {}

        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    # count the unique number of pairs
    def count_num(self, num):
        self.suit_hist()
        cntPair = 0
        for val in self.ranks.values():
            if val == num:
                cntPair += 1
        return cntPair

    def has_pair(self):
        cnt2 = self.count_num(2)
        cnt3 = self.count_num(3)
        return cnt2==1 and cnt3==0

    def has_twopair(self):
        cntPair = self.count_num(2)
        return cntPair == 2

    def has_threekind(self):
        cnt2 = self.count_num(2)
        cnt3 = self.count_num(3)
        return cnt2==0 and cnt3==1

    def has_fourkind(self):
        cnt = self.count_num(4)
        return cnt == 1

    def has_fullhouse(self):
        cnt2 = self.count_num(2)
        cnt3 = self.count_num(3)
        return cnt2==1 and cnt3==1

    def has_straight(self):
        self.suit_hist()
        l = self.ranks.values()
        l.sort()
        for i in range(1, len(l)):
            if l[i] != l[i-1] +1:
                return False
        return True

    def has_straightflush(self):
        return self.has_straight() and self.has_flush()


    def classify(self):
        self.label = None
        for l in PokerHand.all_labels:
            f = getattr(self, 'has_'+l)
            if f():
                self.label = l
                break


class PokerDeck(Deck):

    # shuffles a deck of cards, divides it into hands, classifies the hands, and counts the number of times various classifications appear.
    def shuffle_and_count(self, num_cards = 5, num_hands = 10):
        self.shuffle()

        labels = []
        for i in range(num_hands):
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            labels.append(hand.get_label())

        return labels


if __name__ == '__main__':
    # # make a deck
    # deck = Deck()
    # deck.shuffle()

    # # deal the cards and classify the hands
    # for i in range(7):
    #     hand = PokerHand()
    #     deck.move_cards(hand, 5)
    #     hand.sort()
    #     print '\n', hand
    #     hand.classify()
    #     print hand.get_label()


    lall = []

    n = 10000 # number of iterations
    n_hands = 1

    for i in range(n):
        if i%1000==0:
            print i

        d = PokerDeck()
        l = d.shuffle_and_count(5, n_hands)
        lall += l


    total = float(n_hands*n)
    print  total, ' hands dealt:'

    hist = Hist(lall)
    for l in PokerHand.all_labels:
        freq = hist.get(l)
        if freq == 0:
            continue
        p = freq/total
        print 'p(%s) = %f%% [%d/%.0f]' % (l, p*100, freq, total)




