#Game FUNDA Project by:
'''
1- Yashaswini T
2- Varun H S
3- Udai K C
4- Shivam Mittal
5- Sourav Roy
'''
import random
import emoji
def rps():
    player_name = str(input("Enter your name:\n"))
    print("""Game Rules!:Enter your choices in lowercase
                 ROCK wins over scissors,
                 Paper wins over Rock,
                 Scissors wins over Paper""")
    choice = ['rock', 'paper', 'scissors']
    player_choice = 1
    player_win = 0
    computer_win = 0
    while player_choice == 1:
        print('Choices are:', choice)
        player_choice = input('Enter the choice\n')
        comp_choice = choice[random.randint(0, 2)]
        if player_choice == comp_choice:
            print(emoji.emojize(":face_with_hand_over_mouth:"), emoji.emojize(":face_with_hand_over_mouth:"),
                  emoji.emojize(":face_with_hand_over_mouth:"), "Tie!")
            print("Score")
            print("Computer win:", computer_win)
            print("Player win:", player_win)
        elif player_choice == "rock":
            if comp_choice == "paper":
                print("\U0001F923", "\U0001F923", "\U0001F923")
                print("You lose! computer chose", comp_choice, "player chose", player_choice)
                computer_win += 1
                print("Score")
                print("Computer win:", computer_win)
                print("Player win:", player_win)

            else:
                print("\U0001f600", "\U0001f600", "\U0001f600")
                print("You win! player chose", player_choice, "computer chose", comp_choice)
                player_win += 1
                print("Score")
                print("Computer win:", computer_win)
                print("Player win:", player_win)
        elif player_choice == "paper":
            if comp_choice == "scissors":
                print("\U0001F923", "\U0001F923", "\U0001F923")
                print("You lose! computer chose", comp_choice, "player chose", player_choice)
                computer_win += 1
                print("Score")
                print("Computer win:", computer_win)
                print("Player win:", player_win)
            else:
                print("\U0001f600", "\U0001f600", "\U0001f600")
                print("You win! player chose", player_choice, "computer chose", comp_choice)
                player_win += 1
                print("Score")
                print("Computer win:", computer_win)
                print("Player win:", player_win)
        elif player_choice == "scissors":
            if comp_choice == "rock":
                print("\U0001F923", "\U0001F923", "\U0001F923")
                print("You lose! computer chose", comp_choice, "player chose", player_choice)
                computer_win += 1
                print("Score")
                print("Computer win:", computer_win)
                print("Player win:", player_win)
            else:
                print("\U0001f600", "\U0001f600", "\U0001f600")
                print("You win! player chose", player_choice, "computer chose", comp_choice)
                player_win += 1
                print("Score")
                print("Computer win:", computer_win)
                print("Player win:", player_win)
        else:
            print("That's not a valid play. Check your spelling!")

        ch = input("Do you wish to continue(y/n)")
        if ch == "y":
            player_choice = 1
        else:
            if computer_win > player_win:
                print("Computer won the game!,Player", "\U0001F923")
            elif computer_win == player_win:
                print("Match Tie!")
            else:
                print("Player won the game", "\U0001f600")

            print("COME AGAIN", "\U0001f600", "\U0001f600", "\U0001f600")
            break
