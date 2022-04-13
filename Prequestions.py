import random

class questions:
    @staticmethod
    def getquestion():
        listquestions=["What is your name?",
        "How are you doing?",
        "What is your favourite food?",
        "What is your favourite movie?",
        "Do you like me?",
        "What is your favourite basketball team?",
        "Are you a sports fan?",
        "Do you watch Netflix?",
        "What was the last movie you saw?",
        "What are you currently watching?",
        "Can I be your friend?",
        "Will you be my best friend?",
        "What do you like to do for fun?",
        "How fast can you run?"]

        index = random.randint(0, len(listquestions)-1)
        return listquestions[index]


