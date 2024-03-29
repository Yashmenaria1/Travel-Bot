# -*- coding: utf-8 -*-
"""TravelBot.ipynb"""


from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
     [
        r"(.*) your name ?",
        ["My name is TravelBot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*)created(.*)",
        ["Yash Menaria created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*)travel(.*)Sehore|sehore to bhopal|Bhopal(.*)",
        ["You can travel from Sehore to Bhopal by bus or train. The distance is approximately 40 kilometers."]
    ],
    [
        r"(.*)travel(.*)Sehore|sehore to indore|Indore(.*)",
        ["You can travel from Sehore to Indore by bus or train. The distance is approximately 170 kilometers."]
    ],
    [
        r"(.*)travel(.*)Sehore|sehore to ujjain|Ujjain(.*)",
        ["You can travel from Sehore to Ujjain by bus or train. The distance is approximately 200 kilometers."]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you with travel information.",]
    ],
    [
        r"(.*)thank|Thank you | Thanks",
        ["welcome It's my duty."]
    ],
    [
        r"(.*) your name ?",
        ["My name is TravelBot, but you can just call me bot and I'm a travel assistant.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am a virtual assistant, so I exist everywhere!',]
    ],
    [
        r"quit",
        ["Bye for now. Safe travels!","It was nice helping you. Have a great day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I am a travel assistant. I can only help you with travel-related queries."]
    ],
]

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

import random
import re
def travel_response(user_input):
    for pattern, responses in pairs:
        if re.match(pattern, user_input):
            return random.choice(responses)

# Example usage:
user_input = "Can you help me with traveling from Sehore to Bhopal?"
response = travel_response(user_input)
print(response)

print("Hi, I'm TravelBot and If you like to ask \nPlease type lowercase English language to start a conversation. Type quit to leave ")
chat = Chat(pairs, reflections)
chat.converse()
