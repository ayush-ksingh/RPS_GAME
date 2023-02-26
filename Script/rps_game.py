import logging
import random

win = lose = tie = 0


def check_win(user, machine):
    win_round = False
    tie_round = False
    if user == 0:
        if machine == 2 or machine == 3:
            win_round = True
            tie_round = False
        elif machine == 1 or machine == 4:
            win_round = False
            tie_round = False
        elif machine == 0:
            tie_round = True
        else:
            logging.info("Weird machine was: %s" % machine)
    elif user == 1:
        if machine == 0 or machine == 4:
            win_round = True
            tie_round = False
        elif machine == 2 or machine == 3:
            win_round = False
            tie_round = False
        elif machine == 1:
            tie_round = True
        else:
            logging.info("Weird machine was: %s" % machine)
    elif user == 2:
        if machine == 1 or machine == 3:
            win_round = True
            tie_round = False
        elif machine == 0 or machine == 4:
            win_round = False
            tie_round = False
        elif machine == 2:
            tie_round = True
        else:
            logging.info("Weird machine was: %s" % machine)
    else:
        raise ValueError('A very specific bad thing happened.')
    if tie_round:
        check_stats(2)
        return "tied!"
    elif win_round:
        check_stats(0)
        return "win!"
    else:
        check_stats(1)
        return "lose!"


def check_stats(wlt):
    global win
    global lose
    global tie
    if wlt == 0:
        win += 1
    elif wlt == 1:
        lose += 1
    else:
        tie += 1


def game():
    choices = ["Rock", "Paper", "Scissors"]
    continue_play = True
    continue_game = ""
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
    except ValueError:
        logging.warning("you must enter an integer \n")

    if choice > 2 or choice < 0:
        while choice > 2 or choice < 0:
            print("You must enter an integer less than three and greater than 0 \n")
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")

    machine_choice = random.randint(0, 2)
    result = check_win(choice, machine_choice)
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machine_choice])
    print("You %s" % result)

    while continue_play:
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
            print("you must enter an integer \n")

        if (choice > 2 or choice < 0) and choice != 5:
            while (choice > 2 or choice < 0) and choice != 5:
                print("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
                try:
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 5:
            print("Thanks for Playing!")
            continue_play = False
        else:
            machine_choice = random.randint(0, 2)
            result = check_win(choice, machine_choice)

            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machine_choice])
            print("You %s" % result)


def display_stats(w_mode, l_mode, t_mode, mode):
    print("\nYou won %d times!\n" % int(w_mode))
    print("You lost %d times!\n" % int(l_mode))
    print("You tied %d times!\n" % int(t_mode))
    if w_mode + l_mode + t_mode != 0:
        percent_won = "{percent:.2%}".format(percent=(w_mode / (w_mode + l_mode + t_mode)))
    else:
        percent_won = "{percent:.2%}".format(percent=0)
    print("You have a %s win rate on %s! \n" % (percent_won, mode))


def main():
    play_again = True
    loop_continue = True
    while play_again:
        loop_continue = True
        play_again = False
        game()
        print("Your stats:")
        display_stats(win, lose, tie, "Rock Paper Scissors!!!")
        while loop_continue:
            continue_game = input("Do you wanna play again? Type Yes or No \n")
            if continue_game.lower() == "yes":
                print("Cool. \n")
                loop_continue = False
                play_again = True
            elif continue_game.lower() == "no":
                print("That's too bad. :( \n")
                loop_continue = False
                play_again = False
            else:
                print("That's not an acceptable answer. Please type Yes or No")
                loop_continue = True


if __name__ == "__main__":
    main()