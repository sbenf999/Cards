import random

class Card:
    def __init__(self, suit=None, rank=None, value=None, values=[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.values = values
        
        self.ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

        #Will be used to be able to change the according suit/value when mutating the suit/value
        self.combined = []
        for index, rank_ in enumerate(self.ranks):
                self.combined.append([rank_, self.values[index]])

    def generate_card(self):
        '''
        Used if you want to generate a card with random values. This is why, as default,
        the __init__ func parameters are set to None. However, if it is supplied with
        parameters, there is no reason to generate a card (thought you can if you want!).
        '''
        self.suit = random.choice(["Diamond", "Hearts", "Clubs", "Spades"])
        self.chosen_index = random.choice(range(len(self.ranks)))
        self.rank = self.ranks[self.chosen_index]
        self.value = self.values[self.chosen_index]
        
    def access(self, value):
        '''
        Uses a dictionary of values to return the user choice. No benefit compared to 3
        seperate functions other than being condensed.
        '''
        values = {"suit": self.suit, "rank": self.rank, "value": self.value}
        return values[value]
    
    def set_suit(self, new):
        self.suit = new            
        return self.suit
    
    def set_rank(self, new):
        self.rank = new
        
        #Ensures that the numerical value is changed with accordance to the new rank
        for sub_set in self.combined:
            if sub_set[0] == new:
                self.value = sub_set[1]
        
        return self.rank
    
    def set_value(self, new):
        self.value = new
        
        #Ensures that the suit is changed with accordance to the new value
        for sub_set in self.combined:
            if sub_set[1] == new:
                self.rank = sub_set[0]
        
        return self.value
    
    def compare_to(self, comparison):
        '''
        Compare the calling object card to another card
        '''
        if self.value > comparison.access("value"):
            return 1
        
        elif self.value < comparison.access("value"):
            return -1
        
        return 0
    
    
    def __str__(self):
        '''
        This is what happens when the object is printed out. Replacement to toString() func
        '''
        return f"{self.suit}, {self.rank}, {self.value}"

#Static methods
    
def difference_value(card1, card2):
    '''
    Static method to get the numerical difference in value
    '''
    return (card1.access("value")-card2.access("value"))

def difference_rank(card1, card2):
    '''
    Static method to get the numerical difference in rank
    '''
    val1 = 0
    val2 = 0
    
    for sub_set in card1.combined:
        if sub_set[0] == card1.access("rank"):
            val1 = sub_set[1]
            
    for sub_set in card2.combined:
        if sub_set[0] == card2.access("rank"):
            val2 = sub_set[1]
        
    return val1 - val2