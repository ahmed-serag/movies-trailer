'''
Created on Feb 25, 2017

@author: Ahmed Serag
'''
from movie import Movie
import fresh_tomatoes
if __name__ == '__main__':
    
    #creating some movies objects
    hacksaw_ridge = Movie('hacksaw ridge',
                        'http://t1.gstatic.com/images?q=tbn:ANd9GcQkB0TuKruaG_PylU3qlUC2BkFKj3R4aUgN2MMDkc7hmSXrPTsy',
                        'https://youtu.be/s2-1hz1juBI')
    Split = Movie('Split',
                'http://t0.gstatic.com/images?q=tbn:ANd9GcQxZKPueKzPFNEc1Un4x2TecYop4yrTVArVtfgrNzktMqbfehfv',
                'https://youtu.be/84TouqfIsiI')
    Room = Movie('Room',
                'http://t1.gstatic.com/images?q=tbn:ANd9GcSu9dR_6oOzsDvAq76vlBqPsyYNHdLw3jRRrmJVb7EBPTQBryV1',
                'https://youtu.be/E_Ci-pAL4eE')
    
    
    '''
    put movies objects into an array of movies
    and sending it to function open_movies_page
    in module fresh_tomatoes to display it in the html page
    '''
    movies = [hacksaw_ridge, Split, Room]
    fresh_tomatoes.open_movies_page(movies)