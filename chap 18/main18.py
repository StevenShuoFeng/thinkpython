import random

class Card(object):
	suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
	rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",  "8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, suit = 0, rank = 0):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.suit_names[self.suit], Card.rank_names[self.rank])

	def __cmp__(self, other):
		return cmp((self.suit, self.rank), (other.suit, other.rank))

class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				self.cards.append(Card(suit, rank))

	def __str__(self):
		strlist = []
		for card in self.cards:
			strlist.append(str(card))

		return "\n".join(strlist)

	def add_card(self, card):
		self.cards.append(card)

	def remove_card(self, card):
		self.cards.remove(card)

	def pop_card(self, i=-1):
		return self.cards.pop(i)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())

	def size(self):
		return len(self.cards)

	def allCards(self):
		return self.cards

	# Exercise 18.3.
	def deal_hands(self, numHands, numCards):
		hands = []

		for i in range(numHands):
			h = Hand()
			self.move_cards(h, numCards)
			hands.append(h)

		return hands


class Hand(Deck):
	def __init__(self, label = ''):
		self.cards = []
		self.label = label

def main():
	deck = Deck()
	deck.shuffle()
	# print deck

	hands = deck.deal_hands(3, 5) # deal 5 cards to each of the 3 hands

	for h in hands:
		print '\n', h

	print '\nmethod shuffle belongs to: ', find_defining_class(hands[0], 'shuffle')

	print '\nMove 5 cards from deck to hand:'
	hand = Hand()
	deck.move_cards(hand, 5)
	hand.sort()
	print hand

	print '\nCurrent deck:'
	print deck


def find_defining_class(obj, method_name):
	for ty in type(obj).mro():
		if method_name in ty.__dict__:
			return ty


# main()