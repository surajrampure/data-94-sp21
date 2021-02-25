test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # If you fail this test, either you didn't correctly set the key 'explicit';\n"
                                               ">>> # or you may have accidentally used the variable name 'dict' somewhere, which you should not have.;\n"
                                               ">>> # If it's the latter, change that variable name, restart your notebook, and run all cells until this point.;\n"
                                               ">>> type(even_more_slang['explicit']) == dict\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test makes sure more_slang has the correct six keys.;\n'
                                               ">>> # 'lmao' and 'fml' should not be keys of more_slang: they should be keys of more_slang['explicit'].;\n"
                                               ">>> sorted(even_more_slang.keys()) == ['GOAT', 'explicit', 'haha', 'lol', 'ofr', 'smh']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # This test ensures that more_slang['explicit']['lmao'] is a string with four words;\n"
                                               ">>> # and whose first word starts with 'l', second word starts with 'm', third word starts with 'a', and fourth starts with 'o'.;\n"
                                               ">>> lmao_word = even_more_slang['explicit']['lmao'].split(' ');\n"
                                               ">>> (lmao_word[0][0] == 'l') and (lmao_word[1][0] == 'm') and (lmao_word[2][0] == 'a') and (lmao_word[3][0] == 'o') and (len(lmao_word) == 4)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # This test ensures that more_slang['explicit']['fml'] is a string with three words;\n"
                                               ">>> # and whose first word starts with 'f', second word starts with 'm', and third word starts with 'l'.;\n"
                                               ">>> fml_word = even_more_slang['explicit']['fml'].split(' ');\n"
                                               ">>> (fml_word[0][0] == 'f') and (fml_word[1][0] == 'm') and (fml_word[2][0] == 'l') and (len(fml_word) == 3)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
