# Project 1: Cindy - Rule-Based AI Chatbot
# Intern Name: Divyanjali Mandadi
# Batch: 2026
# Organization: DecodeLabs
# Bot Name: Cindy

responses = {
    "hello":                    "Hey there! How can I help you today?",
    "hi":                       "Hi! Great to see you 😊",
    "hey":                      "Hey! What's up?",
    "how are you":              "I'm just a bot, but I'm doing great!",
    "what is ai":               "AI means making computers think like humans!",
    "what is python":           "Python is a beginner friendly programming language!",
    "what is a chatbot":        "A chatbot is a program that simulates conversation!",
    "your name":                "I'm Cindy, your Rule-Based AI assistant!",
    "who made you":             "An intern at DecodeLabs made me!",
    "tell me a joke":           "Why did the robot go on vacation? It needed to recharge! 😂",
    "help":                     "Try: hello, how are you, what is ai, tell me a joke",
    "good morning":             "Good morning ☀️ Hope you have an amazing day!",
    "good afternoon":           "Good afternoon 😄 How's your day going?",
    "good evening":             "Good evening 🌙 Ready to chat?",
    "good night":               "Good night 😴 Sleep well and dream big!",
    "what is machine learning": "Machine Learning is when computers learn from data!",
    "what is coding":           "Coding is giving instructions to computers using programming languages.",
    "what is data science":     "Data Science is the art of finding insights from data.",
    "what is cybersecurity":    "Cybersecurity protects systems and data from hackers.",
    "what is cloud computing":  "Cloud Computing means storing and accessing data over the internet.",
    "i am bored":               "Let's do something fun 😎 Want a joke or a quiz?",
    "motivate me":              "Success starts with consistency 💪 Keep going!",
    "exam stress":              "Stay calm 😌 One step at a time, you've got this!",
    "tips for studying":        "Study smart: focus, revise, and take short breaks 📚",
    "tell me another joke":     "Why was the computer cold? Because it left its Windows open 😂",
    "do you like humans":       "Of course! Humans created me 🤖❤️",
    "can you dance":            "Only in binary 💃 101010!",
    "sing a song":              "La la la 🎵 I'm better at coding than singing!",
    "are you real":             "I'm virtually real 😄",
    "who is your boss":         "You are the boss here 😎",
    "can you learn":            "I can improve with more data and training!",
    "what can you do":          "I can chat, answer questions, and make your day better ✨",
    "bye":                      "Goodbye! Have a wonderful day 👋"
}

print("   Welcome to Cindy 🤖")
print("   Your Rule-Based AI Assistant")
print("   Type 'bye' to stop chatting.")

while True:

    raw = input("\nYou: ")
    clean = raw.lower().strip()

    if clean == "bye":
        print("Cindy:", responses.get(clean))
        break

    elif clean == "hello" or clean == "hi" or clean == "hey":
        print("Cindy:", responses.get(clean))

    elif clean == "good morning" or clean == "good afternoon" or clean == "good evening" or clean == "good night":
        print("Cindy:", responses.get(clean))

    elif clean == "your name":
        print("Cindy:", responses.get(clean))

    elif clean == "who made you":
        print("Cindy:", responses.get(clean))

    elif clean == "how are you":
        print("Cindy:", responses.get(clean))

    elif clean == "what can you do":
        print("Cindy:", responses.get(clean))

    elif clean == "are you real":
        print("Cindy:", responses.get(clean))

    elif clean == "who is your boss":
        print("Cindy:", responses.get(clean))

    elif clean == "can you learn":
        print("Cindy:", responses.get(clean))

    elif clean == "do you like humans":
        print("Cindy:", responses.get(clean))

    elif clean == "can you dance":
        print("Cindy:", responses.get(clean))

    elif clean == "sing a song":
        print("Cindy:", responses.get(clean))

    elif clean == "what is ai":
        print("Cindy:", responses.get(clean))

    elif clean == "what is python":
        print("Cindy:", responses.get(clean))

    elif clean == "what is a chatbot":
        print("Cindy:", responses.get(clean))

    elif clean == "what is machine learning":
        print("Cindy:", responses.get(clean))

    elif clean == "what is coding":
        print("Cindy:", responses.get(clean))

    elif clean == "what is data science":
        print("Cindy:", responses.get(clean))

    elif clean == "what is cybersecurity":
        print("Cindy:", responses.get(clean))

    elif clean == "what is cloud computing":
        print("Cindy:", responses.get(clean))

    elif clean == "tell me a joke":
        print("Cindy:", responses.get(clean))

    elif clean == "tell me another joke":
        print("Cindy:", responses.get(clean))

    elif clean == "i am bored":
        print("Cindy:", responses.get(clean))

    elif clean == "motivate me":
        print("Cindy:", responses.get(clean))

    elif clean == "exam stress":
        print("Cindy:", responses.get(clean))

    elif clean == "tips for studying":
        print("Cindy:", responses.get(clean))

    elif clean == "help":
        print("Cindy:", responses.get(clean))

    else:
        print("Cindy: Hmm, I don't understand that yet!")
        print("       Try typing 'help' to see what I know 😊")