test = {   'name': 'q3a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> ratings.num_rows == 91 and ratings.labels == ('Restaurant', 'City', 'Rating')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(ratings.column('Rating').take(np.arange(5)) == np.array([3.5, 4, 4, 4, 3.5]))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
