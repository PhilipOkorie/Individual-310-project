import random

class sportquestions:
    @staticmethod
    def getsportqs(question):
        listquestions={"What is your favourite sport?": "Football",
        "What team do you think is the best?": "Obviously Chelsea",
        "What league is the best league in the world?": "The Premier League is the best in the world",
        "What do you know about basketball?": "I know that Lebron James is the best player in the world",
        "Which sport is popular in Canada?": "Hockey and to be honest, it is quite fascinating",
        "What is your favourite basketball team?": "The Warriors! Like Stephen A. Smith says, they have the best shooter ever!",
        "Are you a sports fan?": "Harvie is a fan of everything, especially sports!"
        }

        listquestionslower = {k.lower():v for k,v in listquestions.items()}
        resp = listquestionslower[question]
        return resp


