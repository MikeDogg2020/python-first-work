# def display_message():
#     """ Display the learning criteria. """
#     print("Hello class, today's lesson we will go over what it means to be black in America.")

# display_message()


# def favorite_book(title):
#     """ Display your favorite book. """
#     print("One of my favorite books is " + title.title() + ".")

# favorite_book('harry potter and the chamber of secrets')


# def make_shirt(shirt_text, shirt_size='large'):
#     """Display a message on the shirt."""
#     print("\nI have a " + shirt_size + " shirt.")
#     print("The " + shirt_size + " shirt reads " + shirt_text.title() + ".")

# make_shirt('large', 'a humble individual')
# make_shirt(shirt_size='large', shirt_text='a humble individual')

# make_shirt('i love python')
# make_shirt(shirt_size='medium', shirt_text='i love python')
# make_shirt(shirt_size='small', shirt_text='humble introvert')
# make_shirt(shirt_size='xxlarge', shirt_text='understand humility')


# def describe_city(city_name, country='usa'):
#     """Display the city and the country it resides."""
#     print(city_name.title() + " is in " + country.title() + ".")

# describe_city('atlanta')
# describe_city('los angeles')
# describe_city(city_name='accra', country='ghana')


# def city_country(city, country):
#     """Display the city with its corresponding country."""
#     print(city.title() + ", " + country.title())

# city_country('rabat', 'morocco')
# city_country('abuja', 'nigeria')
# city_country('colombo', 'sri lanka')


# def make_album(artist_name, album_title, tracks=''):
#     """Return a dictionary of information about a music album."""
#     album = {'name': artist_name, 'album': album_title}
#     if tracks:
#         album['tracks'] = tracks
#     return album

# music_album = make_album('jay-z', 'reasonable doubt', tracks=15)
# music_album_1 = make_album('kendrick lamar', 'good kid, m.A.A.d city', tracks=18)
# music_album_2 = make_album('kanye west', 'graduation', tracks=14)
# print(music_album)
# print(music_album_1)
# print(music_album_2)


# def make_album(artist_name, album_title):
#     """Return a dictionary of information about a music album."""
#     album = {'name': artist_name, 'album': album_title}
#     return album

# while True:
#     print("\nGive me some information about the album.")
#     print("(enter 'q' at any time to quit.)")

#     a_name = input("Artist name: ")
#     if a_name == 'q':
#         break

#     a_title = input("Album title: ")
#     if a_title == 'q':
#         break

#     album_info = make_album(a_name.title(), a_title.title())
#     print(album_info)


# def show_magicians(names):

#     for name in names:
#         message = "Hello, " + name.title() + "!"
#         print(message)

# magician_names = ['harry', 'oscar', 'adam', 'houdini']
# show_magicians(magician_names)


# def show_magicians(magician_names, original_names):

#     while magician_names:
#         current_names = magician_names.pop()
#         message = "Hello, " + current_names.title() + "!"
#         print(message)
#         original_names.append(current_names)

# def make_great(original_names):
        
#       for original_name in original_names:
#         phrase = str(original_name.title()) + " the Great!"
#         print(phrase)

# magician_names = ['harry', 'oscar', 'adam', 'houdini']
# original_names = []

# show_magicians(magician_names[:], original_names)
# make_great(original_names)


# def make_sandwich(*toppings):
#     """Print out a list of toppings you want on your sandwich."""
#     print("\nMaking a sandwich with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)

# make_sandwich('lettuce', 'tomatoes', 'onions')
# make_sandwich('cheese', 'lettuce', 'pickles')
# make_sandwich('lettuce', 'tomato', 'pickles', 'banana peppers', 'black olives')


def build_profile(first, last, **user_info):        
    """Build a dictionary containing everything we know about a user."""
    profile = {}        
    profile['first_name'] = first       
    profile['last_name'] = last
    for key, value in user_info.items():       
        profile[key] = value
    return profile      

user_profile = build_profile('mike', 'patrick', birthplace='atlanta', age=31, occupation='student')      
print(user_profile)


def make_car(manufacturer, model_name, **car_info):
    """Build a dictionary that explains what we know about the car."""
    car_profile = {}
    car_profile['make'] = manufacturer
    car_profile['model'] = model_name
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car = make_car('subaru', 'outback', color='maroon', warranty=True)
print(car)