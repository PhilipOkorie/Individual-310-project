# Individual Harvie

# Our very own chatbot - Harvie The MovieBot

Harvie, the conversational chatbot, specializes in talking about film - movies, tv shows and celebrities. The main goal is for it to be able to handle a conversation of at least 30 turns and be able to deal with any possible input.

For now, most of the conversation is based on a series of questions being asked by the user and the bot responding back with answers from an array. We also allowed the bot to be able to ask questions to the reader.

## How to run the bot/install it
For now, we have not compiled the code to be run as an exectuble program. It currently works using a gui

You can clone this remote repository into your own local machine and then run it by either opening `app.py` (or `code app.py a command line once you navigate to the local repository).You must then compiling/running the file using an IDE or using the command `python app` in the terminal.

Note: You will need to have Python installed on your local machine, we recommend having a version *no earlier* than **v 3.9.10**

## Code breakdown:
### Chatbot
for now the chatbot is a simple class that saves that creates an object with a name as its only attribute to identify our chatbot.

### App
contains the Gui implementation of the bot

### getResponse
takes the user's input (as lowercase) and tries to identify a similar string as in a dictionary of possible questions. If it matches a key, the coressponding value (the pre-written answer to the question) is returned. If not, a key error is returned and handled. the use

### questions
this class stores a list of questions, and our bot will randomly pick one and output it to terminal when the user inputs "ask me a question".


### Nerstanza and POStrack
An api we used to find out if the user is typing in past tense or present tense

### NLTK
An api we used to detect synonyms of the words, the bot should be able to understand a word if its a synonym of a word it currently knows

## Chatbot in action

The chatbot is able to take user input and give back answers. However each word does not have to be the exact same as the key in the dictionary to give back the right response.

![image](https://user-images.githubusercontent.com/45835101/159102731-bc2e84cb-25c3-4745-bf22-87a919e66763.png)


It does manage to answer the same question regardless of the casing.

![image](https://user-images.githubusercontent.com/45835101/159102897-e7f26b04-b109-4d82-8b6c-6080bf55aed6.png)


If there is an unexpected input, it is able to return a default message.

![image](https://user-images.githubusercontent.com/45835101/159102914-9e01609d-7b8d-44db-8de0-fe1a93d18812.png)

Once done all the user has to type is `exit` for chatbot to terminate.

![image](https://user-images.githubusercontent.com/45835101/159102958-bdc379f5-b278-4882-baa5-808fb2f690fc.png)

## A3 Features
Handling lack of question mark for questions

Provides more topics like sports and movies

Handling short form requests

Recognizing works of art (use of NER)

Recognizing synonyms, using these to make calculated responses/guess what the user is trying to say

More error handling to guide user input

Ability to ask the user questions, and respond positively or negatively based on simple key words.

## Extra implementations
   I added twitter and spotify API's.
   I was able to add a twitter API that enables the chatbot to retrieve latest tweets by any famous person. In my presentation I used BigSean who is a famous rapper.  So Harvie now can pull  the  latest  tweets  from  a  famous  person,  parse the tweets and know how many likes and when the tweet was put up. Harvie can analyze the tweets.
   Spotify feauture enables you to put random songs onto your playlist and interact with songs that have been added to the bot. He can use those songs when songs are being spoken about.
   
  ![image](screenshots/Screen Shot 2022-04-13 at 5.47.02 PM.png)
   ![image](screenshots/Screen Shot 2022-04-13 at 8.34.47 PM.png)

## Looking ahead
We would love to include the following features to our bot:
- More abilities other than just answering questions such as:
    - quizing the user on movies, tv shows,etc and displaying correct answers at end as a score (trivia mode)
    - being able to give the iMDb synopsis and ratings for a movie using an API
- deploying the bot on a website or as an executable program
- potentially changing the architecture of the software so that the bot is not rule based but instead more intelligent and capable of using NLP to interpret the user's input and give the same response to many similarly worded queries.
