import random


def game_play():
    def char_insert(word, maskword, guess):
        for i in range(len(word)):
            if word[i] == guess:
                maskword[i] = word[i]
        return maskword

    def game_start_over():
        if input("Начать игру заново? Y/N: ").upper() == "Y":
            return 1
        else:
            print("Спасибо за игру!")
            return 0

    game_restart = 1

    while game_restart:
        words = ["доска", "речка", "банан", "дверь",  "птица", "собака", "мороженое"]
        word_to_guess = random.choice(words)
        wordmask = ["\u25A0" for _ in range(len(word_to_guess))]
        difficulty = {"легко": 5, "средне": 4, "тяжко": 3}
        lives = difficulty.get(input('Выберите уровень сложности: легко, средне или тяжко: '),0)# счетчик жизнёв
        if lives == 0:
            print("Такого уровня сложности нет")
            continue
        print("Первая буква - ", word_to_guess[0])  # Выводит первую букву загаданного слова в тестовых целях

        while lives != 0:
            print(' '.join(wordmask), "| \u2764 x", lives)
            guesstry = input("Введите букву в слове или слово целиком: ")
            if guesstry.isdigit():
                print("Нужно ввести букву или слово целиком, но не цифру")
                continue
            else:
                if len(guesstry) == len(word_to_guess):
                    if guesstry == word_to_guess:
                        print("Правильно! Это слово - ", word_to_guess)
                        game_restart = game_start_over()
                        break

                if len(guesstry) == 1 and guesstry in word_to_guess:
                    wordmask = char_insert(word_to_guess, wordmask, guesstry)
                else:
                    print("Неправильно! Вы теряете жизнь")
                    lives -= 1
                if wordmask == list(word_to_guess):
                    print("Правильно! Это слово - ", word_to_guess)
                    game_restart = game_start_over()
                    break

            if lives == 0:
                print('У вас закончились жизни. Игра окончена')
                game_restart = game_start_over()
                break


game_play()
