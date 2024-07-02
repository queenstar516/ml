assignmentScore = input("Assignment(20): ")
#Verifying that the score is valid
while int(assignmentScore) < 0 or int(assignmentScore) > 20:
    print("LOL, you know that's not possible. Input a valid score")
    assignmentScore = input("Assignment(20): ")

testScore = input("Test(20): ")
#Verifying that the score is valid
while int(testScore) < 0 or int(testScore) > 20:
    print("LOL, you know that's not possible. Input a valid score")
    testScore = input("Test(20): ")

examScore = input("Exam(60): ")
#Verifying that the score is valid
while int(examScore) < 0 or int(examScore) > 60:
    print("LOL, you know that's not possible. Input a valid score")
    examScore = input("Exam(60): ")

#Calculating total score
total = int(assignmentScore) + int(testScore) + int(examScore)

#Determine grade based on total score
if total >= 70:
    print(f"Your total score is {total}. Congratulations, you have an A")
elif total >= 60:
    print(f"Your total score is {total}. Good job, you have a B")
elif total >= 50:
    print(f"Your total score is {total}. Mid, you have a C")
elif total >= 40:
    print(f"Your total score is {total}. Try better next time, you have a D")
elif total >= 0:
    print(f"Your total score is {total}. See you next year, you have an F")
