import random
import os 

#Method that runs the dealer part of the app
def dealerGame():
    #Make CardDeck
    cards = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    ]
    random.shuffle(cards)
    
    dealer = []
    player = []

    #Give 1 card to the player and dealer
    player.append(cards.pop())
    dealer.append(cards.pop())

    #Give 2 card to the player and dealer
    player.append(cards.pop())
    dealer.append(cards.pop())
    
    dealerStanding = False
    firstHand = True
    
    #Loop runs and will clear terminal until meeting a break.
    while True:
        os.system('cls' if os.name == 'Windows' else 'clear')
        
        playerHand = totalHand(player)
        dealerHand = totalHand(dealer)

        #Output for showing cards
        print('Player Cards: ({}) [{}]'.format('), ('.join(player), playerHand))
        print('Your Cards: ({}) [{}]'.format('), ('.join(dealer), dealerHand))
        print('')

        print('Choose to hit or stand: ')
        print(' [1] Hit')
        print(' [2] Stand')

        #Conditions for different scenarioes/outcomes
        if dealerStanding:
            if playerHand > 21:
                print('You win! Player is over 21')
            elif playerHand > 21:
                print('Player lost - busted!')
            elif playerHand == dealerHand:
                print('Push!')
            #elif playerHand and dealerHand > 21:
            elif dealerHand > playerHand:
                print('Player lost!')
            elif playerHand <= 18 and playerHand >=14:
                player.append(cards.pop())   
            else:
                print('player wins')
            break
            

        if firstHand and dealerHand == 21:
            print('Dealer wins! - Blackjack')
            break
        elif dealerHand == 21:
            print('Dealer wins! - Blackjack')
            break

        firstHand = False
            
        if dealerHand > 21:
            print('Player wins')
            break
            

        #Dealer gets to choose to stay or hit
        print('')
        choice = input('Your choice:')
        print('')

        if choice == '1':
            dealer.append(cards.pop())
            if playerHand <= 18:
                player.append(cards.pop())
            elif playerHand > 21:
                print('Player lost')
                break 
            elif playerHand == dealerHand:
                print('Push!')
                break
        elif choice == '2':
            if playerHand <= 17:
                player.append(cards.pop())
                if playerHand > dealerHand:
                    print('Player wins')
                elif playerHand == dealerHand:
                    print('Push!')
                else:
                    print('Dealer wins')
            else:
                dealerStanding = True
                if playerHand > dealerHand:
                    print('Player wins')
                #Let the dealer know he has to stay if he hits 17 - like in casinos
                while totalHand(dealer) == 17:
                    print('You have to stand')
                    break


#Method for player part of the app 
def playerGame():
    cards = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    ]
    random.shuffle(cards)
    
    dealer = []
    player = []

    #Give 1 card to the player and dealer
    player.append(cards.pop())
    dealer.append(cards.pop())

    #Give 2 card to the player and dealer
    player.append(cards.pop())
    dealer.append(cards.pop())
    
    playerStanding = False
    firstHand = True

    #Get userInput to print out how much is being bet. 
    userInput = int(input('Choose an amount to bet'))
    
    while True:
        os.system('cls' if os.name == 'Windows' else 'clear')

        
        print("You have made a bet worth: {}".format(userInput))
        
        playerHand = totalHand(player)
        dealerHand = totalHand(dealer)

        #Determines which dealer cards are shown based on player is staying or not
        if playerStanding:
            print('Dealer Cards: ({}) [{}]'.format('), ('.join(dealer), dealerHand))
        else:
            print('Dealer Cards: ({}), (?)'.format(dealer[0]))
            
        print('Your Cards: ({}) [{}]'.format('), ('.join(player), playerHand))
        print('')

        print('Choose to hit or stand: ')
        print(' [1] Hit')
        print(' [2] Stand')

        #Conditions for different scenarioes/outcomes
        if playerStanding:
            if dealerHand > 21:
                print('You win! Dealer is over 21')
                print("You won: {}".format(userInput*2))
            elif playerHand == dealerHand:
                print('Push!')
            elif playerHand > dealerHand:
                print('You win!')
                print("You won: {}".format(userInput*2))
            else:
                print('Dealer wins')
                print("You lost: {}".format(userInput))
            break
            

        if firstHand and playerHand == 21:
            print('You win! - Blackjack')
            print("You won: {}".format(userInput*2))
            break

        firstHand = False
            
        if playerHand > 21:
            print('Busted!')
            print("You lost: {}".format(userInput))
            break
            

        print('')
        choice = input('Your choice:')
        print('')

        #pop a card to the player
        if choice == '1':
            player.append(cards.pop())
        #pop a card to dealer everytime player chooses to stay
        elif choice == '2':
            playerStanding = True
            while totalHand(dealer) <= 16:
                dealer.append(cards.pop())

#Method to handle picturecards and ace(1 or 11). 
def totalHand(hand):
    sum = 0

    nonAcesInHand = [card for card in hand if card != 'A']
    acesInHand = [card for card in hand if card == 'A']

    #Loop cards in hand that are non-ace
    for card in nonAcesInHand:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)
        
    #Loop cards that are ace
    for card in acesInHand:
        if sum <= 10:
            sum += 11
        else:
            sum += 1


    return sum



def main():
    #Check if user wants to play as dealer or player
    playingAsAPlayer = True
    print('BLACKJACK')
    print('')
    print('')

    print('Choose to  play as a Dealer or Player: ')
    print(' [1] Player')
    print(' [2] Dealer')

    print('')
    choiceOfPlay = input('Your choice:')
    print('')

    #Menu
    while True:
        os.system('cls' if os.name == 'Windows' else 'clear')
        if playingAsAPlayer:
            if choiceOfPlay == '1':
                print('Playing as a Player')
                playerGame()
            elif choiceOfPlay == '2':
                print('Fail - playing as a dealer')
                dealerGame()
        break

if __name__ == "__main__":
    main()