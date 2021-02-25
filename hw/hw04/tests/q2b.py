test = {   'name': 'q2b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> # This test checks the first example in question description.;\n'
                                               ">>> convert_1 = emojify('Filing taxes makes me tired and want food.').split(' ');\n"
                                               '>>> e1_1, e1_2 = convert_1[4], convert_1[-1][:-1];\n'
                                               ">>> (e1_1 == fav_emojis['tired']) and (e1_2 == fav_emojis['food'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test checks the second example in question description.;\n'
                                               ">>> convert_2 = emojify('I LOVE love life right now. I am so happy – why do you look so annoyed?!').split(' ');\n"
                                               '>>> e2_1, e2_2, e2_3, e2_4 = convert_2[1], convert_2[2], convert_2[9], convert_2[-1][:-2];\n'
                                               ">>> (e2_1 == fav_emojis['love']) and (e2_2 == fav_emojis['love']) and (e2_3 == fav_emojis['happy']) and (e2_4 == fav_emojis['annoyed'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test checks the third example in question description.;\n'
                                               '>>> convert_3 = emojify("It\'s not you, it\'s me... I don\'t make you haPPy, I make you tired.").split(\' \');\n'
                                               '>>> e3_1, e3_2 = convert_3[9][:-1], convert_3[-1][:-1];\n'
                                               ">>> (e3_1 == fav_emojis['happy']) and (e3_2 == fav_emojis['tired'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test checks a new fourth example.;\n'
                                               ">>> convert_4 = emojify('Billy is lovesick, and not the kind that can be solved with food – Billy is annoyed, really.').split(' ');\n"
                                               '>>> e4_1, e4_2, e4_3 = convert_4[2][0], convert_4[12], convert_4[-2][0];\n'
                                               ">>> (e4_1 == fav_emojis['love']) and (e4_2 == fav_emojis['food']) and (e4_3 == fav_emojis['annoyed'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
