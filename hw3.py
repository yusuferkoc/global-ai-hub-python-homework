import random
word_list = ["sony", "fujifilm", "canon", "nikon", "hasselblad", "leica", "zeiss"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("ADAM ASMACA ")
 
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Harf veya kelime tahmin et: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Bunu zaten denedin", guess)
            elif guess not in word:
                print(guess, "bu kelimede yok")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "var devam:")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print (guess, "zaten denendi")
            elif guess != word:
                print(guess, "bilemedin")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("geçersiz")
        print(word_completion)
        print("\n")
    if guessed:
        print("çokii! bildin")
    else:
        print("kelime :" + word + ". sonra bi zaman")




def main():
    word = get_word(word_list)
    play(word)
    while input("bi da? (E/H) ").upper() == "E":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()