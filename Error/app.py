prompt = "\nEnter 'a' to add. Enter 's' to show. Enter 'f' to find."
movies = []


def add():
    title = input("enter title")
    director = input("enter director")
    year = input("enter year")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find():
    find = input("What is title of movie?")
    for movie in movies:
        if find == movie['title']:
            print_movie(movie)

user_options = {
    'a': add,
    'f': find,
    's': show,
}


def menu():
    selection = input(prompt)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("wrong")
        selection = input(prompt)


menu()