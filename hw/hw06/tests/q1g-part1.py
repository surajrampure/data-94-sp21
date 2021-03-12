test = {   'name': 'q1g-part1',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> common_chains.num_rows == 79\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> common_chains.labels == chains_growth.labels\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(common_chains.column(\'Restaurant\').take(np.arange(5)) == np.array(["McDonald\'s", \'Burger King\', "Wendy\'s", \'Sonic Drive-In\',\n'
                                               "...        'Jack in the Box']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> 'Chipotle Mexican Grill' not in common_chains.column('Restaurant')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
