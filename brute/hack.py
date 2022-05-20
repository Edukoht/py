import string
import time
from datetime import datetime

# Придумайте себе cекрет (например, "abcd") и запишите его в файл hacker_secret.txt.
# Вы можете использовать только символы, указанные внизу!
# Если хотите использовать большие буквы, просто добавьте их в список, удалив "#" в правильном месте.
# Для более успешного взлома рекомендуется начать с более короткого имени (три-четыре символа - идеальная длина!):

possible_symbols = "abcdefghijklmnopqrstuvwxyz_-0123456789"     # + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
first_symbol = possible_symbols[0]      # Тут хранится буква "а" (она маленькая!)
last_symbol = possible_symbols[len(possible_symbols) - 1]      # а тут - цифра 9

timer = datetime.now() # Засекаем время

with open('brute/hacker_secret.txt') as f:
    hacker_secret_to_hack = f.read() # Тут программа считывает, что именно вы загадали

    guess = first_symbol
    current_length = 1 # А тут - делает первое предположение: букву "а"

    while guess != hacker_secret_to_hack:
        time.sleep(0.05) # Это выводятся предположения в консоль снизу. Удалите эту строку для скорости!
        print(guess) # Для суперскорости можно удалить и эту строку, но тогда вы не будете видеть, что сейчас проверяет код
        

        # Всё, что ниже - это алгоритм поиска, который каждый раз проверяет следующее значение
        if guess[0] == last_symbol:
            current_length += 1
            print("Начинается проверка секретов длиной " + str(current_length))
            guess = first_symbol
            while len(guess) < current_length: guess += first_symbol
        else:
            for i in range(1, len(guess) + 1):
                if guess[-i] == last_symbol:
                    guess = guess[:-i] + first_symbol
                    while len(guess) < current_length: guess += first_symbol
                else:
                    guess = guess[:-i] + possible_symbols[possible_symbols.index(guess[-i]) + 1]
                    while len(guess) < current_length: guess += first_symbol
                    break

    print("Вы взломаны! Ваш секрет был: " + guess)
    print("Времени ушло: " + str(datetime.now() - timer))
