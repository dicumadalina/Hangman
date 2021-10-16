import random
words_list = ["python", "java", "kotlin", "javascript"]
chose = random.choice(words_list)
dashed = list(len(chose) * '-')
dashed_w = []
entries = 8

while True:
    print('H A N G M A N')
    get_value = input('Type "play" to play the game, "exit" to quit: ')
    if get_value == 'play':
        while entries > 0:
            print()
            print("".join(dashed))
            guess = input("Input a letter: ")
            if (not guess.islower() or not guess.isalpha()) and len(guess) == 1:
                print('Please enter a lowercase English letter')
                continue
            if not len(guess) == 1:
                print('You should input a single letter')
                continue
            if guess in dashed_w:
                print("You've already guessed this letter")
                continue
            dashed_w.append(guess)
            if guess in chose:
                # if guess in dashed:
                # print("You've already guessed this letter")
                for i in range(0, len(chose)):
                    if chose[i] == guess:
                        dashed[i] = guess
            else:
                print("That letter doesn't appear in the word")
                entries -= 1
            if "".join(dashed) == chose:
                print("".join(dashed))
                print("You guessed the word!\nYou survived!")
                break
        if entries == 0 and dashed != chose:
            print("You lost!")
    elif get_value == 'exit':
        break
