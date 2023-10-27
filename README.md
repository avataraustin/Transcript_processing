# Transcript_processing
A collection of scripts to gather transcripts from a Youtube channel and processes a 
folder of .txt transcript files and attempts to add punctuation sentence structure and
then saves as a .md file

The scrape_transcripts script scrapes the Youtube channel selected and saves the transcripts to a 
folder which can then be handed off to the transcripts_punctuation script to create a bit
better structure to what is normally a chaotic mass of run on text without any periods.

The transcripts_punctuation script takes a folder (make sure to change transcript_dir folder name) 
containing .txt transcript files that are typically very long and do not contain 
any periods to separate the file into any sort of sentence structure. This script 
guesses at a reasonable sentence structure by adding periods before a list of common words. 
which seems to do a reasonable job creating logical sentence structure. The script also tries to chunk
the text into markdown headings which seems to work better if used with software like Obsidian Smart Connections plugin. It is then a bit more suitable for use with their embeddings feature.
