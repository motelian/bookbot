from telnetlib import DO
def get_num_words(text):
    return len(text.split())

def get_char_dict(text):
    char_dict = {}
    for c in text:
        char = c.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict_list(char_dict):
    return sorted(char_dict.items(), key = lambda x: x[1], reverse = True)
