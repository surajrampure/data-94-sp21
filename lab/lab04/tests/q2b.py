test = {   'name': 'q2b',
    'points': 0,
    'suites': [   {   'cases': [   {   'code': '>>> login_secure("data94admin", "goodpassword", True) == "New account"\n'
                                               'Account with username: data94admin created with secure password: goodpassword\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> login_secure("data94admin", "goodpassword") == "Successful login"\nSuccessfully logged in as user: data94admin\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> login_secure("data94admin", "badpassword") == "No successful login"\nIncorrect password, please try again\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> login_secure("data94admin", "betterpassword", True) == "No new account"\nUsername already exists, please select another username\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
