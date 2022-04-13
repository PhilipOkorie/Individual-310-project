import unittest
from Chatbot import *
from Prequestions import questions

class Testing(unittest.TestCase):
    def test_punctuation(self):
        a = 'How are you'
        b = "I'm pretty good."
        self.assertEqual(getResponse(a,""), b)

    def test_ask_me_a_question(self):
        a = questions.getquestion()[-1]
        self.assertEqual(a, "?")

    def test_case(self):
        a = "WHAT'S your DreaM?"
        b = "To direct a classic western film with Keanu Reeves and Tom Cruise."
        self.assertEqual(getResponse(a, ""), b)


if __name__ == '__main__':
    unittest.main()
