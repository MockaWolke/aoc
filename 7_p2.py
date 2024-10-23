from get_data import get_aoc_input
from collections import defaultdict
from functools import cmp_to_key

ranks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
data = get_aoc_input(7, 2023)

cards = []

class Card:
    def __init__(self, s):
        
        self.card, number = s.split()
        self.number = int(number)
    
        self.counts = defaultdict(lambda : 0)
    
        for char in self.card:
            self.counts[char] += 1
        
        self.card_type = self.recu_func(self.counts)

    def recu_func(self, counts : dict[str, int]):
        if counts["J"] == 0:
            return self.get_card_type(counts)
        
        vals = []
        
        for char in ranks[:-1]:
            
            new = counts.copy()
            new["J"] -= 1
            new[char] += 1
            vals.append(self.recu_func(new))
            
        return max(vals)
        
    @staticmethod
    def get_card_type(card : dict[str : int]):
        
        keys = sorted(card, key=card.get, reverse=True)
        counts = [card.get(i) for i in keys]
        if counts[0] == 5:
            return 10
        
        if counts[0] == 4:
            return 9
        
        if counts[0] == 3 and counts[1] == 2:
            return 7

        if counts[0] == 3:
            return 6

        if counts[0] == 2 and counts[1] == 2:
            return 5
        
        if counts[0] == 2:
            return 4
        
        return 3
    
    def __lt__(left, right):
        
        
        if left.card_type > right.card_type:
            return False
        
        if left.card_type < right.card_type:
            return True
        
        for l, r in zip(left.card, right.card):
            
            l,r = ranks.index(l), ranks.index(r)
            if l < r:return False
            if l > r: return True
        

    def __eq__(left, right: object) -> bool:
        
        return left.card_type == right.card_type and left.card == right.card
    
    def __repr__(self) -> str:
        return f"Card {self.card}, Rank {self.card_type}\n"
        
cards = [Card(s) for s in data.splitlines()]
    
cards.sort()
val = sum(a * card.number for a,card in enumerate(cards, start = 1))
print(val)