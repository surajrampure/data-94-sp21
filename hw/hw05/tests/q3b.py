test = {   'name': 'q3b',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> feeders.num_rows == 14\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> feeders.labels == ('Name', 'Region', 'Applied', 'Admitted', 'Enrolled')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(feeders.column('Enrolled') == np.array([64, 47, 39, 38, 30, 28, 27, 26, 26, 25, 25, 23, 23, 22]))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(sorted(feeders.column('Name')) == ['AMADOR VALLEY HIGH SCHOOL',\n"
                                               "...  'AMERICAN HIGH SCHOOL',\n"
                                               "...  'CANYON CREST ACADEMY',\n"
                                               "...  'DOUGHERTY VALLEY HIGH SCHOOL',\n"
                                               "...  'DUBLIN HIGH SCHOOL',\n"
                                               "...  'FOOTHILL HIGH SCHOOL',\n"
                                               "...  'IRVINGTON HIGH SCHOOL',\n"
                                               "...  'JAMES LOGAN HIGH SCHOOL',\n"
                                               "...  'LOWELL HIGH SCHOOL',\n"
                                               "...  'MISSION SAN JOSE HIGH SCHOOL',\n"
                                               "...  'PALISADES CHARTER HIGH SCHOOL',\n"
                                               "...  'PORTOLA HIGH SCHOOL',\n"
                                               "...  'UNIVERSITY HIGH SCHOOL',\n"
                                               "...  'WOODBRIDGE HIGH SCHOOL'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
