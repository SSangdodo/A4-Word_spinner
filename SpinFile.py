from Spinner import *
import string
def make_list_from_file(filename):
    file_content = open(filename,"r")
    returning_list = []

    for lines in file_content:
        for words in lines.lower().translate(str.maketrans('', '', string.punctuation)).lower().split():
            #for the words in the original file, remove punctuation and lower it.
            returning_list.append(words)
            #update the list with the converted words

    file_content.close()
    return returning_list
def main():
    words = make_list_from_file("essay.txt")
    spinned = Spinner(words)
    #make a class using modified words
    print("Original : " + " ".join(words))
    #from the words of the original file, make them into a one full string
    for option_counter in range(1,4):
        #for 1~3
        print("Option " + str(option_counter) +" : " + spinned.convert_synonyms())
        #print 3 sequences of words converted om Spinner.py

if __name__ == '__main__':
    main()