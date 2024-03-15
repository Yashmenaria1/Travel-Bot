import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
import random
import re

# Pairs is a list of patterns and responses.
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

def travel_response(user_input):
    for pattern, responses in pairs:
        if re.match(pattern, user_input):
            return random.choice(responses)

def send_message(event=None):
    message = entry.get()
    if message.strip() == "":
        return
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + message + "\n")
    response = travel_response(message)
    chat_history.insert(tk.END, "TravelBot: " + response + "\n")
    chat_history.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    return "break"

root = tk.Tk()
root.title("TravelBot Chatbot")
root.configure(bg="black")

root.minsize(500, 400)  # Set a minimum size for the window

root.pack_propagate(False)  # Prevent the window from resizing based on its content

chat_history = scrolledtext.ScrolledText(root, height=20, width=50, state=tk.DISABLED, bg="black", fg="white")
chat_history.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

entry_frame = tk.Frame(root, bg="brown")
entry_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

entry = tk.Entry(entry_frame, width=50, bg="light grey", fg="black")
entry.pack(side=tk.LEFT, padx=(0, 5), expand=True, fill=tk.X)
entry.bind("<Return>", send_message)

send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="blue", fg="black")
send_button.pack(side=tk.RIGHT, padx=(5, 0))

root.mainloop()
