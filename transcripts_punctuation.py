import os
from pathlib import Path

'''
This script takes a folder (make sure to change transcript_dir folder name) 
containing .txt transcript files that are typically very long and do not contain 
any periods to separate the file into any sort of sentence structure. This script 
guesses at a reasonable sentence structure by adding periods before the word "I" 
which seems to do a reasonable job creating logical sentence structure. It is 
then more suitable for use with embeddings.
'''

def structure_transcripts():

    # creates an absolute file path to necessary file dirs
    BASE_PATH = Path(__file__).resolve().parent

    transcript_dir = BASE_PATH / 'transcripts/' # <- change folder name as needed
    destination_dir = BASE_PATH / 'Edited/' # <- dir to put new files in

    #iterate over the files in the starting directory
    for filename in os.listdir(transcript_dir):
        if filename.endswith(".txt"):
            # read the txt file
            with open(os.path.join(transcript_dir,filename), "r") as file:
                text = file.read()
            
            # split the text into a list of words
            words = text.split()

            # creating a list of words that typically mark the start of a new sentence
            filter_words = ["I","We","we","these","These","Here","here","There","there","I'll","i","i'll"]
            # iterate through the list of words
            for i in range(len(words) -1):
                if words[i] in filter_words and words[i-1]: ###### hoping this selects previous word #####
                    #add a period to the preceding words end
                    words[i-1] += "."
            
            # join the modified list of words back into a single string
            modified_text = " ".join(words)     ##### may want to add a newline ####
            
            #write the modified string to a new .md file
            new_filename = os.path.splitext(filename)[0] + ".md"

            #write the modified string back to the text file (as a .md file in this case)
            with open(os.path.join(destination_dir,new_filename), "w") as file:
                file.write(modified_text)
            
if __name__ == '__main__':
    structure_transcripts()
