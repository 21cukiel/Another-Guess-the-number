def think_a_number():
    """Computer guesses Your number. It has 10 moves"""
    print("Think a number from 0 to 1000. I find it in 10 steps.")
    ans = ["Too small", "Too big", "You win"]
    min = 0
    max = 1000
    guess = 0
    index = 1
    """Computer ask us about random numbers, we give him directions "Too small" or "Too big"
    When computer find our number, we report "You win" """
    while min <= guess <= max:
        guess = int((max - min) / 2) + min
        i = input(f"(Step {index}): I think {guess}: ")
        if i == ans[0]:
            min = guess
            index += 1
        elif i == ans[1]:
            max = guess
            index += 1
        elif i == ans[2]:
            return f"Your number is {guess}, I win!"
            break
        else:
            """If the given hit is not in the dictionary, computer print available hints"""
            return "You must choice one from To small / To big / You win"
            continue
        if index > 10:
            return "Do not cheat!"
            break


if __name__ == '__main__':
    print(think_a_number())
