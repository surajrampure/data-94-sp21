test = {   'name': 'q3c',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> schools_stats_acc.labels == ('Name', 'Region', 'Applied', 'Admitted', 'Enrolled', 'Acceptance Rate')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> schools_stats.num_rows == 659\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Making sure schools_stats didn't change;\n>>> schools_stats.labels == ('Name', 'Region', 'Applied', 'Admitted', 'Enrolled')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(np.isclose(schools_stats_acc.column('Acceptance Rate').take(np.arange(10)), np.array([0.35294118, 0.19811321, 0.20833333, 0.33333333, "
                                               '0.42105263, 0.21538462, 0.15730337, 0.16666667, 0.18292683, 0.14285714])))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
