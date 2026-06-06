import random

print("=" * 55)
print("🤖 RULE-BASED CHATBOT")
print("=" * 55)

name = input("Enter your name: ")

print(f"\nHello {name}! 👋")
print("Type 'help' to see available commands.\n")

message_count = 0

fun_facts = [
    "AI stands for Artificial Intelligence.",
    "Python is one of the most popular AI languages.",
    "Machine Learning is a subset of AI.",
    "Computer Vision helps machines understand images.",
    "Chatbots are a common AI application."
]

study_tips = [
    "Practice coding daily.",
    "Use active recall while studying.",
    "Take short breaks during study sessions.",
    "Focus on understanding concepts.",
    "Revise regularly."
]

motivation_quotes = [
    "Success comes from consistent effort.",
    "Every expert was once a beginner.",
    "Keep learning and keep growing.",
    "Small progress is still progress.",
    "Believe in yourself."
]

while True:
    user = input("\nYou: ").lower().strip()
    message_count += 1

    if user in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}! 😊")

    elif user == "help":
        print("\nAvailable Commands:")
        print("hi")
        print("mood")
        print("study tip")
        print("fun fact")
        print("motivate")
        print("stats")
        print("help")
        print("exit")

    elif user == "mood":
        mood = input(
            "How are you feeling?\n"
            "(happy/sad/stressed/tired/excited): "
        ).lower()

        if mood == "happy":
            print("Bot: That's wonderful! 😄")
        elif mood == "sad":
            print("Bot: Better days are ahead. 🌈")
        elif mood == "stressed":
            print("Bot: Take things one step at a time. 🌿")
        elif mood == "tired":
            print("Bot: Make sure to get some rest. 😴")
        elif mood == "excited":
            print("Bot: That's awesome! 🎉")
        else:
            print("Bot: Thanks for sharing.")

    elif user == "study tip":
        print("Bot:", random.choice(study_tips))

    elif user == "fun fact":
        print("Bot:", random.choice(fun_facts))

    elif user == "motivate":
        print("Bot:", random.choice(motivation_quotes))

    elif user == "stats":
        print(f"Bot: Total messages exchanged: {message_count}")

    elif user in ["exit", "bye", "quit"]:
        print(f"Bot: Goodbye {name}! 👋")
        break

    else:
        print("Bot: I don't understand that command.")
        