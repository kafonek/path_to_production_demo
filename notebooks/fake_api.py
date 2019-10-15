def search_restaurants():
    "Simulate an API call that returns yelp-like restaurant info"
    restaurants = {'Pizza place' : {'price' : 2,
                                    'rating' : 3,
                                    'nratings' : 27},

                   'Greek place' : {'price' : 1,
                                    'rating' : 2,
                                    'nratings' : 5},

                   'Sushi place' : {'price' : 4,
                                    'rating' : 3,
                                    'nratings' : 55},

                   'Thai place' : {'price' : 3,
                                   'rating' : 1,
                                   'nratings' : 8},

                   'Tapa place' : {'price' : 4,
                                   'rating' : 5,
                                   'nratings' : 9},

                      }
    return restaurants

def visited_restaurants():
    "Simulate a database call to return restaurants we already tried"
    history = {'Pizza place' : ['2019-10-02', '2019-10-09'],
               'Sushi place' : ['2019-10-03'],
               'Tapa place' : ['2019-10-10']}
    return history
