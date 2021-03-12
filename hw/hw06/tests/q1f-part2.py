test = {   'name': 'q1f-part2',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> chains_growth.labels == ('Rank', 'Restaurant', 'Sales', 'YOY_Sales', 'Segment_Category', 'Growth Category')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> chains_growth.num_rows == 250\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Making sure chains remains unchanged;\n>>> chains.labels == ('Rank', 'Restaurant', 'Sales', 'YOY_Sales', 'Segment_Category')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(chains_growth.column('Growth Category').take(np.arange(10)) == np.array(['steady increase', 'steady increase', 'rapid increase',\n"
                                               "...        'steady increase', 'steady increase', 'stagnant',\n"
                                               "...        'steady increase', 'steady increase', 'steady increase',\n"
                                               "...        'steady increase']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
