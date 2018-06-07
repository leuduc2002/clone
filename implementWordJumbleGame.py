from random import *

list_word = ["fuck", "shit", "hype", "sexy", "essketit"]
end = 5

while True:
    random_number = randint(0, len(list_word) - 1)
    random_word = list_word[random_number]
    list_word.pop(random_number)
    char_list_in_order = []
    char_list_in_random = []
    do_dai = len(random_word)
    end = end - 1

    for i in range(do_dai):
        char_list_in_order.append(random_word[i])
    for _ in range(do_dai):
        thu_tu_random = randint(0, len(char_list_in_order) - 1)
        random_char = char_list_in_order[thu_tu_random]
        char_list_in_random.append(random_char)
        char_list_in_order.pop(thu_tu_random)

    print(*char_list_in_random, sep=" "
    while True:
        doan = input("enter word: ")
        if doan.lower() == random_word:
            print("Correct")
            break
        print("Incorrect")
    if end != 0:
        while True:
            action = input("Next / Stop: ")
            if action.lower() == "next":
                print("Next question:")
                break
            elif action.lower() == "stop":
                end = 0
                print("Game over")
                break
            else:
                print("Syntax error")
    else:
        print("You WIN!!!")
        break

