test = {   'name': 'q2a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> # This test makes sure that fav_emojis has exactly 5 key-value pairs.;\n>>> len(fav_emojis) == 5\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # This test makes sure that fav_emojis has the five necessary keys, and nothing else.;\n'
                                               ">>> sorted(list(fav_emojis.keys())) == ['annoyed', 'food', 'happy', 'love', 'tired']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test makes sure that all values in fav_emojis are of length 1.;\n>>> all([len(e) == 1 for e in fav_emojis.values()])\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test makes sure that all of your values are actually emojis.;\n'
                                               ">>> all_emojis = read_json('data/emojis.json');\n"
                                               '>>> \n'
                                               '>>> invalid_keys = [];\n'
                                               '>>> for k in fav_emojis.keys():\n'
                                               '...     if fav_emojis[k] not in all_emojis:\n'
                                               '...         invalid_keys.append(k);\n'
                                               '>>> \n'
                                               '>>> if len(invalid_keys) == 0:\n'
                                               "...     print('All valid')\n"
                                               '... else:\n'
                                               "...     print('The emoji(s) corresponding to the key(s) ' + str(invalid_keys)[1:-1] + ' are invalid.\\nCheck your work!')\n"
                                               'All valid\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
