from cards import *

new_card = Card()
new_card.generate_card()
print(new_card)

new_card.set_rank("Nine")
print(new_card)

new_card.set_value(4)
print(new_card)

new_card2 = Card()
new_card2.generate_card()
print(new_card2)

print(new_card.compare_to(new_card2))

print(difference_value(new_card, new_card2))
print(difference_rank(new_card, new_card2))

#Output example

'''
Hearts, Three, 3
Hearts, Nine, 9
Hearts, Four, 4
Hearts, Six, 6
-1
-2
-2
'''