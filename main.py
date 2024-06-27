import alphabets
import hangmanart
import random

chosen_word = random.choice(alphabets.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(hangmanart.logo)
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed this alphabet {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"The alpahbet entered {guess} is not in the original letter.")
        if lives == 0:
            end_of_game = True
            print(f"Sorry you run out of your lives, the original letter was {chosen_word}")

    print(f"{' '.join(display)}")
    print(hangmanart.stages[lives])
    if lives == 0:
        print(hangmanart.you_lose)
    if "_" not in display:
        end_of_game = True
        print(hangmanart.you_win)
