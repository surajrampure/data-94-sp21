test = {   'name': 'q4c',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> top_lac_schools.labels == ('Name', 'City', 'Region', 'Applied', 'Admitted', 'Enrolled', 'Acceptance Rate')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> top_lac_schools.num_rows == 10\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(sorted(top_lac_schools.column('Name')) == sorted(np.array(['PALISADES CHARTER HIGH SCHOOL', 'ARCADIA HIGH SCHOOL', 'DIAMOND BAR HIGH "
                                               "SCHOOL', 'GRETCHEN WHITNEY HIGH SCHOOL', 'SANTA MONICA HIGH SCHOOL', 'GRANADA HILLS CHARTER HIGH SCH', 'PALOS VERDES PENINSULA HS', 'VAN NUYS HIGH "
                                               "SCHOOL', 'WALNUT HIGH SCHOOL', 'SOUTH PASADENA HIGH SCHOOL'])))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(np.isclose(sorted(top_lac_schools.column('Acceptance Rate')), sorted(np.array([0.2081448 , 0.22088353, 0.14772727, 0.24418605, 0.19487179, "
                                               '0.18584071, 0.19565217, 0.31818182, 0.20710059, 0.23469388]))))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
