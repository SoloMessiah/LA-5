"""
Our program is trying to translate a sentence captured as user input.
We will first read the file textese.txt.
Then, from the file we just read, we will create a list of strings from each line in the text file.
Afterwards, we will create a dictionary from the list.
Next the text file has been read into memory, we can close the file.

We will then define a function for translation.
This involves splitting the user input, sentences, into an array of strings.
We can use "Enjoy the excellent band tonight" as a test subject.
The array will consist of "Enjoy", "the", "excellent", "band", "tonight".

Once the array of strings are complete, which represents the user's input sentence, we will loop through
each words, look for the matching keyword, and return back the value that is associated to that keyword.

Print out the translated sentence after each translation.
"""




"""
main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    words = for each word in the sentence
    for each words, translate word
    print translated sentence

create_dictionary():
    read textese.txt
    create list = each line from textese.txt
    close file
    create dictionary from list
    return dictionary

main()
"""




def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence,dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()


    translation = {}
    for word in words:
        [k, v] = word.split(",")
        translation[k] = v
    
    return translation
    

def translate(sentence, dictionary):
    words = sentence.split()
    
    for word in words:
        print(dictionary.get(word, word), " ", end="")

main()
    
    