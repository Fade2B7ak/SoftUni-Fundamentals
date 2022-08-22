card_deck = input().split()
number_of_shuffles = int(input())
final_deck = []

for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(card_deck) // 2
    left_half = card_deck[0:middle_of_the_deck]
    right_half = card_deck[middle_of_the_deck::]
    for card in range(len(left_half)):
        final_deck.append(left_half[card])
        final_deck.append(right_half[card])
    card_deck = final_deck

print(card_deck)

#Functional solving of the problem.
def farro_shuffle(card_deck, count_of_shuffles):
    final_deck = []

    # Looping through the shuffles, so we can split the deck on 2 hals.
    for shuffle in range(count_of_shuffles):
        final_deck = []
        half_deck = len(card_deck) // 2
        left_half = card_deck[0:half_deck]
        right_half = card_deck[half_deck::]

        # Looping the 2 half's and append them to the list by values.
        for card in range(len(left_half)):
            final_deck.append(left_half[card])
            final_deck.append(right_half[card])
        card_deck = final_deck

    print(card_deck)


farro_shuffle(card_deck=input().split(), count_of_shuffles=int(input()))
