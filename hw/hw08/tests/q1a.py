test = {   'name': 'q1a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> sfo_three_pivoted.num_rows == 84\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> sfo_three_pivoted.num_columns == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> list(sfo_three_pivoted.row(10)) == ['2014-11', 234979, 222279, 1359374]\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(sfo_three_pivoted.column(2).take(np.arange(10)) == np.array([184953, 173069, 228384, 231490, 256089, 298283, 320947, 321517,\n'
                                               '...        251187, 265072]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
