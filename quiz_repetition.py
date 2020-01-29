

def main():
    answers = {"Thaddeus Bradley" : "morgan freeman",
    "Jack Dawnson" : "a", "Neo" : "3"}
    correct_answers = 0
    correct_answers += question_1(answers)
    correct_answers += question_2(answers)
    correct_answers += question_3(answers)
    answer_percentage = str(int((correct_answers/3) * 100))
    print('You got ' + answer_percentage + " Percent of answers right" )

def question_1(answers):
    question_right = 0
    ans = input('Who plays Thaddeus Bradley in "Now you see me? ').lower()
    if ans == answers["Thaddeus Bradley"]:
        question_right = 1
        print('Your answer was correct!')
        print()
        return question_right
    else:
        return question_right

def question_2(answers):
    question_right = 0
    print("Who plays Jack Dawnson in Titanic? Is it: \n A) Leonardo DiCaprio \n B) Theodor Rosevelt \n C) Gwenyth Palthrow")
    ans = input("Please enter either A, B or C ").lower()
    if ans == answers["Jack Dawnson"]:
        question_right = 1
        print('Your answer was correct!')
        print()
        return question_right
    else:
        return question_right

def question_3(answers):
    question_right = 0
    ans = input('Who plays Neo in "The Matrix", is it: \n 1) Mike Swarovski \n 2) Mark Hamill \n 3) Keanu Reeves ').lower()
    if ans == answers["Neo"]:
        question_right = 1
        print('Your answer was correct!')
        print()
        return question_right
    else:
        return question_right

main()
