import random
from art import logo


# display welcome message
print(logo)
print('Welcome to the Number Guessing Game! ')
print('I\'m thinking of a number between 1 and 100. ')

def game():
    # generate random number between 1 and 100
    generated_num = random.randint(1, 100)
    # print(f'Generated number is {generated_num}. ')


    # ask to select difficulty
    # return a number of attempt depends on choosen difficulty
    # easy - 10 attempts, hard - 5 attempts
    difficulty = input('Please choose a difficulty \'easy\' or \'hard\': ').lower()
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    print(f'You have {attempts} attempts. ')


    # compare generated and guessed numbers
    # create logic to repeat asking for a new guess until win or out of attempts
    user_win = False
    game_over = False
    while attempts > 0 and not user_win:
        guess = int(input('Please make a guess: '))
        if guess == generated_num:
            user_win = True
            game_over = True
            print('Guess is right. You win! ')
        elif guess > generated_num:
            attempts -= 1
            print('Guess is too high. ')
        elif guess < generated_num:
            attempts -= 1
            print('Guess is too low. ')

    if attempts == 0:
        game_over = True
        print('You are out of attempts to guess. ')
    
    if game_over == True:
        if input('Would you like to start from the beggining again? Type \'y\' or \'n\'? ') == 'y':
            game()

game()
