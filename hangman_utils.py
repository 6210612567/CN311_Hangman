import random

word = ['hello', 'world']
heart = 8
passed_char = []


def main():
    select_word = random_word()
    n_word = len(select_word)

    print(select_word)


def random_word():
    n_random = random.randint(0, len(word) - 1)
    select_word = word[n_random]

    return select_word


# def check(select_word, n_word, wrong, input_char):
#     while wrong > 0:
#         check_char = True
#         correct = 0

#         # check passed_char got chars
#         if len(passed_char) > 0:
#             for j, char in enumerate(passed_char):
#                 if input_char.lower() == char:
#                     check_char = False
#                     print("same input as before")
#         # input not same as before
#         if check_char:
#             for i, char2 in enumerate(select_word):
#                 if input_char.lower() == char2:
#                     correct += 1
#             passed_char.append(input_char)
#             print("char:", ', '.join(passed_char))

#             if correct != 0:
#                 n_word -= correct

#                 if n_word <= 0:
#                     print("congrat")
#                     print("heart", wrong, "left")
#                     break
#                 else:
#                     print("correct")
#             else:
#                 wrong -= 1
#                 if wrong == 0:
#                     print("Jokes over you're dead")
#                     break
#                 else:
#                     print("heart", wrong, "left")
#                     print("wrong!")

#         print("-------------------------")

def check_occured(input_char):
    input_char = input_char.lower()
    if len(passed_char) > 0:
        for j, char in enumerate(passed_char):
            if input_char == char:
                return True
    return False


def isDead(heart):
    if heart < 0:
        return True
    return False


def check_word(select_word, heart, input_char, word_corrected, passed_char):
    input_char = input_char.lower()
    correct = 0
    n_word = len(select_word)

    if (not check_occured(input_char)) and (not isDead(heart)):
        for char in select_word:
            if input_char == char:
                correct += 1

        passed_char.append(input_char)
        print("char:", ', '.join(passed_char))

        if correct > 0:
            word_corrected += correct
            if word_corrected == n_word:
                print("congrat")
                print("heart", heart, "left")

            else:
                print("correct")
        else:
            heart -= 1
            if heart < 0:
                print("Jokes over you're dead")
            else:
                print("heart", heart, "left")
                print("wrong!")

    else:
        print("same input as before")

    print("-------------------------")

    return heart, word_corrected, passed_char


if __name__ == "__main__":
    main()
