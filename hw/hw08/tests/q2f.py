test = {   'name': 'q2f',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> dest_with_delay.labels == ('Destination', 'Number of Flights', 'Number of Delayed Flights')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> dest_with_delay.num_rows == 62\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> list(dest_with_delay.row(44)) == ['ORD', 4003, 1832]\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(dest_with_delay.column('Number of Delayed Flights').take(np.arange(15, 20)) == np.array([1374, 236, 138, 192, 2081]))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
