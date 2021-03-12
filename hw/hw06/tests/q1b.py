test = {   'name': 'q1b',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> segment_counts.labels == ('Segment_Category', 'count')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> segment_counts.num_rows == 48\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(segment_counts.column('count') == np.array([22, 14, 13, 10, 10, 10,  9,  9,  9,  8,  8,  8,  7,  7,  7,  7,  6,\n"
                                               '...         6,  6,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  3,  3,  3,  3,  3,\n'
                                               '...         2,  2,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(segment_counts.column('Segment_Category').take(np.arange(3)) == np.array(['Varied Menu', 'Mexican', 'Quick Service & Burger']))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
