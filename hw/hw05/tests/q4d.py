test = {   'name': 'q4d',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> big_alameda.labels == ('Name', 'City', 'Region', 'Applied', 'Admitted', 'Enrolled', 'Acceptance Rate')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> big_alameda.num_rows == 7\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(big_alameda.column('Name') == np.array(['AMADOR VALLEY HIGH SCHOOL', 'AMERICAN HIGH SCHOOL', 'DUBLIN HIGH SCHOOL', 'FOOTHILL HIGH SCHOOL', "
                                               "'IRVINGTON HIGH SCHOOL', 'JAMES LOGAN HIGH SCHOOL', 'MISSION SAN JOSE HIGH SCHOOL']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> np.all(big_alameda.column('Enrolled') == np.array([23, 25, 26, 27, 47, 25, 28]))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
