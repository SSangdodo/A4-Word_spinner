from Spinner import *
import string
def make_list_from_file(filename):
    file_content = open(filename,"r")
    returning_list = []
    for lines in file_content:
        for words in lines.lower().translate(str.maketrans('', '', string.punctuation)).lower().split():
            returning_list.append(words)
    file_content.close()
    return returning_list
def main():
    words = make_list_from_file("essay.txt")
    spinned = Spinner(words)
    print("Original : " + " ".join(words))
    for option_counter in range(1,4):
        print("Option " + str(option_counter) +" : " + spinned.convert_synonyms())

if __name__ == '__main__':
    main()