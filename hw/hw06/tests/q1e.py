test = {   'name': 'q1e',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> top_selling_segments.labels == ('Segment_Category', 'Average Sales') and top_selling_segments.num_rows == 7\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(top_selling_segments.column('Segment_Category') == np.array(['Quick Service & Coffee Cafe', 'Quick Service & Burger',\n"
                                               "...        'Quick Service & Mexican', 'Fast Casual & Bakery Cafe',\n"
                                               "...        'Quick Service & Chicken', 'Quick Service & Sandwich',\n"
                                               "...        'Quick Service & Pizza']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(np.isclose(top_selling_segments.column('Average Sales'), np.array([7972.25      , 6106.46153846, 6071.5       , 5890.        ,\n"
                                               '...        3769.83333333, 3741.25      , 2664.5       ])))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
