test = {   'name': 'q2c',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> destinations.labels == ('Destination', 'count', 'name', 'latitude_deg', 'longitude_deg')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> destinations.num_rows == 62\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(destinations.column('name').take(np.arange(25, 30)) == np.array(['Daniel K Inouye International Airport',\n"
                                               "...        'Washington Dulles International Airport',\n"
                                               "...        'George Bush Intercontinental Houston Airport',\n"
                                               "...        'Indianapolis International Airport', 'Jackson Hole Airport']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> list(destinations.row(18)) == ['EUG', 520, 'Mahlon Sweet Field', 44.12459945678711, -123.21199798583984]\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
