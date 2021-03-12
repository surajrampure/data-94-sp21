test = {   'name': 'q2b',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> future_with_city.labels == ('Rank', 'Restaurant', 'City', 'Sales', 'YOY_Sales')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> future_with_city.num_rows == future.num_rows\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(future_with_city.column('City').take(np.arange(6)) == np.array(['Seattle', 'Charlotte', 'Huntington Beach', 'Wilmington', 'Irvine',\n"
                                               "...        'Belmar']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
