print("=" * 60)
print("🎯 RECOMMENDATION SYSTEM")
print("=" * 60)

movies = [
    {"name": "Avengers", "action": 5, "comedy": 2, "sci_fi": 4},
    {"name": "John Wick", "action": 5, "comedy": 1, "sci_fi": 1},
    {"name": "Interstellar", "action": 2, "comedy": 1, "sci_fi": 5},
    {"name": "Inception", "action": 4, "comedy": 1, "sci_fi": 5},
    {"name": "The Mask", "action": 1, "comedy": 5, "sci_fi": 1},
    {"name": "Mr Bean", "action": 1, "comedy": 5, "sci_fi": 1}
]

print("\nRate your interests from 1 to 5")

action = int(input("Action: "))
comedy = int(input("Comedy: "))
sci_fi = int(input("Sci-Fi: "))

recommendations = []

for movie in movies:
    score = (
        action * movie["action"] +
        comedy * movie["comedy"] +
        sci_fi * movie["sci_fi"]
    )

    recommendations.append((movie["name"], score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\n🎬 Top Recommendations For You")

for i in range(3):
    print(f"{i+1}. {recommendations[i][0]}")

print("\n🤖 Recommendation Generated Successfully!")