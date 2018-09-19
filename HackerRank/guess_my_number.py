low, high = 0, 100 # the range of potential numbers
too_high, too_low, correct = 'h', 'l', 'c' # to know which region to keep/discard
respond_to_guess = ''

print('Please think of a number between 0 and 100!')

while respond_to_guess != correct:
    guess_number = int((low+high)/2)
    print('Is your secret number ' + str(guess_number) + '?')
    respond_to_guess = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    
    if respond_to_guess == too_high:
        high = guess_number
        # disregard larger half and use smaller half
    elif respond_to_guess == too_low:
        low = guess_number
        # disregard smaller half and use larger half
    elif respond_to_guess == correct:
        print ('Game over. Your secret number was: ' + str(guess_number))
    elif respond_to_guess != too_high or respond_to_guess != too_low:
        print ('Sorry, I did not understand your input.')