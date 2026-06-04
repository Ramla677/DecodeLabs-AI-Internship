print("=" * 50)
print("🎬 AI MOVIE RECOMMENDATION SYSTEM 🎬")
print("=" * 50)

# Movie database
movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr Bean", "The Mask", "Friends"],
    "horror": ["Conjuring", "Insidious", "Annabelle"],
    "romance": ["Titanic", "Notebook", "La La Land"],
    "sci-fi": ["Interstellar", "Inception", "Avatar"]
}

# Take user input
user_choice = input(
    "\nChoose a genre (action/comedy/horror/romance/sci-fi): "
).lower()

# Recommendation logic
if user_choice in movies:
    print("\n🤖 Recommended Movies For You:\n")

    for movie in movies[user_choice]:
        print("🎥", movie)

else:
    print("\n❌ Sorry! Genre not found.")