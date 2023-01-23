book_path = "books/frankenstein.txt"

def main():
    text = get_words(book_path)
    count = count_words(text)
    letters = count_letters(text)
    list_of_char = make_list(letters)
    
        
    print(f"--- Begin report of {book_path}  ---")
    print(f"{count} words found in the document")
    print()
    for item in list_of_char:
        if not item["char"].isalpha(): #if "char" item isn't alphabet then continues loop. if alphabet then prints values
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")


def sort_on(d): # extra sort element, sorts the highest num
    return d["num"]

def make_list(dicto):
    list1 = []
    for k in dicto:
        list1.append({"char": k, "num": dicto[k]}) #append to list with "char": a, "num": count from dictionary / "char": a, "num": 26743,
    list1.sort(reverse=True, key=sort_on) #adds sorting func sort_on, sorts high to low if True or low to High if False
    return list1

def count_letters(all_words):
    dict2 = {}
    for i in all_words:
        lowered = i.lower()
        if lowered in dict2:
            dict2[lowered] += 1
        else:
            dict2[lowered] = 1
    return dict2


def count_words(full_text):
    words = full_text.split()
    return len(words)

def get_words(path):
    with open(book_path) as f:
        return f.read()


main()   
