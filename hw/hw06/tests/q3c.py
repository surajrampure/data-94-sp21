test = {   'name': 'q3c',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> independents_with_ratings.num_rows == 91\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> independents_with_ratings.labels == ('Rank', 'Restaurant', 'Sales', 'Average Check', 'City', 'State', 'Meals Served', 'Rating')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> np.all(independents_with_ratings.column('Rating').take(np.arange(5)) == np.array([4, 4, 2.5, 3.5, 4]))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(independents_with_ratings.column(\'Restaurant\').take(np.arange(5)) == np.array(["Carmine\'s (Times Square)", \'The Boathouse Orlando\',\n'
                                               "...        'LAVO Italian Restaurant & Nightclub', 'Bryant Park Grill & Cafe',\n"
                                               "...        'Gibsons Bar & Steakhouse']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
