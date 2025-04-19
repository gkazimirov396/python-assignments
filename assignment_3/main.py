import random

from words_fetcher import fetch_words

# Hangman

class Hangman:
    word: str
    guesses: int
    guessed: bool
    word_size: int
    guessed_letters: list[str]

    def __init__(self, available_words: list[str]) -> None:
        self.word = random.choice(available_words).upper()
        self.word_size = len(self.word)
        self.guessed_letters = []
        self.guessed = False
        self.guesses = 8

    def start(self) -> None:
        word_hidden = '.' * self.word_size

        print(f'The word is {word_hidden}')
        print('\n')

        while not self.guessed and self.guesses > 0:
            guessed_letter = input('Guess a letter: ').upper()

            if len(guessed_letter) > 1 or not guessed_letter.isalpha():
                print('Letter must consist of 1 character and be alphabetic!')
                continue

            if guessed_letter in self.guessed_letters:
                print(f'You have already guessed the letter {guessed_letter}!')
                continue
            elif guessed_letter in self.word:
                self.guessed_letters.append(guessed_letter)

                word_hidden_list = list(word_hidden)
                indexes = [i for i, letter in enumerate(
                    self.word) if letter == guessed_letter]

                for i in indexes:
                    word_hidden_list[i] = guessed_letter

                word_hidden = ''.join(word_hidden_list)

                if '.' not in word_hidden:
                    self.guessed = True
                    break

                print(f'The word is {word_hidden}')
                print('\n')
            else:
                self.guesses -= 1
                self.guessed_letters.append(guessed_letter)
                print(f'No such letter! You have {self.guesses} guesses left!')
                print(f'The word is {word_hidden}')
                print('\n')

        if self.guessed and self.guesses > 0:
            print(f'Congrats! You guessed the word {self.word}!')
        else:
            print(f'Sorry, you ran out of guesses. The word was {self.word}.')


words_hangman = fetch_words(min_letters=6, max_letters=12)

hangman = Hangman(words_hangman)
# hangman.start()


# Wordle

class Wordle:
    word: str
    guesses: int
    guessed: bool
    guessed_words: list[str]
    available_words: list[str]

    def __init__(self, available_words: list[str]) -> None:
        self.guesses = 7
        self.guessed = False
        self.guessed_words = []
        self.available_words = available_words
        self.word = random.choice(self.available_words)

    def start(self) -> None:
        while not self.guessed or self.guesses > 0:
            guessed_word = input('Enter a word (5 letters): ')

            if guessed_word not in self.available_words:
                print('This is an unknown word!')
                print('\n')
                continue

            if not guessed_word.isalpha():
                print('Word must be alphabetic!')
                print('\n')
                continue

            if guessed_word in self.guessed_words:
                print(f'You have already guessed the word {guessed_word}!')
                print('\n')
                continue

            guessed_word_modified = list(guessed_word)

            self.guessed_words.append(guessed_word)

            for letter in guessed_word:
                if letter in self.word:
                    letter_index = guessed_word_modified.index(letter)

                    if letter_index == self.word.index(letter):
                        guessed_word_modified[letter_index] = letter.upper()
                    else:
                        guessed_word_modified[letter_index] = letter + '*'

            guessed_word_modified = ' '.join(guessed_word_modified)

            if guessed_word == self.word or guessed_word_modified == self.word:
                self.guessed = True
                break
            else:
                self.guesses -= 1
                print(f'No such letter! You have {self.guesses} guesses left!')
                print('\n')

            if self.guesses == 0:
                print(
                    f'Sorry, you ran out of guesses. The word was {self.word.upper()}.')
                break

            print(guessed_word_modified)
            print('\n')

        if self.guessed and self.guesses > 0:
            print(f'Congrats! You guessed the word {self.word.upper()}!')


words_wordle = fetch_words(min_letters=5, max_letters=5)

worlde = Wordle(words_wordle)
# worlde.start()
