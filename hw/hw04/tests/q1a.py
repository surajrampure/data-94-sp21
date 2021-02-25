test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # This test ensures you added the right key ('ofr') and nothing else.;\n"
                                               ">>> sorted(more_slang.keys()) == ['GOAT', 'haha', 'lol', 'ofr', 'smh']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test ensures that you added a value with three words;\n'
                                               ">>> # and whose first word starts with 'o', second word starts with 'f', and third word starts with 'r'.;\n"
                                               ">>> new_abb = more_slang['ofr'].split(' ');\n"
                                               ">>> (new_abb[0][0] == 'o') and (new_abb[1][0] == 'f') and (new_abb[2][0] == 'r') and (len(new_abb) == 3)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
