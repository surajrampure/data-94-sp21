# If you're a student reading this – you can ignore this file, but don't change anything!
def load_clean_split(path):
    f = open(path, 'r')
    text = f.read().lower()
    characters_to_remove = ['.', ',', '!', '(', ')', ':', '"', '-', "'", ';', '\n']
    for char in characters_to_remove:
        if char == '\n':
            text = text.replace(char, ' ')
        else:
            text = text.replace(char, ' ')

    return [word for word in text.split(' ') if word != '']

def sort_by_value(d):
    sorted_keys = sorted(d, key = d.get, reverse = True)
    return sorted_keys, [d[k] for k in sorted_keys]
