import random

play_again = 'y'
while play_again == 'y':
    def deal_card():
        card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        card_random = random.choice(card)
        return card_random

    def score(card):
        if sum(card) == 21 and len(card) == 2:
            return 0
        if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
        return sum(card)

    def declare_winner(dealercards, usercards):
        if user_score == 0:
            return "You win with a blackjack"
        elif dealer_score == 0:
            return "Dealer wins with a blackjack"
        elif user_score == dealer_score :
            return "Push"
        elif user_score > 21:
            return "Bust, dealer wins"
        elif dealer_score > 21:
            return "Dealer bust, you win"
        elif user_score > dealer_score :
            return "You win"
        else:
            return "Dealer wins"


    player_card = []
    dealer_card = []
    game_over = False

    for hand in range(2):
        player_card.append(deal_card())
        dealer_card.append(deal_card())


    user_score = score(player_card)
    dealer_score = score(dealer_card)

    while not game_over:
        user_score = score(player_card)
        computer_score = score(dealer_card)
        print(f"Your cards are {player_card} and your score is {user_score}")
        print(f"Dealer's shown card: {dealer_card[0]} ")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            if user_score == 21 :
                game_over = True
            hit = input("Enter 'Y' to hit and 'N' to stand\n").upper()
            if hit == "Y":
                player_card.append(deal_card())
            elif hit == "N":
                game_over = True
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_card.append(deal_card())
        dealer_score = score(dealer_card)


    print(f"Dealer cards: {dealer_card}",)
    print(f"Dealer score: {dealer_score}")
    print(declare_winner(dealer_score, user_score))
    print ("Game Over.")
    play_again = (input ("Type Y to play again, otherwise press enter: "))
print("Goodbye!")
