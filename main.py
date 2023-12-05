from random import choice

def run_game():
    word_fruits: str = choice(['apple', 'orange', 'banana', 'pineapple'])
    # word_programming_language: str = choice(['C#', 'Java', 'Dart', 'Javascript'])
    # word_subjects: str = choice(['Mathematics', 'Science', 'History', 'Religion'])

    username: str = input("What is your name? ")
    print(f"Hey {username}, Welcome to advanced guessing! ")

    guessed: str = ''
    tries: int = 3
    
    while tries > 0:
        blanks:int = 0
        print("Word ", end='')
        for char in word_fruits:
            if char in guessed:
                print(char, end='')
            else: 
                print('_', end='')
                blanks+=1
        print()
        if blanks == 0:
            print("You got it")
            break
        
        guess:str = input("Enter a guess letter: ")

        if guess == 'abcdefghijklmnopqrstuvwxyz':
            print("you are trying to cheat")
            continue
        
        if guess in guessed:
            print(f"{guess} already used. Try another letter! ")
            continue

        guessed += guess

        if guess not in word_fruits:
            tries -=1
            print(f"Sorry. That is a wrong letter. Try another letter ({tries} tries left!) ")

            if tries ==0:
                print(f"{tries} remaining. You lose!")
                break    

if __name__ == "__main__":
    run_game()
