movies = list()


def menu():
    user_input = input("Please enter 'a' to add a movie, enter 'l' to see the list of available movies, enter 'f' to find a movie from the list, enter 'q' to quit application: ").lower()

    while user_input != "q":
        if user_input in ['a', 'add']:
            add_movie()
        elif user_input in ['l', 'list']:
            show_movies(movies)
        elif user_input in ['f', 'find']:
            find_movie()
        else:
            print("Command was not found. Use one of the following commands: 'a', 'l', 'f', 'q'")

        user_input = input("\nPlease enter 'a' to add a movie, enter 'l' to see the list of available movies, enter 'f' to find a movie from the list, enter 'q' to quit application: ").lower()

        user_input = user_input.lower()

    if user_input == "q":
        print("Thank you for using app. Quiting program...")


def add_movie():
    title = input("Please give us title of the movie: ")
    director = input("Please give us who was the director of the movie: ")
    genre = input("Please give us genre of the movie: ").lower()
    year= int(input("Please give us the year in which movie was produced (only numbers are accepted): "))
    movie = {
        'title': title,
        'director': director,
        'genre': genre,
        'year': year
    }
    movies.append(movie)
    print(f"The following movie '{movie['title']}' was added to your movies list.")


def show_movies(movies_list):
    if not movies_list:
        print('There are no movies in the list :(')
    else:
        for i, movie in enumerate(movies_list):
            print(f"\n{i+1} - title: {movie['title']}, director: {movie['director']}, year: {movie['year']};")


def find_movie():
    find_by = input("What property of the movie are you looking for (title, director, year, genre)? ").lower()
    looking_for = input("What are you searching for? ")

    if find_by == 'year' and looking_for.isdigit():
        looking_for = int(looking_for)

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    if not found_movies:
        print('There are no movies in the list :(')
    else:
        show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = list()

    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found


if __name__ == '__main__':
    menu()

