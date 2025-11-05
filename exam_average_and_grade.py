"""
Program: Exam Average & Letter Grade
Author: Donaven Bruce
Description: Prompts for three exam scores, computes the rounded average,
then prints the average and a letter grade based on thresholds.
"""

# get three exam scores
exam_score_1 = int(input("Please enter your first exams score :\n"))
exam_score_2 = int(input("Please enter your second exams score :\n"))
exam_score_3 = int(input("Please enter your third exams score :\n"))

# sum and average (rounded)
total_exam_score = exam_score_1 + exam_score_2 + exam_score_3
average_exam_score = round((total_exam_score / 3))

# choose and display letter grade
if average_exam_score >= 90:
  print("Your average score is :" + str(average_exam_score))
  print("Your grade is :A")
elif average_exam_score <= 90 and average_exam_score >= 80:
  print("Your average score is :" + str(average_exam_score))
  print("Your grade is :B")
elif average_exam_score >= 70 and average_exam_score <= 80:
  print("Your average score is :" + str(average_exam_score))
  print("Your grade is :C")
elif average_exam_score < 70:
  print("Your average score is :" + str(average_exam_score))
  print("Your grade is :F")
