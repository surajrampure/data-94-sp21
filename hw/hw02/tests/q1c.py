test = {   'name': 'q1c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> np.isclose(effective_tax_rate(60000), 0.149833)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(effective_tax_rate(10000), 0.10025)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(effective_tax_rate(420150), 0.22591)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # If you fail this test, make sure you address the case where if income is less than or equal to 0, you return 0!;\n'
                                               '>>> effective_tax_rate(0) == 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
