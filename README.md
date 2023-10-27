# Transcript_processing
processes a folder of .txt transcript files and attempts to add punctuation sentence structure &amp; then saves as a .md file

This script takes a folder (make sure to change transcript_dir folder name) 
containing .txt transcript files that are typically very long and do not contain 
any periods to separate the file into any sort of sentence structure. This script 
guesses at a reasonable sentence structure by adding periods before the word "I" 
which seems to do a reasonable job creating logical sentence structure. It is 
then perhaps a bit more suitable for use with embeddings.
