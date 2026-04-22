import random

# Simple movie database with genres/moods
movies = {
    "action": [
        "Die Hard",
        "Mad Max: Fury Road",
        "John Wick",
        "The Dark Knight",
        "Avengers: Endgame"
    ],
    "comedy": [
        "The Hangover",
        "Superbad",
        "Groundhog Day",
        "The Grand Budapest Hotel",
        "Shaun of the Dead"
    ],
    "drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "Titanic",
        "The Godfather",
        "Pulp Fiction"
    ],
    "horror": [
        "The Conjuring",
        "Get Out",
        "Hereditary",
        "The Shining",
        "It"
    ],
    "romance": [
        "La La Land",
        "The Notebook",
        "Pride and Prejudice",
        "Crazy Rich Asians",
        "To All the Boys I've Loved Before"
    ],
    "sad": [
        "The Pursuit of Happyness",
        "Schindler's List",
        "Grave of the Fireflies",
        "Manchester by the Sea",
        "The Fault in Our Stars"
    ],
    "happy": [
        "Up",
        "Inside Out",
        "Toy Story",
        "Finding Nemo",
        "Moana"
    ],
    "thriller": [
        "Inception",
        "Parasite",
        "Gone Girl",
        "The Silence of the Lambs",
        "Fight Club"
    ],
    "sci-fi": [
        "Interstellar",
        "Blade Runner 2049",
        "The Matrix",
        "Arrival",
        "Dune"
    ],
    "fantasy": [
        "The Lord of the Rings: The Fellowship of the Ring",
        "Harry Potter and the Sorcerer's Stone",
        "The Chronicles of Narnia",
        "Pan's Labyrinth",
        "Stardust"
    ]
}

def recommend_movies(mood, num_recommendations=3):
    """
    Recommend movies based on user's mood/genre preference.
    This is a simple content-based filtering approach.
    """
    mood = mood.lower().strip()
    if mood in movies:
        available_movies = movies[mood]
        if len(available_movies) <= num_recommendations:
            return available_movies
        else:
            return random.sample(available_movies, num_recommendations)
    else:
        return ["Sorry, I don't have recommendations for that mood. Try: action, comedy, drama, horror, romance, sad, happy, thriller, sci-fi, fantasy."]

def main():
    print("Welcome to the Simple Movie Recommendation System!")
    print("I can recommend movies based on your current mood or preferred genre.")
    print("Available moods/genres: action, comedy, drama, horror, romance, sad, happy, thriller, sci-fi, fantasy")
    print()

    while True:
        user_mood = input("What mood are you in or what genre do you prefer? (or type 'exit' to quit): ").strip()
        if user_mood.lower() == 'exit':
            print("Goodbye! Enjoy your movies!")
            break

        recommendations = recommend_movies(user_mood)
        if isinstance(recommendations, list) and len(recommendations) > 0:
            print(f"Based on your mood '{user_mood}', I recommend:")
            for movie in recommendations:
                print(f"- {movie}")
        else:
            print(recommendations[0])  # Error message
        print()

if __name__ == "__main__":
    main()
