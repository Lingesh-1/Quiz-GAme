
class QuizBrain:
    def __init__(self,qlist):
        self.qnum=0
        self.qulist=qlist
        self.score=0
    def stillhasques(self):
        return self.qnum<len(self.qulist)
        #     return True
        # else:
        #     return False
    def checkanswer(self,usans,corrects):
        if usans.lower()==corrects.lower():
            self.score+=1
            print("You are right")
        else:
            print("You are wrong!!!")
        print(f"The Correct answer is {corrects}")
        print(f"Your current Score is {self.score}/{self.qnum}")
        print("\n"*3)
        
    def nextqn(self):
        current_ques=self.qulist[self.qnum]
        self.qnum+=1
        usans=input(f"Q.{self.qnum}: {current_ques.t}? (True/False)").title()
        self.checkanswer(usans,current_ques.ans)
        
    