def hand():
    a = '''------------GAME RULES------------
    1.YOU CAN CHOOSE RANDOM NUMBER FROM 1-10
    2.IF YOUR GUESS AND COMPUTER GUESS ARE DIFFERENT, IT WILL BE TAKEN AS SCORE
    3.YOU WILL BE BATTING FIRST
    4.EACH PLAYER WILL BE GOVEN 20 BALLS TO PLAY
    5.IF YOUR AND COMPUTER GUESS ARE SAME , THEN BATSMAN IS OUT
    6.IF COMPUTER BEATS YOUR SCORE ,COMPUTER WINS (VICE-VERSA)'''
    print(a)
    try:
        choice = input("do you want to continue the game yes or no(y/n)")
    except TypeError:
        choice = input("do you want to continue the game yes or no(y/n)")

    ch = choice.lower()
    if ch == 'n':
        exit()
    else:
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ball1 = 20
    chances1 = 0
    runs1 = 0

    print(" ALL THE BEST !!!!!  now you are batting")
    while chances1 < ball1:

        uruns = int(input("Enter 1-10 Runs for Your Batting Turn: "))
        cball = list1[random.randint(0, 9)]

        if uruns == cball:
            print("Your Guess: ", uruns, ",Computer Guess: ", cball)
            print("You are Out. Your Total Runs= ", runs1, "\n")
            break
        elif uruns > 10:
            print("ALERT!! Support No only till 10\n")
            continue
        else:
            runs1 = runs1 + uruns
            print("Your Guess: ", uruns, ",Computer Guess: ", cball)

            print("Your runs Now are: ", runs1, "\n")

            chances1 = chances1 + 1
    try:
        choice1 = str(input("do you want to continue yes or no (y/n): "))
    except TypeError:
        choice1 = str(input("do you want to continue yes or no (y/n): "))

    ch1 = choice1.lower()
    if ch1 == 'n':
        exit()
    else:
        print("ALL THE BEST !!! YOU ARE BOWLING")
    ball2 = 20
    chances2 = 0
    runs2 = 0

    while chances2 < ball2:

        uball = int(input("Enter Runs for Your Bowling Turn: "))
        cruns = random.choice(list1)

        if cruns == uball:
            print("Computer Guess: ", cruns, "Your Guess: ", uball)
            print("The Computer is Out. Computer Runs= ", runs2, "\n")
            break
        else:
            runs2 = runs2 + cruns
            print("Computer Guess: ", cruns, "Your Guess: ", uball)
            print("Computer Runs: ", runs2, "\n")

            if runs2 > runs1:
                break

        chances2 = chances2 + 1

    print("RESULTS: ")

    if runs2 < runs1:
        print("\nYou won the Game.\n\nYour Total Runs= ", runs1, "\nComputer Total Runs= ", runs2)

    elif runs1 == runs2:
        print("The Game is a Tie")

    else:
        print("\nComputer won the Game.\n\nComputer Total Runs= ", runs2, "\nYour Total Runs= ", runs1)

    b = input("do you want to continue this game yes or no(y/n)")
    if b == 'y':
        hand()
    else:
        main()


def ttt():
    print("SYMBOLS: X  O")
    player1 = input("Player 1 choose your symbol:")
    player2 = input("Player 2 choose your symbol:")
    player1.upper()
    player2.upper()
    print("\n")
    # MAKING THE TIC-TAC-TOE BOARD
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("**TIC-TAC-TOE**")
    print("_____________", '\n')
    for i in range(0, 3):
        for j in range(0, 3):
            print(a[i][j], end=" ")
        print('\n')
    print("_____________")

    for k in range(0, 5):
        choice=input("Do you want continue(y/n)")
        if choice!='y':
            main()

        print(player1, end=" ")
        pos = int(input("Enter the postion you want to fill:"))
        # ENTERING THE SYMBOL ON THE BOARD
        for i in range(0, 3):
            for j in range(0, 3):
                if a[i][j] == pos:
                    a[i][j] = player1.upper()
        print('\n')
        print("**TIC-TAC-TOE**")
        print("_____________", '\n')
        for i in range(0, 3):
            for j in range(0, 3):
                print(a[i][j], end=" ")
            print('\n')
        print("_____________")
        # CHECKING CONDITIONS OF WINNING
        for i in range(0, 3):
            if a[i][0] == a[i][1] == a[i][2] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[i][0] == a[i][1] == a[i][2] == 'O':
                print("O is winner")
                print("Game over!")
                main()
            elif a[0][i] == a[1][i] == a[2][i] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[0][i] == a[1][i] == a[2][i] == 'O':
                print("O is winner")
                print("Game over!")
                main()
            if a[0][2] == a[1][1] == a[2][0] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[0][2] == a[1][1] == a[2][0] == 'O':
                print("O is winner")
                print("Game over!")
                main()
            elif a[0][0] == a[1][1] == a[2][2] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[0][0] == a[1][1] == a[2][2] == 'O':
                print("O is winner")
                print("Game over!")
                main()

        # ENDING THE GAME WHEN ALL THE PLACES ARE FILLED
        if k == 4:
            print("Game draw")
            print("Game over!")
            main()
        print(player2, end=" ")
        pos = int(input("Enter the postion you want to fill:"))
            # ENTERING SYMBOL ON THE BOARD
        for i in range(0, 3):
            for j in range(0, 3):
                if a[i][j] == pos:
                    a[i][j] = player2.upper()
        print('\n')
        print("**TIC-TAC-TOE**")
        print("_____________", '\n')
        for i in range(0, 3):
            for j in range(0, 3):
                print(a[i][j], end=" ")
            print('\n')
        print("_____________")

        # CHECKING CONDITIONS OF WINNING
        for i in range(0, 3):
            if a[i][0] == a[i][1] == a[i][2] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[i][0] == a[i][1] == a[i][2] == 'O':
                print("O is winner")
                print("Game over!")
                main()
            elif a[0][i] == a[1][i] == a[2][i] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[0][i] == a[1][i] == a[2][i] == 'O':
                print("O is winner")
                print("Game over!")
                main()
            if a[0][2] == a[1][1] == a[2][0] == 'X':
                print("X is winner")
                print("Game over!")
                main()
            elif a[0][2] == a[1][1] == a[2][0] == 'O':
                print("O is winner")
                print("Game over!")
                main()
            elif a[0][0] == a[1][1] == a[2][2] == 'X':
                print("X is winner")
                print("Game over!")

                main()
            elif a[0][0] == a[1][1] == a[2][2] == 'O':
                print("O is winner")
                print("Game over!")
                main()
