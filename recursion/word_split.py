#takes in a string phrase and a set list_of_words
#function will then determine if it is possible to split the string in a way in which words can be made from the list of words

def word_split(phrase,list_of_words, output = None):

    word = ''
    count = 0

    if output is None:
        output = []

    for letter in phrase:
        word+=letter
        count+=1

        if word in list_of_words:
            output.append(word)
            return word_split(phrase[count::], list_of_words, output)

    return output
