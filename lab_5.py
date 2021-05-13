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