def get_word_count(file_string):
    return (len(file_string.split()))

def get_char_count(file_string):
    words = file_string.split()
    char_count = {}
    for word in words:
        for c in word.lower():
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    return char_count


def sort_on(items):
    return items["quant"]

def dict_to_list(dic_char):
    char_list = []
    for c in dic_char:
        char_list.append({"letter": c, "quant":dic_char[c]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list