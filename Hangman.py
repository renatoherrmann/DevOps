# Eingabe des geheimen Wortes
secret_word = input("Enter a secret word: ").lower()
# print(secret_word)
from pandas import read_table

pics = read_table("HANGMANPICS.txt")

# Initialisierung des Resultats
word_result = ["_"]*len(secret_word)
letters_used = []
calc_mistakes = 0
max_mistakes = 7
print(word_result)
pics_counter = 0

while calc_mistakes < max_mistakes:
    letter = input("Enter a letter: ").lower()

    if letter in letters_used:
        print("Den hattest du schon. Versuche einen anderen Buchstaben")

    elif letter in secret_word:
        for index, char in enumerate(secret_word):
            if char == letter:
                word_result[index] = letter

        if "_" not in word_result:
            print(f"Du hast gewonnen, das gesuchte Wort ist {secret_word}")
            break
        else:
            print("Gut gemacht! Der aktuelle Stand: ", " ".join(word_result))
    else:
        calc_mistakes += 1
        print(f"Falsch! Du hast noch {max_mistakes - calc_mistakes} versuche.")
        print(pics.loc[pics_counter:pics_counter + 6])
        pics_counter += 7

    if calc_mistakes == max_mistakes:
        print(f"Du hast verloren und baumelst am Galgen. Das geheime Wort war {secret_word}")
        break

    letters_used.append(letter)