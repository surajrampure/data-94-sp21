test = {   'name': 'q4e',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> bay_schools.labels == ('Name',\n...  'City',\n...  'Region',\n...  'Applied',\n...  'Admitted',\n...  'Enrolled',\n...  'Acceptance Rate')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bay_schools.num_rows == 190\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(bay_schools.column('Name').take(np.arange(50, 55)) == np.array(['EMERY SECONDARY SCHOOL', 'ENCINAL HIGH SCHOOL', 'ENVISION ACAD "
                                               "ARTS/TECHNOLOGY', 'EVEREST PUBLIC HIGH SCHOOL', 'EVERGREEN VALLEY HIGH SCHOOL']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> np.all(bay_schools.column('Enrolled').take(np.arange(30, 35)) == np.array([19,  5,  3,  8, 11]))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bay_acc_rate < 0.2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(bay_acc_rate, 0.18745785)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
