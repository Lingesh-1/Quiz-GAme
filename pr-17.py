from questionmodel import Question
from data import question_data
from quiz_brain import QuizBrain

que=[]

for i in question_data:
    qt=i['text']
    qan=i['answer']
    newques=Question(qt,qan)
    que.append(newques)
# print(que)
quiz=QuizBrain(qlist=que)
while quiz.stillhasques():
    quiz.nextqn()

print("YOU HAVE COMPLETED THE QUIZ!!")
print(f"YOUR FINAL SCORE WAS: {quiz.score}/{quiz.qnum}")



















# score=0
# game=True
# gyn=input("Do you want to Play the Quiz Game??? y/n:")
# while game or gyn=='y':
#     ranq=r.choice(q)
#     new_q=Question(ranq['text'],ranq['answer'])
#     print(new_q.t)
#     chosee= input("Enter True/False:").title()
#     if new_q.ans==chosee:
#         # print("\n"*3)
#         score+=1
#         print(f"Your Score is {score}")
#         print(f"{chosee} is correct answer!!!")
#     else:
#         # print("\n"*3)
#         print(f"{chosee} is Wrong answer!!!")
#         print(f"It is {new_q.ans}")
#         print(f"Your Final Score is {score}")
#         game=False