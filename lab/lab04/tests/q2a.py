test = {   'name': 'q2a',
    'points': 0,
    'suites': [   {   'cases': [   {   'code': '>>> login("data94admin", "12345", True) == "New account"\nAccount with username: data94admin created with password: 12345\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> login("data94admin", "12345") == "Successful login"\nSuccessfully logged in as user: data94admin\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> login("data94admin", "123456") == "No successful login"\nIncorrect password, please try again\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> login("data94admin", "better_password", True) == "No new account"\nUsername already exists, please select another username\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