def fortune():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    Jan = ["You Have A Good Sense Of Humour", "You Are Self-Motivated", "You Stay Calm Even During Difficult Times",
           "You have good Leadership Quality", "You Adapt To Every Situation"]
    Feb = ["You are Extremely Loyal", "You take Secrets to your grave", "You are born to do charity",
           "You are creative and Intelligent", "You are selective in picking friends"]
    Mar = ["You have good Intuition", "You have a heart of Gold", "You are Optimistic",
           "You will have Successful career", "You stay devoted to your closed ones"]
    Apr = ["You are super energetic", "You follow heart more than brain", "You believe in your company",
           "You are a born leader", "You are quite sensitive"]
    May = ["You have a positive attitude", "You have a strong will in anything", "You are patient most of the time",
           "You are stubborn and hard-hearted", "You have a positive attitude"]
    Jun = ["You have a dynamic personality", "Your mind is always full of thoughts", "You have a good sense of fashion",
           "You like to do things according to your will", "You never show your true emotions"]
    Jul = ["You are practical and logical in your approach", "You are a positive thinkers",
           "You are close with your family", "You have more mood swings", "You are empathetic in nature"]
    Aug = ["You love being alone", "You love being center of attraction", "You are too sensitive",
           "You are confident individual", "You overcome adverse situations without loosing your energy"]
    Sep = ["You are open minded", "You stick to the truth", "You get anxious many times", "You are quite polite",
           "You will get bored easily"]
    Oct = ["You keep your surroundings calm and quiet", "You have a romantic personality",
           "You are born will high will-power", "You are an opportunist", "You are a good challenger"]
    Nov = ["You are good looking", "You are hardworking", "You have your own rules", "You are often mistaken by others",
           "You are fair in taking decisions"]
    Dec = ["You are down to earth", "You believe in god and karma", "You tend to have good luck",
           "You like sharing your knowledge to rest of the world", "You are good at understandng in nature"]
    career = ["Architecture and Engineering", "Arts, culture and entertainment Industry",
              "Business, management and administration", "Community and social services", "Education Domain",
              "Government Sector", "Health and medicine Sector", "Law and public Sector", "Sales Sector"]
    count = 1
    while count == 1:
        user_name = str(input("Enter your name: "))
        print("Hello!", user_name, ",Choose your birth month:")
        user_month = int(input(
            "1.January\n2.February\n3.March\n4.April\n5.May\n6.June\n7.July\n8.August\n9.September\n10.October\n11.November\n12.December\n "))
        if user_month == 1:
            print(Jan[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 2:
            print(Feb[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 3:
            print(Mar[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 4:
            print(Apr[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 5:
            print(May[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 6:
            print(Jun[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 7:
            print(Jul[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 8:
            print(Aug[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 9:
            print(Sep[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 10:
            print(Oct[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 11:
            print(Nov[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        elif user_month == 12:
            print(Dec[random.randint(0, 4)], "and you will be successfull in", career[random.randint(0, 8)])
        else:
            print("Enter a Valid Choice!")
        choice = ['y', 'n']
        opt = input("Do you wish to continue? Y/N\n")
        opt.lower()
        if opt in choice:
            if opt == 'y':
                count = 1
            elif opt == 'n':
                break
        else:
            print("Choose only between Y/N:")

def quiz():
    # -------------------------
    def new_game():

        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("-------------------------")
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1

        display_score(correct_guesses, guesses)

    # -------------------------
    def check_answer(answer, guess):

        if answer == guess:
            print("CORRECT!")
            return 1
        else:
            print("WRONG!")
            return 0

    # -------------------------
    def display_score(correct_guesses, guesses):
        print("-------------------------")
        print("RESULTS")
        print("-------------------------")

        print("Answers: ", end="")
        for i in questions:
            print(questions.get(i), end=" ")
        print()

        print("Guesses: ", end="")
        for i in guesses:
            print(i, end=" ")
        print()

        score = int((correct_guesses / len(questions)) * 100)
        print("Your score is: " + str(score) + "%")

    # -------------------------
    def play_again():

        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            return True
        else:
            return False

    # -------------------------

    questions = {
        "Who is known as the father of computer?: ": "A",
        "Who is the first Indian to win a Nobel Prize?: ": "B",
        "Which Indian airport uses only solar power to run its operations?: ": "C",
        "Who is the Karnataka Governor 2022?: ": "D",
        "Which planet has the most moons?: ": "C",
        "Who invented electricity?: ": "B",
        "What is the language from which the word ‘Tsunami’ comes from?: ": "D",
        "Kuala Lumpur is the capital of which country?: ": "C", }

    options = [["A. Charles Babbage", "B. Steve Wozniak", "C. Guido van Rossum", "D. Tim Berners-Lee"],
               ["A. CV Raman", "B. Rabindranath Tagore", "C. Kailash Satyarthi", "D. Venkatraman Ramakrishnan"],
               ["A. Chennai International Airport", "B. Rajiv Gandhi International Airport",
                "C. Cochin International Airport", "D. Calicut International Airport"],
               ["A. Shri Jagannath Pahadia", "B. Shri J.B.Patnaik", "c. Shri E.S.L.Narasimhan",
                "D. Thawar Chand Gehlot"],
               ["A. uranus", "B. jupiter", "C. Saturn", "D. mars"],
               ["A. Alessandro Volta", "B. Benjamin Franklin", "C. Thomas Alva Edison", "D. William Shockley"],
               ["A. Spanish", "B. Arabic", "C. Russian", "D. Japanese"],
               ["A. Indonesia", "B. Brunei", "c. Malaysia", "D. Philippines"]]

    new_game()

    while play_again():
        new_game()

    print("untill next time")

    # -------------------------
def main():

    while 1:
        print("1: Rock,Paper and Scissors\n2: Tik-Tac-Toe\n3: Hand Cricket\n4: Fortune Teller\n5: Quiz\n6: EXIT")
        print("Choose The Game you want to play:")
        ch = int(input())
        if ch == 1:
            rps()
        elif ch == 2:
            ttt()
        elif ch == 3:
            hand()
        elif ch == 4:
            fortune()
        elif ch == 5:
            quiz()
        elif ch == 6:
            exit()
        else:
            print("Entered option is out of LIST!")
print(
        "-------------------------------------------------------------Welcome To GAME FUNDA-------------------------------------------------------------------------------------------")
main()