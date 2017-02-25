'''
Created on Feb 25, 2017

@author: Ahmed Serag
'''

class Movie():
    '''
    this class contains movie information including
    movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.
    '''


    def __init__(self, title, poster_url, trailer_url):
        '''
        Constructor
        '''
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        
        