# Unit Testing Explained
## test_punctuation
The purpose of this test was to check if the bot can interpret the user's input even if they don't include punctuation.

Our test case input was the response: "How are you"

The way our bot works is that matches the user responses to one of the possible keys in a dictionary. (possible_questions in Chatbot.py)

We omitted a question mark and wanted to see if the bot would still be able to return the expected response "I'm pretty good".

## test_ask_me_a_question
We wanted the bot to be able to ask the user a question whenever the user types in "Ask me a question" into the chatbot. Since chatbot will pick a random question from an array, we realized the only way to verify if the returned value is a question is if it ends with a question mark.

So if the getquestion() method returned a string where its last character was equal to ?, then the test would pass.

## test_case
We wanted to also check if the bot can return a response regardless of the case sensitivity of the user's input. Our test input had a string that was a key value of the possible_questions dictionary. Except we also used a combination of upper and lower case characters.

If the returned string of the getResponse() function still matched the value from the possible_questions dictionary, the unit test would pass