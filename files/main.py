# started from https://github.com/EricCharnesky/CIS1501-Fall2021/blob/main/Lab6/main.py

def menu():
    print("DO you want to?")
    print("1 - Add a student")
    print("2 - Add an assignment")
    print("3 - Score assignment")
    print("4 - print the gradebook")
    print("5 - Save gradebook to file")
    print("6 - Load gradebook from file")
    print("7 - quit")
    choice = input()
    return choice

gradebook = {}

choice = ""

while choice != "7":
    choice = menu()
    if choice == "1":
        name = input("Enter the student's name: ")
        gradebook[name] = {}

        if len(gradebook.keys()) > 1:
            for student in gradebook:
                if student != name:
                    for assignment in gradebook[student]:
                        if "points_possible" in assignment:
                            gradebook[name][assignment] = gradebook[student][assignment]
                        elif "score" in assignment:
                            gradebook[name][assignment] = 0
                    break # stop looping through other student keys

    elif choice == "2":
        assignment_name = input("Enter the assignment's name: ")
        points_possible = int(input("How many points is this assignment worth?"))

        for student in gradebook:
            gradebook[student][assignment_name + "_points_possible"] = points_possible
            gradebook[student][assignment_name + "_score"] = 0

    elif choice == "3":
        assignment_to_score = input("What assignment did you want to score?")
        for student in gradebook:
            if (assignment_to_score + "_points_possible") not in gradebook[student]:
                print(f"Unable to find assignment with name of {assignment_to_score}")
                break
            print(assignment_to_score, "points possible: ", gradebook[student][assignment_to_score + "_points_possible"])
            score = int(input("What was the score for " + student + ": "))
            gradebook[student][assignment_to_score + "_score"] = score

    elif choice == "4":
        for student in gradebook:
            print(student, gradebook[student])

    elif choice == '5':
        filename = input("Enter the name of a file to save the gradebook to: ")

        with open(filename + '.txt', 'w') as file:
            for student_name in gradebook:
                for key, value in gradebook[student_name].items():
                    file.write(f'{student_name}~{key}~{value}\n')

    elif choice == '6':
        filename = input("Enter the name of the file to load the gradebook from: ")

        gradebook.clear()

        with open(filename + '.txt') as file:
            lines = file.readlines()
            for line in lines:
                values = line.split("~")
                student_name = values[0]
                key = values[1]
                value = values[2].strip()
                if student_name not in gradebook:
                    gradebook[student_name] = {}
                gradebook[student_name][key] = value