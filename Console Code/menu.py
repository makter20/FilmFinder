import movie
import rating

def print_menu():
    menu_option={
        1: 'Find Movies by ID', 
        2: 'Find Movies by Title',
        3: 'Find Movies by Genre.', 
        4: 'Find Movies by Year', 
        5: 'Find Movies by User Id', 
        6: 'Insert a Movie', 
        7: 'Find Highly Rated Movies', 
        8: 'Find Lowly Rated Movies',
        9: 'Find Movies by Rating',
        10: 'Find Rating by movie ID and date range',
        11: 'Delete a rating',
        12: 'Put a rating',
        13: 'Exit'
        }
    for key, value in menu_option.items():
        print(key,".", value)

def menu(db):
    print_menu()
    option = int(input('Enter your choice: '))
    print("Entered Option: ", option)
    if option==1:
        value = int(input('Enter movie id: '))
        cursor = movie.getMoviesbyID(db, value)
        printCursor(cursor)

    if option==2:
        value = str(input('Enter movie title: '))
        limitValue = int(input('Enter limit: '))
        cursor = movie.getMoviesbyTitle(db, value, limitValue)
        printCursor(cursor)

    if option==3:
        value = str(input('Enter movie genre: '))
        limitValue = int(input('Enter limit: '))
        cursor = movie.getMoviesbyGenre(db, value, limitValue)
        printCursor(cursor)

    if option==4:
        value = str(input('Enter year: '))
        limitValue = int(input('Enter limit: '))
        cursor = movie.getMoviesbyYear(db, value, limitValue)
        printCursor(cursor)

    if option==5:
        value = int(input('Enter User ID: '))
        limitValue = int(input('Enter limit: '))
        cursor = movie.getMoviesbyUserId(db, value, limitValue)
        printCursor(cursor)

    if option==6:
        titleValue = str(input('Enter Movie title (Please use "Title (Year)"): '))
        genreValue = str(input('Enter Movie Genres (Please use "Genre1, Genre2"): '))
        cursor = movie.addMovie(db, titleValue, genreValue)
        printCursor(cursor)

    if option==7:
        limitValue = int(input('Enter limit: '))
        cursor = movie.getHighlyRatedMovies(db, limitValue)
        printCursor(cursor)

    if option==8:
        limitValue = int(input('Enter limit: '))
        cursor = movie.getLowlyRatedMovies(db, limitValue)
        printCursor(cursor)

    if option==9:
        value = int(input('Enter Rating: '))
        limitValue = int(input('Enter limit: '))
        cursor = movie.getMoviesbyRating(db, value, limitValue)
        printCursor(cursor)

    if option==10:
        movieId = int(input('Enter a movieId: '))
        startTime = int(input('Enter starting datetime: '))
        endTime = int(input('Enter ending datetime: '))
        limitValue = int(input('Enter limit: '))
        cursor = rating.getRating(db, movieId, startTime, endTime, limitValue)
        printCursor(cursor)

    if option==11:
        userId = int(input('Enter a userId: '))
        movieId = int(input('Enter a movieId: '))
        cursor = rating.delRating(db, userId, movieId)
        printCursor(cursor)

    if option==12:
        userId = int(input('Enter a userId: '))
        movieId = int(input('Enter a movieId: '))
        ratingIn = int(input('Enter a rating: '))
        timestamp = int(input('Enter a timestamp: '))
        cursor = rating.putRating(db, userId, movieId, ratingIn, timestamp)
        printCursor(cursor)

    if option==13:
        print("Exiting menu.....")

def printCursor(cursor):
    print("============================================================================")
    for record in cursor:
        print(record)
    print("============================================================================")
    
