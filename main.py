from random import *
import itertools
import random

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
suits_symbols = ['♠', '♣', '♥', '♦']

deck = list(itertools.product(vals, suits_symbols))

random.shuffle(deck)

def showCard(card):
    for val, suit in card:
        s=""
        if val == '10':
            print(' ____________ ')
            print('|            | ')
            print('| %s         |' % (val))
            print('|            | ')
            print('|            | ')   
            print('|     %s      |  ' % (suit))
            print('|            | ')
            print('|            | ')
            print('|        %s  |' % (val))
            print('|____________| ') 
        else:
            print(' ____________ ')
            print('|            | ')
            print('| %s          |' % (val))
            print('|            | ')
            print('|            | ')   
            print('|     %s      |  ' % (suit))
            print('|            | ')
            print('|            | ')
            print('|         %s  |' % (val))
            print('|____________| ') 

def dealCard():
    card = deck.pop()
    return card

def value(card):
    for val, suit in card:
        if val == 'J' or val == 'Q' or val == 'K':
            return 10
        elif val == 'A':
            return 11
        else:
            return int(val)


def startGame():
    print("Welcome to the game of Blackjack!")
    myCards1 =[dealCard()]
    myCards2 =[dealCard()]
    myCards = myCards1 + myCards2
    dealersCard1 = [dealCard()]
    dealersCard2 = [dealCard()]
    dealersCards = dealersCard1
    print("Dealers cards are: ")
    showCard(dealersCards)
    print("Your cards are: ")
    showCard(myCards)
    print("Dealers total is: ")
    dealersTotal = value(dealersCard1)
    myTotal = value(myCards1) + value(myCards2)
    print(dealersTotal)
    print("Your total is: ")
    print(myTotal)
    flag = 0
    while myTotal < 22 and flag == 0:
        if myTotal == 21:
            print("You win!")
            flag = 1
            break
        choice = input("Do you want to hit or stay? (H/S)")
        if choice == "H":
            myCards3 = [dealCard()]
            myCards = myCards + myCards3
            showCard(myCards)
            myTotal = myTotal + value(myCards3)
            print("Your total is: ")
            print(myTotal)
        if choice == "S":
            flag = 1
            print("Dealers turn: ")
            dealersCards = dealersCards + dealersCard2
            showCard(dealersCards)
            dealersTotal = dealersTotal + value(dealersCard2)
            print("Dealers total is: ")
            print(dealersTotal)
            if dealersTotal == 21:
                print("Dealer wins!")
                flag = 1
                break
            if dealersTotal > 17:
                break
            while dealersTotal < 17:
                dealersCard3 = [dealCard()]
                dealersCards = dealersCards + dealersCard3
                showCard(dealersCards)
                dealersTotal = dealersTotal + value(dealersCard3)
                print("Dealers total is: ")
                print(dealersTotal)
                
    if myTotal > dealersTotal and myTotal < 21:
        print("You win!")     
    elif myTotal < dealersTotal and dealersTotal < 21:
        print("Dealer wins!")
    elif myTotal == dealersTotal and myTotal < 21:
        print("It's a tie!")
    if dealersTotal > 21:
        print("Dealer busts! You win!")
    if myTotal > 21:
        print("You bust! You lose!")

if __name__ == "__main__":
    startGame()
    reset = input("Do you want to play again? (Y/N)")
    if reset == "Y":
        startGame()
    print("Thanks for playing!")