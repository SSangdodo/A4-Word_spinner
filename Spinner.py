from random import *
def make_list_from_file(filename):
    file_content = open(filename,"r")
    returning_list = []
    for lines in file_content:
        returning_list.append(lines.strip("\n").strip(" "))
    return returning_list

def make_response_dictionary(response_list):
    keyword_and_response = {}
    for items in response_list:
        keyword,synonyms = items.split(":")
        keyword_and_response[keyword] = synonyms.split(",")
    return keyword_and_response
class Spinner():
    def __init__(self,file_words):
            self.file_words_list = file_words
            self.synonyms_data = make_response_dictionary(make_list_from_file("synonyms-simplified.txt"))
    def convert_synonyms(self):
        returning_list = []
        for words in self.file_words_list:
            # print(words,self.synonyms_data.get(words,1))
            if self.synonyms_data.get(str(words),1) != 1 and randint(1,2) == 2:
                returning_list.append(self.synonyms_data[str(words)][randint(0,len(self.synonyms_data[words])-1)])
            else:
                returning_list.append(words)

        return " ".join(returning_list)