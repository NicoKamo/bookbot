def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def words_in_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words_num = len(file_contents.split())
    return words_num

def get_character_count(text):
    count_dict = {}
    for string in text:
        if count_dict.get(string.lower()) == None:
            count_dict[string.lower()] = 1
        else:
            count_dict[string.lower()] += 1
    return count_dict

def sort_dict(count_dict):
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1],reverse=True))
    return sorted_dict